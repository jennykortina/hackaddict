import os

# pip install python-frontmatter
import frontmatter

DIRECTORY = "./"

for filename in os.listdir(DIRECTORY):
    if filename.endswith(".md"):
        fname = os.path.join(DIRECTORY, filename)
        with open(fname) as f:
            post = frontmatter.load(f)
            blogger_orig_url = post.metadata["blogger_orig_url"]
            post.metadata["redirect_from"] = blogger_orig_url.split(
                "https://www.hackaddict.net/"
            )[1]
            new_content = frontmatter.dumps(post)

        with open(filename, "w") as f:
            f.write(new_content)
