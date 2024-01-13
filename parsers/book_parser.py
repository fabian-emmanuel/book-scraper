from locators.book_locator import BookLocator


class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'name -> {self.name} \nlink -> {self.link} \nprice -> {self.price} \nrating -> {self.rating} star(s) \n'

    @property
    def name(self):
        locator = BookLocator.NAME
        return self.parent.select_one(locator).attrs['title']

    @property
    def link(self):
        locator = BookLocator.LINK
        return self.parent.select_one(locator).attrs['href']

    @property
    def price(self):
        locator = BookLocator.PRICE
        return self.parent.select_one(locator).string

    @property
    def rating(self):
        locator = BookLocator.RATING
        classes = self.parent.select_one(locator).attrs['class']
        rating_class = [r for r in classes if r != 'star-rating'][0]
        return BookParser.RATINGS.get(rating_class)
