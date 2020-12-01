import csv
import requests
from bs4 import BeautifulSoup


books = []
headers = ["product_page_url", "universal_product_code", "title",
           "price_including_tax", "price_exluding_tax", "number_available",
           "product_description", "category", "review_rating", "image_url"]
baseUrl = 'http://books.toscrape.com/'
catUrl = 'catalogue/category/books/science-fiction_16/'

category = requests.get(baseUrl + catUrl)
if category.ok:
    categorySoup = BeautifulSoup(category.text, 'html.parser')
    articles = categorySoup.findAll('article')
    for article in articles:
        a = article.find('a')
        href = a['href']
        bookPage = requests.get(baseUrl + catUrl + href)
        if bookPage.ok:
            bookSoup = BeautifulSoup(bookPage.text, 'html.parser')
            book = dict.fromkeys(["product_page_url", "universal_product_code", "title",
            "price_including_tax", "price_exluding_tax", "number_available",
            "product_description", "category", "review_rating", "image_url"])
            book["product_page_url"] = (baseUrl + catUrl + href)
            book["title"] = bookSoup.find('h1').text
            book["product_description"] = bookSoup.find('meta', attrs={'name': 'description'})["content"]
            book["category"] = bookSoup.find('ul', attrs={'class': 'breadcrumb'}).findAll('li')[2].text.strip()
            book["image_url"] = baseUrl + bookSoup.find('div', attrs={'class': 'item active'}).find('img')["src"].replace("../", "")
            books.append(book)
            infos = bookSoup.findAll('td')
            print(infos)

def write_csv_from_dicts(data, header, filename):
    with open(filename, "w") as csv_file:
        dict_writer = csv.DictWriter(csv_file, fieldnames=header)
        dict_writer.writeheader()
        for row in data:
            dict_writer.writerow(row)

write_csv_from_dicts(books, headers, "result.csv")
