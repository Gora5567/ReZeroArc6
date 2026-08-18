import os

import requests
from bs4 import BeautifulSoup


ARC_URL = "https://witchculttranslation.com/arc-6/"

# Корень проекта ReZeroArc6
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Папка для исходных глав
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")


def download_chapters():
    # Создаём папку для исходных глав
    os.makedirs(CHAPTERS_DIR, exist_ok=True)

    # Получаем страницу Arc 6
    response = requests.get(ARC_URL)

    if response.status_code != 200:
        print(f"❌ Не удалось получить Arc 6: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    chapters = []

    # Ищем ссылки на главы
    for link in soup.find_all("a"):
        text = link.get_text(" ", strip=True)
        url = link.get("href")

        if not url:
            continue

        # Если это Arc 10 — нахуй
        if "Arc 10" in text:
            continue

        # Берём только ссылки, в названии которых есть Chapter
        if "Chapter" in text:
            chapters.append((text, url))

    print(f"📚 Найдено глав: {len(chapters)}")

    # Скачиваем главы
    for i, (title, url) in enumerate(chapters, start=1):

        print(f"\n⬇️ {i}. {title}")
        print(f"   {url}")

        try:
            chapter_response = requests.get(
                url,
                timeout=30
            )

            if chapter_response.status_code != 200:
                print(
                    f"   ❌ Ошибка: "
                    f"{chapter_response.status_code}"
                )
                continue

            filename = os.path.join(
                CHAPTERS_DIR,
                f"chapter_{i:02d}.html"
            )

            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as file:
                file.write(chapter_response.text)

            print(f"   ✅ Сохранено: {filename}")

        except requests.RequestException as error:
            print(
                f"   ❌ Ошибка соединения: {error}"
            )

    print("\n🎉 Скачивание завершено!")


if __name__ == "__main__":
    download_chapters()