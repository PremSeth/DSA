class Matrix:
    def __init__(self, size, data=None):
        self.size = size
        self.data = data if data is not None else [[0] * size for _ in range(size)]

    def get(self, row, column):
        return self.data[row][column]

    def set(self, row, column, value):
        self.data[row][column] = value

    def split(self):
        half = self.size // 2
        return (
            Matrix(half, [row[:half] for row in self.data[:half]]),
            Matrix(half, [row[half:] for row in self.data[:half]]),
            Matrix(half, [row[:half] for row in self.data[half:]]),
            Matrix(half, [row[half:] for row in self.data[half:]]),
        )

    def __add__(self, other):
        return Matrix(self.size, [
            [self.data[i][j] + other.data[i][j] for j in range(self.size)]
            for i in range(self.size)
        ])

    def __sub__(self, other):
        return Matrix(self.size, [
            [self.data[i][j] - other.data[i][j] for j in range(self.size)]
            for i in range(self.size)
        ])

    def multiply(self, other):
        """Conventional multiplication: O(n³)."""
        if not self.size == other.size:
            return None
        result = Matrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def strassenMultiply(self, other, cutoff=1):
        """Strassen multiplication; use conventional multiplication below cutoff."""
        if not self.size == other.size:
            return None
        size = 1
        while size < self.size:
            size *= 2
        a, b = Matrix(size), Matrix(size)
        for i in range(self.size):
            a.data[i][:self.size] = self.data[i]
            b.data[i][:self.size] = other.data[i]
        product = _strassen(a, b, cutoff)
        return Matrix(self.size, [row[:self.size] for row in product.data[:self.size]])


def _strassen(a, b, cutoff):
    if a.size <= cutoff:
        return a.multiply(b)

    a11, a12, a21, a22 = a.split()
    b11, b12, b21, b22 = b.split()
    m1 = _strassen(a11 + a22, b11 + b22, cutoff)
    m2 = _strassen(a21 + a22, b11, cutoff)
    m3 = _strassen(a11, b12 - b22, cutoff)
    m4 = _strassen(a22, b21 - b11, cutoff)
    m5 = _strassen(a11 + a12, b22, cutoff)
    m6 = _strassen(a21 - a11, b11 + b12, cutoff)
    m7 = _strassen(a12 - a22, b21 + b22, cutoff)

    c11 = m1 + m4 - m5 + m7
    c12 = m3 + m5
    c21 = m2 + m4
    c22 = m1 - m2 + m3 + m6
    half = c11.size
    return Matrix(half * 2, [
        c11.data[i] + c12.data[i] for i in range(half)
    ] + [
        c21.data[i] + c22.data[i] for i in range(half)
    ])
