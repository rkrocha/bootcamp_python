
def float_range(start: float, stop: float, step: float = 1) -> list:
	lst = []
	while start < stop:
		lst.append(float(start))
		start += step
	return lst


class Vector:
	def __init__(self, attr):
		if isinstance(attr, list):
			self.values = attr
		elif isinstance(attr, int):
			self.values = float_range(0, attr)
		elif isinstance(attr, tuple) and len(attr) == 2:
			self.values = float_range(attr[0], attr[1])
		self.size = len(self.values)

	def __add__(self, other):
		if isinstance(other, Vector):
			assert self.size == other.size, "Can't add vectors of different sizes!"
			return Vector([float(i + j) for i, j in zip(self.values, other.values)])
		if isinstance(other, float) or isinstance(other, int):
			return Vector([float(i + other) for i in self.values])

	def __radd__(self, other):
		return self.__add__(other)

	def __sub__(self, other):
		if isinstance(other, Vector):
			if self.size != other.size:
				exit("Can't subtract vectors of different sizes!")
			return Vector([float(i - j) for i, j in zip(self.values, other.values)])
		if isinstance(other, float) or isinstance(other, int):
			return Vector([float(i - other) for i in self.values])

	def __rsub__(self, other):
		return self.__sub__(other)

	def __str__(self) -> str:
		return f"Vector({str(self.values)})"

	def __repr__(self) -> str:
		return str(self)
