import sys


def print_usage(message):
	if message:
		print(message)
	exit(
"""\
Usage:   python operations.py <number1> <number2>
Example: python operations.py 10 42\
""")


def get_quotient(num1, num2):
	if num2 == 0:
		return "ERROR: div by zero"
	else:
		return num1 / num2


def get_remainder(num1, num2):
	if num2 == 0:
		return "ERROR: module by zero"
	else:
		return num1 % num2


if len(sys.argv) != 3:
	print_usage("")
elif not str.isdigit(sys.argv[1]) or not str.isdigit(sys.argv[2]):
	print_usage("Input error: only numbers!")

num1, num2 = int(sys.argv[1]), int(sys.argv[2])

print(
f"""\
Sum:        {num1 + num2}
Difference: {num1 - num2}
Product:    {num1 * num2}
Quotient:   {get_quotient(num1, num2)}
Remainder:  {get_remainder(num1, num2)}\
""")
