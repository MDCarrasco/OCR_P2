import csv
import requests
from bs4 import BeautifulSoup

headers = ["product_page_url", "universal_product_code", "title",
           "price_including_tax", "price_excluding_tax", "number_available",
           "product_description", "category", "review_rating", "image_url"]
baseUrl = 'http://books.toscrape.com/'
catalogueUrl = 'catalogue/'
categoryUrl = 'category/books/science-fiction_16/'

def one():
    return "1/5"
def two():
    return "2/5"
def three():
    return "3/5"
def four():
    return "4/5"
def five():
    return "5/5"

switcher = {
    "One": one,
    "Two": two,
    "Three": three,
    "Four": four,
    "Five": five
}

def rating_switch(rating):
    func = switcher.get(rating, "Not rated")
    return func()

def construct_book(baseUrl, url):
    book = dict.fromkeys(["product_page_url", "universal_product_code", "title",
    "price_including_tax", "price_excluding_tax", "number_available",
    "product_description", "category", "review_rating", "image_url"])
    book["product_page_url"] = url
    bookSoup = BeautifulSoup(bookPage.text, 'html.parser')
    book["title"] = bookSoup.find('h1').text
    book["product_description"] = bookSoup.find('meta', attrs={'name': 'description'})["content"].strip()
    book["category"] = bookSoup.find('ul', attrs={'class': 'breadcrumb'}).findAll('li')[2].text.strip()
    book["image_url"] = baseUrl + bookSoup.find('div', attrs={'class': 'item active'}).find('img')["src"].replace("../", "")
    rating = bookSoup.find('p', attrs={'class': 'star-rating'}).attrs.get('class', [])[1].strip()
    book["review_rating"] = rating_switch(rating)
    bookInfos = bookSoup.findAll('td')
    book["universal_product_code"] = bookInfos[0].getText()
    book["price_including_tax"] = bookInfos[2].getText()[1:]
    book["price_excluding_tax"] = bookInfos[3].getText()[1:]
    book["number_available"] = bookInfos[5].getText()[bookInfos[5].getText().find("(")+1:bookInfos[5].getText().find(")")-9]
    return book

def write_csv_from_dicts(data, header, filename):
    with open(filename, "w") as csv_file:
        dict_writer = csv.DictWriter(csv_file, fieldnames=header)
        dict_writer.writeheader()
        for row in data:
            dict_writer.writerow(row)

books = []
category = requests.get(baseUrl + catalogueUrl + categoryUrl)
if category.ok:
    categorySoup = BeautifulSoup(category.text, 'html.parser')
    articles = categorySoup.findAll('article')
    for article in articles:
        a = article.find('a')
        href = a['href'].replace("../", "")
        bookPage = requests.get(baseUrl + catalogueUrl + href)
        if bookPage.ok:
            books.append(construct_book(baseUrl, baseUrl + catalogueUrl + href))
write_csv_from_dicts(books, headers, "result.csv")
