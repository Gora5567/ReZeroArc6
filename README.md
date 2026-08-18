# Re:Zero Arc 6 — EPUB Builder

A Python-based project for collecting, cleaning, formatting and compiling the Re:Zero Web Novel Arc 6 into a single EPUB book.

The project was created to make the Web Novel more convenient to read on an e-reader.

## Features

* Collects chapter links from the source website
* Downloads chapter pages automatically
* Extracts the relevant HTML content
* Removes unnecessary page elements
* Supports different chapter page structures
* Cleans and formats individual chapters
* Compiles all 90 chapters into a single EPUB
* Generates a clickable table of contents
* Adds EPUB metadata
* Supports a custom book cover
* Produces a ready-to-read EPUB file

## Requirements

* Python 3.10+
* pip

## Installation

Clone the repository:

```bash
git clone https://github.com/Gora5567/ReZeroArc6.git
cd ReZeroArc6
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Download the chapters

Run the downloader:

```bash
python downloader.py
```

The downloader collects the available chapter pages and saves them locally for further processing.

### 2. Clean and format the chapters

The downloaded chapters are processed using the project's HTML templates. Different templates are used when the source website uses different page structures.

### 3. Build the EPUB

Run:

```bash
python epub_builder.py
```

The final EPUB will be generated in the `output/` directory.

## Project Structure

```text
ReZeroArc6/
│
├── assets/
│   ├── cover.jpeg
│   └── cover_final.jpeg
│
├── output/
│   └── Re_Zero_Arc_6.epub
│
├── main.py
├── downloader.py
├── template.py
├── other_template.py
├── epub_builder.py
├── make_cover.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## EPUB

The generated book contains:

* An introduction
* A clickable table of contents
* All 90 chapters of Arc 6
* Formatted chapter titles
* EPUB metadata
* A custom cover
* Navigation between chapters

The final result is designed to be comfortable to read on an e-reader or EPUB-compatible application.

## Credits

**Re:Zero − Starting Life in Another World**
Original work by **Tappei Nagatsuki**.

EPUB compilation, formatting and tooling by **Gora**.

Created with assistance from **ChatGPT by OpenAI**.

The source material and fan translation belong to their respective authors and translators. This project does not claim ownership of the original work.

## Source

The English text used for the compilation was obtained from:

**Witch Cult Translations**

https://witchculttranslation.com/

## Disclaimer

This is a fan-made project created for personal and archival purposes.

All rights to the original Re:Zero work belong to their respective copyright holders.

This project is not affiliated with or endorsed by Tappei Nagatsuki, Witch Cult Translations, or any official Re:Zero publisher.

## License

The code in this repository is provided for educational and personal use.

The original Re:Zero text, characters, names and other copyrighted material are not owned by this project.
