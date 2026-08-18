from pathlib import Path

from downloader import download_chapters
from template import clean_chapter
from template_other import clean_other_chapter
from epub_builder import build_epub


# ==========================================
# PATHS
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CHAPTERS_DIR = PROJECT_ROOT / "chapters"
CLEAN_CHAPTERS_DIR = PROJECT_ROOT / "clean_chapters"


# ==========================================
# ВОПРОС
# ==========================================

def ask_to_continue(question):

    answer = input(
        f"\n{question} (Y/N): "
    ).strip().lower()

    return answer == "y"


# ==========================================
# START
# ==========================================

print("\n" + "=" * 55)
print("📖 Re:Zero Arc 6 — EPUB Builder")
print("=" * 55)


# ==========================================
# 1. DOWNLOAD
# ==========================================

if not ask_to_continue(
    "Do you wish to start downloading chapters?"
):

    print("\n🛑 Process stopped.")
    exit()


print("\n" + "=" * 55)
print("📥 DOWNLOADING CHAPTERS")
print("=" * 55)

download_chapters()


# ==========================================
# 2. CLEANING
# ==========================================

if not ask_to_continue(
    "Do you wish to continue to the cleaning?"
):

    print("\n🛑 Process stopped.")
    exit()


print("\n" + "=" * 55)
print("🧹 CLEANING CHAPTERS")
print("=" * 55)

CLEAN_CHAPTERS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================
# CHAPTERS 1–88
# ==========================================

print("\n🧹 Cleaning chapters 1–88...\n")

for i in range(1, 89):

    input_file = (
        CHAPTERS_DIR /
        f"chapter_{i:02d}.html"
    )

    output_file = (
        CLEAN_CHAPTERS_DIR /
        f"chapter_{i:02d}_clean.html"
    )

    if not input_file.exists():

        print(
            f"⚠️ File not found: {input_file}"
        )

        continue

    clean_chapter(
        str(input_file),
        str(output_file)
    )


# ==========================================
# CHAPTERS 89–90
# ==========================================

print("\n🧹 Cleaning chapters 89–90...\n")

for i in range(89, 91):

    input_file = (
        CHAPTERS_DIR /
        f"chapter_{i:02d}.html"
    )

    output_file = (
        CLEAN_CHAPTERS_DIR /
        f"chapter_{i:02d}_clean.html"
    )

    if not input_file.exists():

        print(
            f"⚠️ File not found: {input_file}"
        )

        continue

    clean_other_chapter(
        str(input_file),
        str(output_file)
    )


print("\n✅ Cleaning finished!")


# ==========================================
# 3. EPUB
# ==========================================

if not ask_to_continue(
    "Do you wish to continue to build the EPUB?"
):

    print("\n🛑 Process stopped.")
    exit()


print("\n" + "=" * 55)
print("📚 BUILDING EPUB")
print("=" * 55)

build_epub()


# ==========================================
# DONE
# ==========================================

print("\n" + "=" * 55)
print("🎉 PROJECT COMPLETE!")
print("=" * 55)