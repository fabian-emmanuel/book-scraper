from bs4 import BeautifulSoup

from locators.books_page_locator import BooksPageLocators
from parsers.book_parser import BookParser


class BooksPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, "html.parser")

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(BooksPageLocators.BOOKS)]
