import unittest

from strassen_matrix import Matrix


class TestMatrix(unittest.TestCase):
    def test_values_and_quadrants(self):
        matrix = Matrix(2)
        matrix.set(0, 1, 7)
        self.assertEqual(matrix.get(0, 1), 7)
        self.assertEqual([part.data for part in matrix.split()],
                         [[[0]], [[7]], [[0]], [[0]]])

    def test_multiplication(self):
        for size in (1, 2, 3, 4, 5):
            left = Matrix(size, [[i + j + 1 for j in range(size)] for i in range(size)])
            right = Matrix(size, [[i - j for j in range(size)] for i in range(size)])
            self.assertEqual(left.strassenMultiply(right).data, left.multiply(right).data)

    def test_incompatible_sizes(self):
        self.assertIsNone(Matrix(2).multiply(Matrix(3)))
        self.assertIsNone(Matrix(2).strassenMultiply(Matrix(3)))


if __name__ == '__main__':
    unittest.main()
