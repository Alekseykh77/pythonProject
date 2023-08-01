import pytest
from hw14.matrixes import Matrix


@pytest.fixture()
def matrix_1():
    """Подготовка матриц для проведения операций"""
    return Matrix(matrix=[[2, 3, 8], [4, 6, 9], [5, 7, 1]])


@pytest.fixture()
def matrix_2():
    return Matrix(matrix=[[4, 2, 8], [7, 1, 5], [2, 8, 3]])


@pytest.fixture()
def matrix_5():
    return Matrix(matrix=[[4, 2, 8], [7, 1, 5], [2, 8, 3]])


def test_add(matrix_1, matrix_2):
    """Сложение матриц"""
    matrix_3 = matrix_1 + matrix_2
    assert matrix_3.__repr__() == "Matrix(matrix=[[6, 5, 16], [11, 7, 14], [7, 15, 4]])"


def test_sub(matrix_1, matrix_2):
    """Вычитание матриц"""
    matrix_4 = matrix_1 - matrix_2
    assert matrix_4.__repr__() == "Matrix(matrix=[[-2, 1, 0], [-3, 5, 4], [3, -1, -2]])"


def test_mult(matrix_1, matrix_5):
    assert (matrix_1 * matrix_5).__repr__() == "Matrix(matrix=[[64, 40, 24], [72, 45, 27], [8, 5, 3]])"


def test_equal(matrix_1):
    assert matrix_1 == matrix_1


def test_not_equal(matrix_1, matrix_2):
    assert not matrix_1 == matrix_2


if __name__ == '__main__':
    pytest.main(["-v"])
