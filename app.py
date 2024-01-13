import requests

from pages.books_page import BooksPage

page_content = requests.get('https://books.toscrape.com/').content
page = BooksPage(page_content)

books = page.books

for book in books:
    print(book)
