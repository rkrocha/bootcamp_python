import json

global cookbook


def add_recipe():
	recipe_name = input("What is the recipe called?\n")
	recipe = dict({ "steak" : {
	"ingredients" : ["steak", "salt", "pepper"],
	"meal" : "lunch",
	"prep_time" : 15
	}})
	cookbook.update(recipe)


def delete_recipe():
	recipe = input("\nWhat recipe would you like to delete?\n")
	if cookbook.get(recipe):
		cookbook.pop(recipe)
	else:
		print("Recipe not found!\n")


def print_recipe():
	name = input("\nEnter the recipe's name to get its details:\n")
	recipe = cookbook.get(name)
	if recipe:
		print(f'''
Recipe for {name}:
Ingredients: {recipe["ingredients"]}
To be eaten for {recipe["meal"]}.
Takes {recipe["prep_time"]} minutes of prep.
''')
	else:
		print("Recipe not found!\n")


def print_cookbook():
	print(json.dumps(cookbook, sort_keys=True, indent=4))


def save_cookbook():
	name = input("\nType a name for this new cookbook:\n") + ".json"
	file = open(name, 'w')
	file.write(json.dumps(cookbook, sort_keys=True, indent=4))
	file.close()


def wait_input():
	cmd = input("""
Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Save cookbook to file
6: Quit
""")
	if cmd == "1":
		add_recipe()
	elif cmd == "2":
		delete_recipe()
	elif cmd == "3":
		print_recipe()
	elif cmd == "4":
		print_cookbook()
	elif cmd == "5":
		save_cookbook()
	elif cmd == "6":
		quit("\nGoodbye :)")


name = input("Specify the name of a cookbook to open:\n")
if name:
	try:
		file = open(name + ".json", 'r')
	except FileNotFoundError:
		file = ""
if not name or not file:
	print("No cookbook selected. Starting a new one.")
	cookbook = dict()
else:
	cookbook = json.load(file)
	file.close()

while True:
	wait_input()
