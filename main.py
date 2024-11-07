from Book import Book

book1 = Book()
book2 = Book()
book3 = Book()
book4 = Book()
book5 = Book()
book6 = Book()

# Obejktas sukurtas naudojantis pilnu konstruktoriumi
book1 = Book('Neissimiegojas darbuotojas', 120, 2014)
book2 = Book('Augalu kerstas', 250, 2022)
book3 = Book('PC builder', 400, 2004)
# print(book1)
# print(book2)
# print(book3)

# Objektas sukurtas naudojant tuscia konstruktoriu
book4.Title = "Kosmonautas"
book4.Pages = 120
book4.Release_year = 2009
# print(book4)
book5.Title = "Paskutinis medis"
book5.Pages = 50
book5.Release_year = 2023
# print(book4)
book6.Title = 'Kancia'
book6.Pages = 1000
book6.Release_year = 2005

list = [ book1, book2, book3, book4, book5, book6]

for x in list:
    print(x)

