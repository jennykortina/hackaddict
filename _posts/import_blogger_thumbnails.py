import re
import requests
import os

# pip install python-frontmatter
import frontmatter

DIRECTORY = "./"
DATE_RE = re.compile("(?P<date>[0-9]+\-[0-9]+\-[0-9]+)")

for filename in os.listdir(DIRECTORY):
    if filename.endswith(".md"):
        date_prefix = DATE_RE.search(filename).group("date")
        fname = os.path.join(DIRECTORY, filename)
        with open(fname) as f:
            file_index = 0
            post = frontmatter.load(f)
            sourceurl = post.metadata["thumbnail"]
            extstart = sourceurl.rfind(".")
            extension = sourceurl[extstart:]
            newfile = date_prefix + "-image-{:04d}{}".format(
                file_index, extension
            )  # noqa
            file_index += 1
            print("{} => {}".format(sourceurl, newfile))
            filepath = "../assets/images/thumbnails/" + newfile
            try:
                r = requests.get(sourceurl, timeout=2)
                with open(filepath, "wb") as outfile:
                    outfile.write(r.content)
                post["thumbnail"] = (
                    "{{ site.url }}/assets/images/thumbnails/" + newfile
                )  # noqa
                new_content = frontmatter.dumps(post)

            except Exception as e:
                print(e)

        with open(filename, "w") as f:
            f.write(new_content)
