
class GotCharacter:
	"A class representing a character from Game of Thrones."
	def __init__(self, first_name: str, is_alive: bool = True):
		self.first_name = first_name
		self.is_alive = is_alive

class Lannister(GotCharacter):
	"A class representing House Lannister. Or fool's gold."
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.house_name = "Lannister"
		self.house_words = "Hear Me Roar!"

	def print_house_words(self):
		"Prints the House words."
		print(self.house_words)

	def die(self):
		self.is_alive = False
