from Plant import Plant
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

# for x in list:
#     print(x)

plant1 = Plant( 'Rose', 'Rosa', True, 'Australia', 1.2, False)
plant2 = Plant( 'Tomato', 'Solanum lycopersicum', True, 'South America', 1.5, True)
plant3 = Plant( 'Potato', 'Solanum tuberosum', True, 'South America', 0.6, True)
plant4 = Plant()
plant4.Name = 'Spruce'
plant4.Latin_name = 'Picea'
plant4.Is_annual = False
plant4.Continent = 'Asia, Europe'
plant4.Height = 60
plant4.Eatable = False

plants = [ plant1, plant2, plant3, plant4]

for i in plants:
    print(i)
