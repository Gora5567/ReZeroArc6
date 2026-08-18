from PIL import Image, ImageDraw, ImageFont


INPUT_FILE = "../assets/cover.jpeg"
OUTPUT_FILE = "../assets/cover_final.jpeg"


# ==========================================
# ОТКРЫВАЕМ ИЗОБРАЖЕНИЕ
# ==========================================

image = Image.open(INPUT_FILE).convert("RGB")

width, height = image.size

draw = ImageDraw.Draw(image)


# ==========================================
# ШРИФТЫ
# ==========================================

# macOS
FONT_BOLD = "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Times New Roman.ttf"


title_font = ImageFont.truetype(
    FONT_BOLD,
    int(width * 0.17)
)

subtitle_font = ImageFont.truetype(
    FONT_REGULAR,
    int(width * 0.07)
)

authors_font = ImageFont.truetype(
    FONT_REGULAR,
    int(width * 0.064)
)


# ==========================================
# RE:ZERO
# ==========================================

title = "Re:Zero"

bbox = draw.textbbox(
    (0, 0),
    title,
    font=title_font
)

title_width = bbox[2] - bbox[0]
title_height = bbox[3] - bbox[1]

title_x = (width - title_width) // 2
title_y = int(height * 0.08)


# ==========================================
# ТЕНЬ
# ==========================================

shadow_offset = max(2, int(width * 0.004))

draw.text(
    (
        title_x + shadow_offset,
        title_y + shadow_offset
    ),
    title,
    font=title_font,
    fill=(0, 0, 0)
)

draw.text(
    (title_x, title_y),
    title,
    font=title_font,
    fill=(255, 255, 255)
)


# ==========================================
# ARC 6
# ==========================================

subtitle = "Arc 6 — Corridor of Memories"

bbox = draw.textbbox(
    (0, 0),
    subtitle,
    font=subtitle_font
)

subtitle_width = bbox[2] - bbox[0]

subtitle_x = (width - subtitle_width) // 2
subtitle_y = title_y + title_height + int(height * 0.015)


draw.text(
    (
        subtitle_x + shadow_offset,
        subtitle_y + shadow_offset
    ),
    subtitle,
    font=subtitle_font,
    fill=(0, 0, 0)
)

draw.text(
    (subtitle_x, subtitle_y),
    subtitle,
    font=subtitle_font,
    fill=(255, 255, 255)
)


# ==========================================
# АВТОРЫ
# ==========================================

authors = "Tappei Nagatsuki · Gora"

bbox = draw.textbbox(
    (0, 0),
    authors,
    font=authors_font
)

authors_width = bbox[2] - bbox[0]
authors_height = bbox[3] - bbox[1]

authors_x = (width - authors_width) // 2

authors_y = int(
    height * 0.91
)


# ==========================================
# ТЕНЬ АВТОРОВ
# ==========================================

draw.text(
    (
        authors_x + shadow_offset,
        authors_y + shadow_offset
    ),
    authors,
    font=authors_font,
    fill=(0, 0, 0)
)

draw.text(
    (authors_x, authors_y),
    authors,
    font=authors_font,
    fill=(255, 255, 255)
)


# ==========================================
# СОХРАНЕНИЕ
# ==========================================

image.save(
    OUTPUT_FILE,
    "JPEG",
    quality=95
)

print(f"✅ Обложка готова: {OUTPUT_FILE}")