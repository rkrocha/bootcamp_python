from book import Book
from recipe import Recipe

sandwich = Recipe('sandwich', 1, 2, ['bread', 'mayo', 'ham', 'cheese'], "It's a stack of deliciousness", 'snack')
ice_cream = Recipe('ice cream', 1, 0, ['cream', 'milk', 'sugar', 'vanilla'], "Frosty", 'dessert')

print(str(sandwich), "\n")

book = Book("My cookbook")

book.add_recipe(sandwich)
book.add_recipe(ice_cream)

print(str(book), "\n")

print(book.get_recipe_by_types('snack'))
print(book.get_recipe_by_types('dessert'), "\n")

book.get_recipe_by_name('ice cream')
