# OCR_P2

OpenClassrooms' Python Project 2 is a small web scraper with multithreading that goes site->categories->books into a CSV file.

For a full scrap of http://books.toscrape.com multithreading makes it 7x faster ! (14 min before vs 2 min with multithreading).

## Installation

```bash
python -m venv env
pip install -r ./requirements.txt
```

## Usage

```bash
./clean.sh
python ./siteScraper.py
```
Project contains two folders named "img" and "csv", after the scraping process is complete those folders will be filled with .jpg files and .csv files respectively.
