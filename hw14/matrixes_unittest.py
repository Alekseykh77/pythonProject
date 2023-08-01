import unittest
from hw14.matrixes import Matrix


class TestMatrix(unittest.TestCase):

    def setUp(self) -> None:
        """Подготовка матриц для проведения операций"""
        self.matrix_1 = Matrix(matrix=[[4, 5, 10], [6, 8, 11], [7, 9, 3]])
        self.matrix_2 = Matrix(matrix=[[5, 3, 9], [8, 2, 6], [3, 9, 4]])
        self.matrix_5 = Matrix(matrix=[[2, 1, 3], [6, 2, 4], [1, 7, 5]])

    def test_add(self):
        matrix_3 = self.matrix_1 + self.matrix_2
        self.assertEqual(matrix_3.__repr__(),
                         "Matrix(matrix=[[9, 8, 19], [14, 10, 17], [10, 18, 7]])")

    def test_sub(self):
        matrix_4 = self.matrix_1 - self.matrix_2
        self.assertEqual(matrix_4.__repr__(),
                         "Matrix(matrix=[[-1, 2, 1], [-2, 6, 5], [4, 0, -1]])")

    def test_mult(self):
        self.assertEqual((self.matrix_1 * self.matrix_5).__repr__(),
                         "Matrix(matrix=[[48, 84, 82], [71, 99, 105], [71, 46, 72]])")

    def test_equal(self):
        self.assertTrue(self.matrix_1 == self.matrix_1)

    def test_not_equal(self):
        self.assertFalse(self.matrix_1 == self.matrix_2)


if __name__ == '__main__':
    test = TestMatrix()
    test.main(verbosing=True)
