from bs4 import BeautifulSoup
import os

def clean_chapter(input_file, output_file):
    # Открываем исходную страницу
    with open(input_file, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")

    # Заголовок
    title = soup.find(class_="entry-title")

    if title is None:
        print(f"❌ Заголовок не найден: {input_file}")
        return

    # Текст главы
    content = soup.find(class_="entry-content")

    if content is None:
        print(f"❌ entry-content не найден: {input_file}")
        return

    # Удаляем первые 8 элементов мусора
    elements = content.find_all(recursive=False)

    for element in elements[:8]:
        element.decompose()

    # Создаём готовый HTML
    output = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title.get_text(strip=True)}</title>

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

<h1>{title.get_text(strip=True)}</h1>
<hr>

{content.decode_contents()}

</body>
</html>
"""
    os.makedirs("../clean_chapters", exist_ok=True)

    # Сохраняем
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(output)

    print(f"✅ {input_file} → {output_file}")