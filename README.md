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

## How it works

<img width="956" alt="HomeCategories" src="https://user-images.githubusercontent.com/50454011/101605744-da323080-3a02-11eb-9576-e61b5487dda4.png">

<img width="956" alt="CategoryBookLink" src="https://user-images.githubusercontent.com/50454011/101606412-a86d9980-3a03-11eb-8c99-a3e63c4b5c47.png">

<img width="956" alt="BookPage" src="https://user-images.githubusercontent.com/50454011/101608958-ac4eeb00-3a06-11eb-81e6-e76bd911ce66.png">
