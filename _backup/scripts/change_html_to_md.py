import os


DIRECTORY = "./"

for filename in os.listdir(DIRECTORY):
    if filename.endswith(".html"):
        no_html = os.path.splitext(filename)[0]
        os.rename(filename, no_html + ".md")
