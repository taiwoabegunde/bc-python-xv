import unittest
from two_sums import twosum

class TwoSumTesTSuite(unittest.TestCase):

	def test_list_range_4(self):
		res = twosum([2,5,1,7], 8)
		self.assertEqual(res, [2,3])

	def test_list_range_5(self):
		res = twosum([2,5,1,7,6], 9)
		self.assertEqual(res, [0,3])

	def test_list_range_6(self):
		res = twosum([2,5,1,7,0,6], 8)
		self.assertEqual(res, [2,3])

	def test_list_range_7(self):
		res = twosum([2,5,1,7,0,6,9], 8)
		self.assertEqual(res, [2,3])

	def test_list_range_8(self):
		res = twosum([2,5,1,7,0,6,9,8], 8)
		self.assertEqual(res, [2,3])

	def test_list_range_9(self):
		res = twosum([2,5,1,7,0,6,9,8,3], 8)
		self.assertEqual(res, [2,3])

	def test_list_range_10(self):
		res = twosum([2,5,1,7,0,6,9,8,3,4], 8)
		self.assertEqual(res, [2,3])

	def test_list_range_11(self):
		res = twosum([2,5,1,7,0,6,9,8,3,4,4], 8)
		self.assertEqual(res, [2,3])

	def test_list_range_12(self):
		res = twosum([2,5,1,7,0,6,9,8,3,4,4,2], 8)
		self.assertEqual(res, [2,3])

	def test_list_range_13(self):
		res = twosum([2,5,1,7,0,6,9,8,3,4,4,2,9], 8)
		self.assertEqual(res, [2,3])

	def test_list_range_414(self):
		res = twosum([2,5,1,7,0,6,9,8,3,4,4,2,9], 8)
		self.assertEqual(res, [2,3])







if __name__ == '__main__':
	unittest.main()