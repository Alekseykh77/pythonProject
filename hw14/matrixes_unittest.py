import unittest
from hw14.matrixes import Matrix


class TestMatrix(unittest.TestCase):

    def setUp(self) -> None:
        """Подготовка матриц для проведения операций"""
        self.matrix_1 = Matrix(matrix=[[2, 3, 8], [4, 6, 9], [5, 7, 1]])
        self.matrix_2 = Matrix(matrix=[[4, 2, 8], [7, 1, 5], [2, 8, 3]])
        self.matrix_5 = Matrix(matrix=[[4, 2, 8], [7, 1, 5], [2, 8, 3]])

    def test_add(self):
        matrix_3 = self.matrix_1 + self.matrix_2
        self.assertEqual(matrix_3.__repr__(),
                         "Matrix(matrix=[[6, 5, 16], [11, 7, 14], [7, 15, 4]])")

    def test_sub(self):
        matrix_4 = self.matrix_1 - self.matrix_2
        self.assertEqual(matrix_4.__repr__(),
                         "Matrix(matrix=[[-2, 1, 0], [-3, 5, 4], [3, -1, -2]])")

    def test_mult(self):
        self.assertEqual((self.matrix_1 * self.matrix_5).__repr__(),
                         "Matrix(matrix=[[64, 40, 24], [72, 45, 27], [8, 5, 3]])")

    def test_equal(self):
        self.assertTrue(self.matrix_1 == self.matrix_1)

    def test_not_equal(self):
        self.assertFalse(self.matrix_1 == self.matrix_2)


if __name__ == '__main__':
    test = TestMatrix()
    test.main(verbosing=True)
