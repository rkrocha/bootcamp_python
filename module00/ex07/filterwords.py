import re
import sys

list = []

if len(sys.argv) != 3 or str.isdigit(sys.argv[1]) or not str.isdigit(sys.argv[2]):
	exit("ERROR")
for word in str.split(sys.argv[1]):
	word = re.sub(r'[^\w\s]', '', word)
	if len(word) > int(sys.argv[2]):
		list.append(word)
print(list)
