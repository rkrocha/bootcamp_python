import sys

sys.argv.pop(0)
string = (" ".join([str for str in sys.argv]))
print(string.swapcase()[::-1])
