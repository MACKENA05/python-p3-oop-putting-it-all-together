#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.page_count = page_count
        self.title = title

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, count):
        if isinstance(count, int):
            self._page_count = count
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    
book = Book("And Then There Were None", 272)

print(book.title)
print(book.turn_page())