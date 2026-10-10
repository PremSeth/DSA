import unittest

from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_empty_and_single_item(self):
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([7]), [7])

    def test_duplicates_and_negative_numbers(self):
        values = [4, -2, 4, 0, -9, 3, -2]
        self.assertEqual(insertion_sort(values), [-9, -2, -2, 0, 3, 4, 4])

    def test_reverse_order_and_original_input(self):
        values = list(range(100, -1, -1))
        self.assertEqual(insertion_sort(values), list(range(101)))
        self.assertEqual(values, list(range(100, -1, -1)))


if __name__ == '__main__':
    unittest.main()
