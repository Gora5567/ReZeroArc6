# Re:Zero Arc 6 — EPUB Builder

A Python-based project for collecting, cleaning, formatting and compiling the **Re:Zero Web Novel Arc 6** into a single EPUB book.

The project was created to make the Web Novel more convenient to read on an e-reader.

## Features

* Downloads all 90 chapters of Arc 6 automatically
* Uses different cleaning templates for different chapter structures
* Removes unnecessary HTML elements
* Cleans and formats the downloaded chapters
* Compiles all 90 chapters into a single EPUB
* Generates a clickable table of contents
* Adds EPUB metadata
* Adds a custom book cover
* Produces a ready-to-read EPUB file
* Runs the entire process through a single `main.py` script
* Allows the user to stop between major processing stages

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

The entire project is controlled through `main.py`.

Run:

```bash
python src/main.py
```

### 1. Start the program

When the program starts, it asks:

```text
Do you wish to start? (Y/N)
```

Enter:

* `Y` or `y` — start the process
* `N` or `n` — stop the program
* Any other character — stop the program

### 2. Download the chapters

After starting, the program automatically downloads the 90 Arc 6 chapters.

The downloaded HTML files are saved to:

```text
chapters/
```

The downloader currently uses:

* **Witch Cult Translations** for chapters 1–88
* **Eminent Translations** for chapters 89–90

The downloaded chapters are numbered automatically:

```text
chapter_01.html
chapter_02.html
...
chapter_90.html
```

### 3. Clean and format the chapters

After downloading, the program asks whether you want to continue to the cleaning stage.

Enter:

```text
Y
```

or

```text
y
```

to continue.

Any other character stops the process.

The program then processes the downloaded chapters.

Chapters 1–88 use the main cleaning template:

```text
template.py
```

Chapters 89–90 use a separate template because their source pages have a different HTML structure:

```text
template_other.py
```

The cleaned chapters are saved to:

```text
clean_chapters/
```

For example:

```text
chapter_01_clean.html
chapter_02_clean.html
...
chapter_90_clean.html
```

### 4. Build the EPUB

After the cleaning stage, the program asks whether you want to continue with creating the book.

Enter:

```text
Y
```

or

```text
y
```

to continue.

Any other character stops the process.

The EPUB builder then creates the final book using the cleaned chapters.

The finished EPUB is saved to:

```text
output/Re_Zero_Arc_6.epub
```

## Project Structure

```text
ReZeroArc6/
│
├── assets/
│   ├── cover.jpeg
│   └── cover_final.jpeg
│
├── chapters/
│   └── chapter_01.html
│   └── ...
│   └── chapter_90.html
│
├── clean_chapters/
│   └── chapter_01_clean.html
│   └── ...
│   └── chapter_90_clean.html
│
├── output/
│   └── Re_Zero_Arc_6.epub
│
├── src/
│   ├── main.py
│   ├── downloader.py
│   ├── template.py
│   ├── template_other.py
│   ├── epub_builder.py
│   └── make_cover.py
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

The final result is designed to be comfortable to read on an e-reader or any EPUB-compatible application.

## Credits

**Re:Zero − Starting Life in Another World**
Original work by **Tappei Nagatsuki**.

EPUB compilation, formatting and tooling by **Gora**.

Created with assistance from **ChatGPT by OpenAI**.

The source material and fan translations belong to their respective authors and translators. This project does not claim ownership of the original work.

## Sources

The English text used for the compilation was obtained from:

**Witch Cult Translations**

https://witchculttranslation.com/

Chapters 89–90 are obtained from:

**Eminent Translations**

https://eminenttranslations.com/

## Disclaimer

This is a fan-made project created for personal and archival purposes.

All rights to the original *Re:Zero* work belong to their respective copyright holders.

This project is not affiliated with or endorsed by Tappei Nagatsuki, Witch Cult Translations, Eminent Translations, or any official *Re:Zero* publisher.

## License

The code in this repository is provided for educational and personal use.

The original *Re:Zero* text, characters, names and other copyrighted material are not owned by this project.
