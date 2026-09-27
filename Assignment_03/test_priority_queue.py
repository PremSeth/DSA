import unittest
from priority_queue import minPQ


class TestMinPQ(unittest.TestCase):
    def test_empty_queue(self):
        queue = minPQ()
        self.assertTrue(queue.is_empty())
        self.assertIsNone(queue.next())

    def test_lowest_priority_first(self):
        queue = minPQ()
        queue.priority_add('slow', 9)
        queue.priority_add('fast', 2)
        self.assertEqual(queue.next(), (2, 'fast'))
        self.assertEqual(queue.next(), (9, 'slow'))

    def test_adjust_priority(self):
        queue = minPQ()
        queue.priority_add('A', 5)
        queue.priority_add('B', 8)
        queue.adjust_priority('B', 1)
        self.assertEqual(queue.next(), (1, 'B'))


if __name__ == '__main__':
    unittest.main()
