import os

from bs4 import BeautifulSoup
from ebooklib import epub


# ==========================================
# НАСТРОЙКИ
# ==========================================

CLEAN_CHAPTERS_DIR = "../clean_chapters"
OUTPUT_FILE = "../output/Re_Zero_Arc_6.epub"


# ==========================================
# СОЗДАНИЕ EPUB
# ==========================================

def build_epub():

    book = epub.EpubBook()

    # ==========================================
    # МЕТАДАННЫЕ
    # ==========================================

    book.set_identifier("rezero-arc-6")
    book.set_title("Re:Zero — Arc 6: Corridor of Memories")
    book.set_language("en")

    # Авторы
    book.add_author("Tappei Nagatsuki")
    book.add_author("Gora")

    # ==========================================
    # CSS
    # ==========================================

    style = """
    body {
        margin: 0;
        padding: 20px;
        line-height: 1.6;
        font-family: serif;
    }

    h1 {
        text-align: center;
        font-size: 1.9em;
        margin-bottom: 0.5em;
    }

    h2 {
        text-align: center;
        font-size: 1.4em;
        margin-bottom: 0.5em;
    }

    hr {
        border: 0;
        border-top: 1px solid #888;
        margin: 1.5em 0;
    }

    p {
        margin-bottom: 1em;
    }

    .intro {
        text-align: center;
        margin-top: 5%;
    }

    .description {
        text-align: left;
        margin-top: 2em;
    }

    .description p {
        margin-bottom: 0.9em;
    }

    .credits {
        text-align: center;
        font-size: 0.85em;
        margin-top: 2em;
    }

    .toc-page {
        margin-top: 5%;
    }

    .toc-page h1 {
        margin-bottom: 1.5em;
    }

    .toc-list {
        padding: 0;
        list-style: none;
    }

    .toc-list li {
        margin-bottom: 0.7em;
    }

    .toc-list a {
        text-decoration: none;
    }
    """

    css = epub.EpubItem(
        uid="style",
        file_name="style/style.css",
        media_type="text/css",
        content=style.encode("utf-8")
    )

    book.add_item(css)

    # ==========================================
    # INTRO
    # ==========================================

    intro = epub.EpubHtml(
        title="Re:Zero — Arc 6",
        file_name="intro.xhtml",
        lang="en"
    )

    intro.content = """
    <html>

    <head>
        <title>Re:Zero — Arc 6: Corridor of Memories</title>
    </head>

    <body>

        <div class="intro">

            <h1>Re:Zero</h1>

            <h2>Arc 6 — Corridor of Memories</h2>

            <p>
                <em>by Tappei Nagatsuki</em>
            </p>

            <p>
                <small>EPUB edition by Gora</small>
            </p>

            <hr>

            <div class="description">

                <p>
                    A mysterious tower stands in the middle of the vast
                    Augria Sand Dunes, holding secrets that have remained
                    untouched for centuries.
                </p>

                <p>
                    Subaru Natsuki and his companions journey into the desert
                    in search of the Sage Shaula. But the tower holds trials
                    far more dangerous than they could have imagined.
                </p>

                <p>
                    Here, memories can become weapons, the past can become
                    a prison, and losing one's name may mean losing one's
                    very identity.
                </p>

                <p>
                    <strong>
                        If you lose your memories, your name, and everything
                        that tells you who you are… what remains?
                    </strong>
                </p>

            </div>

            <hr>

            <div class="credits">

                <p>
                    <strong>Original Work</strong><br>
                    <em>
                        Re:Zero − Starting Life in Another World
                    </em><br>
                    by Tappei Nagatsuki
                </p>

                <p>
                    <strong>EPUB Compilation</strong><br>
                    Compiled and formatted by Gora
                </p>

                <p>
                    Created with assistance from
                    ChatGPT by OpenAI.
                </p>

                <p>
                    Source material collected from
                    Witch Cult Translations,
                    a fan translation website dedicated to
                    <em>
                        Re:Zero − Starting Life in Another World
                    </em>.
                </p>

                <p>
                    This EPUB was created for personal reading
                    and archival purposes.
                </p>

                <p>
                    All rights to the original work belong to their
                    respective creators and rights holders.
                </p>

            </div>

        </div>

    </body>

    </html>
    """

    book.add_item(intro)

    # ==========================================
    # ГЛАВЫ
    # ==========================================

    chapters = []

    print("\n📚 Adding chapters...\n")

    for i in range(1, 91):

        filename = f"chapter_{i:02d}_clean.html"

        filepath = os.path.join(
            CLEAN_CHAPTERS_DIR,
            filename
        )

        # Проверяем файл
        if not os.path.exists(filepath):

            print(
                f"⚠️ Chapter not found: {filepath}"
            )

            continue

        # Читаем HTML
        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            html = file.read()

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        # ==========================================
        # ЗАГОЛОВОК ГЛАВЫ
        # ==========================================

        title = soup.find("h1")

        if title:

            chapter_title = title.get_text(
                " ",
                strip=True
            )

        else:

            chapter_title = f"Chapter {i}"

        # Убираем "Arc 6, "
        if chapter_title.startswith("Arc 6, "):

            chapter_title = chapter_title[7:]

        # ==========================================
        # BODY
        # ==========================================

        body = soup.find("body")

        if body:

            content = body.decode_contents()

        else:

            content = html

        # ==========================================
        # СОЗДАЁМ EPUB-ГЛАВУ
        # ==========================================

        chapter = epub.EpubHtml(
            title=chapter_title,
            file_name=f"chapter_{i:02d}.xhtml",
            lang="en"
        )

        chapter.content = f"""
        <html>

        <head>
            <title>{chapter_title}</title>
        </head>

        <body>

            {content}

        </body>

        </html>
        """

        chapter.add_item(css)

        book.add_item(chapter)

        chapters.append(chapter)

        print(
            f"📖 {i:02d}/90 — {chapter_title}"
        )

    # ==========================================
    # ВИЗУАЛЬНАЯ СТРАНИЦА CONTENTS
    # ==========================================

    toc_page = epub.EpubHtml(
        title="Contents",
        file_name="contents.xhtml",
        lang="en"
    )

    toc_links = ""

    for chapter in chapters:

        toc_links += f"""
        <li>
            <a href="{chapter.file_name}">
                {chapter.title}
            </a>
        </li>
        """

    toc_page.content = f"""
    <html>

    <head>
        <title>Contents</title>
    </head>

    <body>

        <div class="toc-page">

            <h1>Contents</h1>

            <ul class="toc-list">

                {toc_links}

            </ul>

        </div>

    </body>

    </html>
    """

    book.add_item(toc_page)

    # ==========================================
    # ОБЛОЖКА
    # ==========================================

    with open("../assets/cover_final.jpeg", "rb") as cover_file:
        cover_image = cover_file.read()

    book.set_cover(
        "cover_final.jpeg",
        cover_image
    )

    # ==========================================
    # EPUB NAVIGATION
    # ==========================================

    book.add_item(
        epub.EpubNcx()
    )

    book.add_item(
        epub.EpubNav()
    )

    # ==========================================
    # НАЧАЛЬНАЯ СТРАНИЦА
    # ==========================================
    #
    # Ридер должен открывать книгу сразу
    # с intro.xhtml, а не с Contents.

    book.guide = [
        {
            "type": "text",
            "title": "Start",
            "href": "intro.xhtml"
        }
    ]

    # ==========================================
    # ПОРЯДОК СТРАНИЦ
    # ==========================================

    book.spine = [
        intro,
        toc_page
    ] + chapters

    # ==========================================
    # СОХРАНЕНИЕ
    # ==========================================

    print("\n💾 Creating EPUB...\n")

    epub.write_epub(
        OUTPUT_FILE,
        book,
        {}
    )

    # ==========================================
    # ФИНАЛ
    # ==========================================

    print("\n" + "=" * 55)
    print("🎉 EPUB READY!")
    print("=" * 55)

    print(
        f"\n📖 File: {OUTPUT_FILE}"
    )

    print(
        f"📚 Chapters: {len(chapters)}/90"
    )

    if len(chapters) == 90:

        print(
            "✅ All 90 chapters are included!"
        )

    else:

        print(
            "⚠️ WARNING: Not all chapters were found!"
        )


# ==========================================
# ЗАПУСК
# ==========================================

if __name__ == "__main__":

    build_epub()