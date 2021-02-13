import re
import requests
import os

# pip install python-frontmatter
import frontmatter

# IMPORTANT: Before running this script manually create a folder /assets/images/thumbnails # noqa

DIRECTORY = "./"
DATE_RE = re.compile("(?P<date>[0-9]+\-[0-9]+\-[0-9]+)")

for filename in os.listdir(DIRECTORY):
    if filename.endswith(".md"):
        date_prefix = DATE_RE.search(filename).group("date")
        fname = os.path.join(DIRECTORY, filename)
        with open(fname) as f:
            file_index = 0
            post = frontmatter.load(f)
            thumb_url = post.metadata.get("thumbnail", None)
            if thumb_url is None:
                continue
            extstart = thumb_url.rfind(".")
            extension = thumb_url[extstart:]
            newfile = date_prefix + "-image-{:04d}{}".format(
                file_index, extension
            )  # noqa
            file_index += 1
            print("{} => {}".format(thumb_url, newfile))
            filepath = "../assets/images/thumbnails/" + newfile
            r = None
            try:
                r = requests.get(thumb_url, timeout=2)
            except Exception as e:
                print(f"ERROR: {e}")
            if r is not None:
                with open(filepath, "wb") as outfile:
                    outfile.write(r.content)
                post["thumbnail"] = (
                    "{{ site.url }}/assets/images/thumbnails/" + newfile
                )  # noqa
                new_content = frontmatter.dumps(post)
                with open(filename, "w") as f:
                    f.write(new_content)
