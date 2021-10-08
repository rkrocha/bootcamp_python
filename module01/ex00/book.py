import datetime
from recipe import Recipe

class Book:
	def __init__(self, name: str):
		self.name = name if name else exit ("A book name must be provided as a string")
		self.creation_date = datetime.datetime.now()
		self.last_update = self.creation_date
		self.recipes_list = dict({'snack' : [], 'meal' : [], 'dessert' : []})

	def __str__(self):
		"Returns a string containing book info"
		return f"""Book: {self.name}
Creation date: {self.creation_date}
Last updated: {self.last_update}
Recipes contained:
	Snacks: {self.get_recipe_by_types('snack')}
	Meals: {self.get_recipe_by_types('meal')}
	Desserts: {self.get_recipe_by_types('dessert')}"""

	def get_recipe_by_name(self, name):
		"Print a recipe called 'name' and returns its instance"
		lst = self.recipes_list.values()
		for sub_lst in lst:
			for obj in sub_lst:
				if obj.name.lower() == name.lower():
					print(str(obj))
					return obj

	def get_recipe_by_types(self, recipe_type):
		"Get all recipe names for a given recipe_type"
		obj_lst = self.recipes_list.get(recipe_type.lower(), '')
		if not type(obj_lst):
			exit("Invalid recipe type")
		str_lst = []
		for obj in obj_lst:
			str_lst.append(obj.name)
		return str_lst

	def add_recipe(self, recipe):
		"Add a recipe to the book and update last_update"
		if not isinstance(recipe, Recipe):
			exit("Recipe must be an object of type Recipe")
		lst = self.recipes_list.get(recipe.recipe_type)
		lst.append(recipe)
		self.recipes_list.update({recipe.recipe_type : lst})
		self.last_update = datetime.datetime.now()
