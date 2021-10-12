from game import GotCharacter, Lannister

jaime = Lannister("Jaime")
print(jaime.__dict__)
jaime.print_house_words()
print(jaime.is_alive)
jaime.die()
print(jaime.is_alive)
print(jaime.__doc__)
