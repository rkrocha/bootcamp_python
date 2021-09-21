def text_analyzer(*text):
	"This function counts the number of uppercase characters, lowercase characters, punctuation marks and spaces in a given text."
	if len(text) > 1:
		exit("ERROR")
	if text:
		text = str(text[0])
	while not text:
		text = input("What is the text to analyze?\n")
	print(
f"""\
The text contains {len(text)} characters:
- {len([c for c in text if c.isupper()])} uppercase characters
- {len([c for c in text if c.islower()])} lowercase characters
- {len([c for c in text if c in '.,;:!?'])} punctuation marks
- {len([c for c in text if c.isspace()])} spaces\
""")

text_analyzer("Ayy")
