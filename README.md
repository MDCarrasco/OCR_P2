# OCR_P2

OpenClassrooms' Python Project 2 is a small web scraper with multithreading that goes site->categories->books into a CSV file.

For a full scrap of http://books.toscrape.com multithreading makes it 7x faster ! (14 min before vs 2 min with multithreading).

## Installation

```bash
python -m venv env
source ./env/bin/activate
pip install -r ./requirements.txt
```

## Usage

```bash
./clean.sh
python ./siteScraper.py
```
Project contains two folders named "img" and "csv", after the scraping process is complete those folders will be filled with .jpg files and .csv files respectively.

## How it works

If books.toscrape.com is accessible, the script starts by getting all the categories listed in the left side div as shown in the following screenshot:
> <img width="956" alt="HomeCategories" src="https://user-images.githubusercontent.com/50454011/101605744-da323080-3a02-11eb-9576-e61b5487dda4.png">

Now we got a list with all the categories. 
We made sure of popping out the unwanted first link aka "Books" as we want to be able to create a CSV file per category so we have to navigate through each and every one of those individually (that is where the multithreading happens by the way).

Category scraping starts by checking if the category has multiple pages or not and then calling a dictionnary filler on every book url in the category's page or pages. 
Below, an example of a book page url inside a category's page:
> <img width="956" alt="CategoryBookLink" src="https://user-images.githubusercontent.com/50454011/101606412-a86d9980-3a03-11eb-8c99-a3e63c4b5c47.png">

The dictionnary filler then proceeds to do the scraping of every data we need to be seeing in the csv file from every book page one by one. Again, example below:
> <img width="956" alt="BookPage" src="https://user-images.githubusercontent.com/50454011/101608958-ac4eeb00-3a06-11eb-81e6-e76bd911ce66.png">

- Caption/CSV headers
0. Product_page_url
1. Title
2. Product_description
3. Category
4. Image_url
5. Review_rating
6. Universal_product_code
7. Price_excluding_tax
8. Price_including_tax
9. Number_available

Each time a book page is scrapped, a copy of the corresponding .jpg file is downloaded into the "img" folder. Then, the script writes row by row (that is book by book) into the category's csv file named after it into the "csv" folder.

### File naming procedure

- jpg files
The script keeps only alphanumeric characters from the "title" value of a book and uses that string to set the filename.
- csv files
The script uses the category name (spaces included) to set the filename.

### Multithreading

The script uses the package `concurrent.futures` to create an object of type `ThreadPoolExecutor` with the worker amount set to 30 or to the number of categories to be scraped if lower. Each worker thread then executes the scraping for a category, any idle worker takes on another category until there is none left.
More on it here : https://docs.python.org/3/library/concurrent.futures.html and there : https://wiki.python.org/moin/GlobalInterpreterLock
