import unittest
import random
import quickSort

class TestQuickSort(unittest.TestCase):

	def test_sorting(self):
		#	testing for 10 elements
		array = [random.randint(0, 100) for i in range(10)]
		self.assertEqual(sorted(array), quickSort.quickSort(array, 0, len(array) - 1))

		#	testing for 25 elements
		array = [random.randint(0, 100) for i in range(25)]
		self.assertEqual(sorted(array), quickSort.quickSort(array, 0, len(array) - 1))

		#	testing for 50 elemnts
		array = [random.randint(0, 100) for i in range(50)]
		self.assertEqual(sorted(array), quickSort.quickSort(array, 0, len(array) - 1))

		#	testing for 100 elemnts
		array = [random.randint(0, 100) for i in range(100)]
		self.assertEqual(sorted(array), quickSort.quickSort(array, 0, len(array) - 1))

		#	testing for 10000 elemnts
		array = [random.randint(0, 100) for i in range(10000)]
		self.assertEqual(sorted(array), quickSort.quickSort(array, 0, len(array) - 1))

if __name__ == "__main__":
	unittest.main()