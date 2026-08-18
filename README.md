# Re:Zero Arc 6 — EPUB Builder

A Python-based project for collecting, cleaning, formatting and compiling the **Re:Zero Web Novel Arc 6 — Corridor of Memories** into a single EPUB book.

The goal of this project is to make the Web Novel more convenient to read on e-readers and EPUB-compatible applications.

## 📖 Download the EPUB

If you only want to read the book, you **do not need to install Python or run the project**.

The latest ready-to-read EPUB can be downloaded from the project's GitHub Releases:

**[Download the latest EPUB](https://github.com/Gora5567/ReZeroArc6/releases/latest)**

The release contains the compiled **Re:Zero Arc 6 EPUB** with all 90 chapters.

---

## ✨ Features

* Downloads all 90 chapters of Arc 6 automatically
* Supports multiple source websites
* Uses different cleaning templates for different chapter structures
* Removes unnecessary HTML elements
* Cleans and formats downloaded chapters
* Compiles all 90 chapters into a single EPUB
* Generates a clickable table of contents
* Adds EPUB metadata
* Adds a custom book cover
* Produces a ready-to-read EPUB
* Runs the entire process through a single `main.py` script
* Allows the user to stop between major processing stages

---

## 📋 Requirements

* Python 3.10+
* pip

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Gora5567/ReZeroArc6.git
cd ReZeroArc6
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

The entire project is controlled through:

```text
src/main.py
```

Run:

```bash
python src/main.py
```

The program guides you through the entire process.

---

### 1. Start the program

When the program starts, it asks:

```text
Do you wish to start? (Y/N)
```

Enter:

* `Y` or `y` — start the process
* `N` or `n` — stop the program
* Any other character — stop the program

---

### 2. Download the chapters

After starting, the program automatically downloads all 90 Arc 6 chapters.

The downloaded HTML files are saved to:

```text
chapters/
```

The downloader currently uses:

* **Witch Cult Translations** — Chapters 1–88
* **Eminent Translations** — Chapters 89–90

The chapters are automatically numbered:

```text
chapter_01.html
chapter_02.html
...
chapter_90.html
```

After downloading is complete, the program asks whether you want to continue.

---

### 3. Clean and format the chapters

The program asks whether you want to continue to the cleaning stage.

Enter:

```text
Y
```

or:

```text
y
```

to continue.

Any other character stops the process.

The project uses two different cleaning templates because the source websites use different HTML structures.

#### Chapters 1–88

Use:

```text
src/template.py
```

#### Chapters 89–90

Use:

```text
src/template_other.py
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

After the cleaning stage is complete, the program asks whether you want to continue with creating the EPUB.

---

### 4. Build the EPUB

Enter:

```text
Y
```

or:

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

When the process finishes, the program displays the number of successfully included chapters.

---

## 📚 EPUB Contents

The generated EPUB contains:

* An introduction
* A clickable table of contents
* All 90 chapters of Arc 6
* Formatted chapter titles
* EPUB metadata
* A custom cover
* Navigation between chapters
* A reading-friendly layout

The EPUB is designed to work with EPUB-compatible e-readers and reading applications.

---

## 📁 Project Structure

```text
ReZeroArc6/
│
├── assets/
│   ├── cover.jpeg
│   └── cover_final.jpeg
│
├── chapters/
│   ├── chapter_01.html
│   ├── ...
│   └── chapter_90.html
│
├── clean_chapters/
│   ├── chapter_01_clean.html
│   ├── ...
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

---

## 🌐 Sources

The English text used for the compilation was obtained from fan translation websites.

### Witch Cult Translations

Used for Chapters 1–88.

https://witchculttranslation.com/

### Eminent Translations

Used for Chapters 89–90.

https://eminenttranslations.com/

Please support the original translators and visit their websites.

---

## 👤 Credits

**Re:Zero − Starting Life in Another World**
Original work by **Tappei Nagatsuki**.

EPUB compilation, formatting and tooling by **Gora**.

Created with assistance from **ChatGPT by OpenAI**.

The source material and fan translations belong to their respective authors and translators. This project does not claim ownership of the original work.

---

## ⚠️ Disclaimer

This is a fan-made project created for **personal reading and archival purposes**.

All rights to the original *Re:Zero* work, including its characters, story, names and other copyrighted material, belong to their respective copyright holders.

This project is **not affiliated with, sponsored by, or endorsed by**:

* Tappei Nagatsuki
* Witch Cult Translations
* Eminent Translations
* Any official *Re:Zero* publisher

---

## 📜 License

The code in this repository is provided for educational and personal use.

The original *Re:Zero* text, characters, names, translations and other copyrighted material are **not owned by this project**.

---

## ⭐ If You Find This Project Useful

If this project helped you create or read an EPUB version of Arc 6, consider giving the repository a ⭐ on GitHub.

**[Download the latest EPUB →](https://github.com/Gora5567/ReZeroArc6/releases/latest)**
