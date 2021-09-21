import json

"""
cookbook will store 3 recipes:
• sandwich
• cake
• salad

Each recipe will store 3 values:
• ingredients: a list of ingredients
• meal: type of meal
• prep_time: preparation time in minutes

Sandwich’s ingredients are ham, bread, cheese and tomatoes. It is a lunch and it takes 10 minutes of preparation.

Cake’s ingredients are flour, sugar and eggs. It is a dessert and it takes 60 minutes of preparation.

Salad’s ingredients are avocado, arugula, tomatoes and spinach. It is a lunch and it takes 15 minutes of preparation.
"""

cookbook = {
	"sandwich" : {
	"ingredients" : ["ham", "bread", "cheese", "tomatoes"],
	"meal" : "lunch",
	"prep_time" : 10
	},
	"cake" : {
	"ingredients" : ["flour", "sugar", "eggs"],
	"meal" : "dessert",
	"prep_time" : 60
	},
	"salad" : {
	"ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
	"meal" : "lunch",
	"prep_time" : 15
	}
}

def print_cookbook():
	print(json.dumps(cookbook, sort_keys=True, indent=4))

def print_recipe(name):
	recipe = cookbook.get(name)
	print(f'''\
Recipe for {name}:
Ingredients: {recipe["ingredients"]}
To be eaten for {recipe["meal"]}.
Takes {recipe["prep_time"]} minutes of prep.
''')

print_recipe("cake")
print_recipe("sandwich")
print_recipe("salad")
