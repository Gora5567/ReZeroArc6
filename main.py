import os

from downloader import download_chapters
from template import clean_chapter
from template_other import clean_other_chapter


# ==========================================
# 1. СКАЧИВАЕМ ВСЕ ГЛАВЫ
# ==========================================

print("\n📥 Начинаем скачивание глав...\n")

download_chapters()


# ==========================================
# 2. СОЗДАЁМ ПАПКУ ДЛЯ ГОТОВЫХ ГЛАВ
# ==========================================

os.makedirs("clean_chapters", exist_ok=True)


# ==========================================
# 3. ОБРАБАТЫВАЕМ ГЛАВЫ 1–88
# ==========================================

print("\n🧹 Обрабатываем главы 1–88...\n")

for i in range(1, 89):

    input_file = f"chapters/chapter_{i:02d}.html"
    output_file = f"clean_chapters/chapter_{i:02d}_clean.html"

    if not os.path.exists(input_file):
        print(f"⚠️ Файл не найден: {input_file}")
        continue

    clean_chapter(input_file, output_file)


# ==========================================
# 4. ОБРАБАТЫВАЕМ ГЛАВЫ 89–90
# ==========================================

print("\n🧹 Обрабатываем главы 89–90...\n")

for i in range(89, 91):

    input_file = f"chapters/chapter_{i:02d}.html"
    output_file = f"clean_chapters/chapter_{i:02d}_clean.html"

    if not os.path.exists(input_file):
        print(f"⚠️ Файл не найден: {input_file}")
        continue

    clean_other_chapter(input_file, output_file)


# ==========================================
# 5. ГОТОВО
# ==========================================

print("\n" + "=" * 50)
print("🎉 ВСЁ ГОТОВО!")
print("=" * 50)

print("\n📁 Исходные главы:")
print("   chapters/")

print("\n📖 Очищенные главы:")
print("   clean_chapters/")

print("\nТеперь можно проверить:")
print("   chapter_01_clean.html")
print("   chapter_50_clean.html")
print("   chapter_89_clean.html")
print("   chapter_90_clean.html")