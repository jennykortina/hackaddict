import re
import requests
import os

# pip install BeautifulSoup4
from bs4 import BeautifulSoup

# IMPORTANT: Before running this script manually create a folder /assets/images/thumbnails # noqa

DIRECTORY = "./"
IMG_RE = re.compile('<img[^>]+src="(?P<src>[^"]+)"')
DATE_RE = re.compile("(?P<date>[0-9]+\-[0-9]+\-[0-9]+)")

for filename in os.listdir(DIRECTORY):
    if filename.endswith(".html"):
        date_prefix = DATE_RE.search(filename).group("date")
        fname = os.path.join(DIRECTORY, filename)
        with open(fname, "r") as f:
            file_index = 0
            contents = f.read()

            # download and replace images
            for match in IMG_RE.finditer(contents):
                sourceurl = match.group("src")
                extstart = sourceurl.rfind(".")
                extension = sourceurl[extstart:]
                newfile = date_prefix + "-image-{:04d}{}".format(
                    file_index, extension
                )  # noqa
                file_index += 1
                print("{} => {}".format(sourceurl, newfile))
                filepath = "../assets/images/posts/" + newfile
                try:
                    r = requests.get(sourceurl, timeout=2)
                    with open(filepath, "wb") as outfile:
                        outfile.write(r.content)
                    contents = contents.replace(
                        sourceurl,
                        "{{ site.url }}/assets/images/posts/" + newfile,  # noqa
                    )
                except Exception as e:
                    print(e)

            # remove href wrapping images
            contents = BeautifulSoup(contents, "html.parser")
            for img in contents.find_all("img"):
                if img.parent.name == "a":
                    img.parent.unwrap()
                    try:
                        img["style"] = (
                            img["style"]
                            .replace("cursor:pointer;", "")
                            .replace("cursor:hand;", "")
                            .replace("cursor: pointer;", "")
                            .replace("cursor: hand;", "")
                        )
                    except Exception as e:
                        print(e)

        with open(filename, "w") as f:
            f.write(str(contents))