from Book import Book

book1 = Book()
book2 = Book()
book3 = Book()

# Obejktas sukurtas naudojantis pilnu konstruktoriumi
book2 = Book('Augalu kerstas', 250, 2022)
book3 = Book('PC builder', 400, 2004)
print(book2)
print(book3)

# Objektas sukurtas naudojant tuscia konstruktoriu
book1.Title = "Kosmonautas"
book1.Pages = 120
book1.Release_year = 2009
print(book1)