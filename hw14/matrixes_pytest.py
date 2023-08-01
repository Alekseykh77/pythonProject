import pytest
from hw14.matrixes import Matrix


@pytest.fixture()
def matrix_1():
    """Подготовка матриц для проведения операций"""
    return Matrix(matrix=[[4, 5, 10], [6, 8, 11], [7, 9, 3]])


@pytest.fixture()
def matrix_2():
    return Matrix(matrix=[[5, 3, 9], [8, 2, 6], [3, 9, 4]])


@pytest.fixture()
def matrix_5():
    return Matrix(matrix=[[2, 1, 3], [6, 2, 4], [1, 7, 5]])


def test_add(matrix_1, matrix_2):
    """Сложение матриц"""
    matrix_3 = matrix_1 + matrix_2
    assert matrix_3.__repr__() == "Matrix(matrix=[[9, 8, 19], [14, 10, 17], [10, 18, 7]])"


def test_sub(matrix_1, matrix_2):
    """Вычитание матриц"""
    matrix_4 = matrix_1 - matrix_2
    assert matrix_4.__repr__() == "Matrix(matrix=[[-1, 2, 1], [-2, 6, 5], [4, 0, -1]])"


def test_mult(matrix_1, matrix_5):
    assert (matrix_1 * matrix_5).__repr__() == "Matrix(matrix=[[48, 84, 82], [71, 99, 105], [71, 46, 72]])"


def test_equal(matrix_1):
    assert matrix_1 == matrix_1


def test_not_equal(matrix_1, matrix_2):
    assert not matrix_1 == matrix_2


if __name__ == '__main__':
    pytest.main(["-v"])
