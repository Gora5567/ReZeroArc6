from bs4 import BeautifulSoup


def clean_other_chapter(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")

    # Main chapter text container
    content = soup.find("div", class_="reader-paged-content")

    if content is None:
        print(f"❌ Chapter text not found: {input_file}")
        return

    # Chapter title
    title = soup.find("h1")

    if title is not None:
        title_text = title.get_text(" ", strip=True)
    else:
        title_text = soup.title.get_text(" ", strip=True) if soup.title else "Re:Zero"

    # Remove the duplicate title ONLY from the body
    duplicate_title = content.find(
        class_="mb-[1em] mt-[2em] text-center text-[2xl] md:text-4xl"
    )

    if duplicate_title is not None:
        duplicate_title.decompose()

    chapter_text = content.decode_contents()

    output = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title_text}</title>

    <style>
        body {{
            margin: 0;
            padding: 20px;
            line-height: 1.6;
            font-family: serif;
        }}

        h1 {{
            text-align: center;
            font-size: 1.8em;
            margin-bottom: 0.5em;
        }}

        hr {{
            border: 0;
            border-top: 1px solid #888;
            margin: 1.5em 0;
        }}

        p {{
            margin-bottom: 1em;
        }}
    </style>
</head>

<body>

<h1>{title_text}</h1>

<hr>

{chapter_text}

</body>
</html>
"""

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(output)

    print(f"✅ {input_file} → {output_file}")