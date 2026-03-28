import os
import re
from datetime import datetime

ARTICLE_DIR = "articles"
INDEX_FILE = "index.html"

title = input("Enter Article title: ")
date_str = datetime.now().strftime("%Y-%m-%d")

if not os.path.exists(ARTICLE_DIR):
    os.makedirs(ARTICLE_DIR)

files = os.listdir(ARTICLE_DIR)
numbers = [
    int(re.search(r"^(\d+)\.html$", f).group(1))
    for f in files
    if re.search(r"^(\d+)\.html$", f)
]
next_num = max(numbers) + 1 if numbers else 1
new_filename = f"{next_num}.html"
new_filepath = os.path.join(ARTICLE_DIR, new_filename)

html_template = f"""
<!doctype html>
<html>
    <head>
        <meta charset="UTF-8" />
        <link rel="stylesheet" href="../style.css" />
        <link rel="icon" href="/public/minerva-juppiter.svg" />
        <title>{title}</title>
    </head>
    <body>
        <header>
            <h1>Blog</h1>
            <h2>by Minerva_Juppiter</h2>
            <nav>
                <a href="/">Home</a>
                /
                <a href="/about">About</a>
            </nav>
        </header>
        <article>
            <h1>{title}</h1>
            <h3>{date_str}</h3>
        </article>
        <footer>
            <p>@all right reserved by Minerva_Juppiter</p>
        </footer>
    </body>
</html>"""

with open(new_filepath, "w", encoding="utf-8") as f:
    f.write(html_template)

if os.path.exists(INDEX_FILE):
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_li = f'                    <li>\n                        <a href="{ARTICLE_DIR}/{new_filename}">{title}</a>\n                    </li>\n'

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if "<ul>" in line:
                f.write(new_li)

print(f"Generated: {new_filepath}")
print(f"Updated: {INDEX_FILE} (Inserted '{title}' at the top of the list)")
