import sys

if len(sys.argv) != 2 or not str.isdigit(sys.argv[1]):
	exit("ERROR")

num = int(sys.argv[1])

if num == 0:
	print("I'm zero.")
elif num % 2 == 0:
	print("I'm even.")
else:
	print("I'm odd.")
