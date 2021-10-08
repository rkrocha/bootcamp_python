
class Recipe:
	def __init__(self, name: str,
						cooking_lvl: int,
						cooking_time: int,
						ingredients: list,
						description: str,
						recipe_type: str) -> None:
		self.name = name if name else exit ("A recipe name must be provided as a string")
		self.cooking_level = cooking_lvl if cooking_lvl in range(1, 6) else exit("Cooking level must be in range 1 to 5")
		self.cooking_time = cooking_time if cooking_time >= 0 else exit("Cooking time must not be negative")
		self.ingredients = ingredients if len(ingredients) > 0 else exit("The recipe's ingredients must be provided as a list")
		self.description = description
		self.recipe_type = recipe_type.lower() if recipe_type.lower() in ["snack", "meal", "dessert"] else exit("Recipe type must be 'snack', 'meal' or 'dessert'")

	def __str__(self):
		"Returns a string containing recipe info."
		return f"""Recipe: {self.name}
Cooking level: {self.cooking_level}
Cooking time: {self.cooking_time}
Ingredients: {str(self.ingredients)}
Description: {self.description}
Recipe type: {self.recipe_type}"""
