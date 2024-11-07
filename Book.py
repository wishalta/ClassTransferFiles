
class Book():
    def __init__(self, title="", pages=0, release_year=0):
        self.Title = title = "Mafija"
        self.Pages = pages = 234
        self.Release_year = release_year = 2015
    def __str__(self):
        return f'Title: {self.Title} | Pages:{self.Pages} | Release_year:{self.Release_year}'
