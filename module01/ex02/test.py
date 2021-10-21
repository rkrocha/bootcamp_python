from unittest import TestCase
from vector import Vector


class VectorUnitTest(TestCase):
	def test_values_init_with_attr_list(self):
		expected = [2.0, 3.0, 4.0]
		result = Vector([2.0, 3.0, 4.0]).values
		self.assertEqual(expected, result)

	def test_size_init_with_attr_list(self):
		expected = 3
		result = Vector([2.0, 3.0, 4.0]).size
		self.assertEqual(expected, result)

	def test_values_init_with_attr_int(self):
		expected = [0.0, 1.0, 2.0]
		result = Vector(3).values
		self.assertEqual(expected, result)

	def test_size_init_with_attr_int(self):
		expected = 3
		result = Vector(3).size
		self.assertEqual(expected, result)

	def test_values_init_with_attr_tuple(self):
		expected = [2.0, 3.0, 4.0]
		result = Vector((2, 5)).values
		self.assertEqual(expected, result)

	def test_size_init_with_attr_tuple(self):
		expected = 3
		result = Vector((2, 5)).size
		self.assertEqual(expected, result)

	def test_add_float(self):
		expected = Vector([2, 3, 4]).values
		result = (Vector([0, 1, 2]) + 2).values
		self.assertEqual(expected, result)

	def test_radd_float(self):
		expected = Vector([2, 3, 4]).values
		result = (2 + Vector([0, 1, 2])).values
		self.assertEqual(expected, result)

	def test_add_vector(self):
		expected = Vector([1, 2, 3]).values
		result = (Vector([0, 1, 2]) + Vector([1, 1, 1])).values
		self.assertEqual(expected, result)

	def test_sub_float(self):
		expected = Vector([-1, 0, 1]).values
		result = (Vector([0, 1, 2]) - 1).values
		self.assertEqual(expected, result)

	def test_rsub_float(self):
		expected = Vector([-1, 0, 1]).values
		result = (1 - Vector([0, 1, 2])).values
		self.assertEqual(expected, result)

	def test_sub_vector(self):
		expected = Vector([-1, 0, 1]).values
		result = (Vector([0, 1, 2]) - Vector([1, 1, 1])).values
		self.assertEqual(expected, result)

	def test_str(self):
		expected = "Vector([-1, 0, 1])"
		result = str(Vector([-1, 0, 1]))
		self.assertEqual(expected, result)

	def test_repr(self):
		expected = "Vector([-1, 0, 1])"
		result = repr(Vector([-1, 0, 1]))
		self.assertEqual(expected, result)

# py -m unittest discover . test.py -v
