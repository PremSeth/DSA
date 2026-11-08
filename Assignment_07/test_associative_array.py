import unittest

from associative_array import AssociativeArray


class TestAssociativeArray(unittest.TestCase):
    def test_empty(self) -> None:
        array = AssociativeArray(3)
        self.assertEqual(len(array.buckets), 3)
        self.assertEqual(array.size(), 0)
        self.assertFalse(array.contains('missing'))
        self.assertIsNone(array.get('missing'))
        self.assertFalse(array.remove('missing'))

    def test_set_and_replace(self) -> None:
        array = AssociativeArray(3)
        array.set('cat', 1)
        array.set('cat', 2)
        array.set(5, 'five')
        self.assertTrue(array.contains('cat'))
        self.assertEqual(array.get('cat'), 2)
        self.assertEqual(array.get(5), 'five')
        self.assertEqual(array.size(), 2)

    def test_collision_and_remove(self) -> None:
        array = AssociativeArray(3)
        first, second = 1, 4  # Both go into the same bucket.
        array.set(first, 1)
        array.set(second, 2)
        self.assertEqual(array.get(first), 1)
        self.assertEqual(array.get(second), 2)
        self.assertTrue(array.remove(first))
        self.assertFalse(array.contains(first))
        self.assertEqual(array.get(second), 2)
        self.assertEqual(array.size(), 1)

    def test_key_value_pairs(self) -> None:
        array = AssociativeArray(3)
        array.set('a', 1)
        array.set('b', 2)
        self.assertEqual(set(array.keyValuePairs()), {('a', 1), ('b', 2)})

    def test_rehash(self) -> None:
        array = AssociativeArray(3)
        for i in range(30):
            array.set(i, i * 2)
        self.assertGreater(len(array.buckets), 3)
        self.assertEqual(array.size(), 30)
        for i in range(30):
            self.assertEqual(array.get(i), i * 2)


if __name__ == '__main__':
    unittest.main()
