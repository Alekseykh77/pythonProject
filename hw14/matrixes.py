class Matrix:
    """Класс матрица. Производит базовые действия сложение, вычитание, умножение матриц, сравнение."""

    def __init__(self, rows: int = 2, cols: int = 2, init_value: int = 0, *, matrix: list[list[int]] = None):
        """Инициализация матрицы по умолчанию 2 строки и 2 колонки

        :rows: Количество строк.
        :cols: Количество колонок.
        :init_value: Значение для инициализации матрицы.
        :matrix: Готовая матрица.
        """
        if matrix is None:
            self.__matrix = []
            for _ in range(rows):
                self.__matrix.append([init_value for _ in range(cols)])
        else:
            rows = len(matrix)
            cols = len(matrix[0])
            self.__matrix = matrix

        self.__cols = cols
        self.__rows = rows

    def __add__(self, other):
        """Сложение матриц. Матрицы должны иметь одну размерность."""
        if self.__rows != other.__rows or self.__cols != other.__cols:
            return None

        result = Matrix(self.__rows, self.__cols)
        for i in range(result.__rows):
            for j in range(result.__cols):
                result.__matrix[i][j] = self.__matrix[i][j] + other.__matrix[i][j]

        return result

    def __sub__(self, other):
        """Вычитание матриц. Матрицы должны иметь одну размерность."""
        if self.__rows != other.__rows or self.__cols != other.__cols:
            return None

        result = Matrix(self.__rows, self.__cols)
        for i in range(result.__rows):
            for j in range(result.__cols):
                result.__matrix[i][j] = self.__matrix[i][j] - other.__matrix[i][j]

        return result

    def __str__(self):
        """Вывод матрицы на печать."""
        result = []
        for row in self.__matrix:
            for val in row:
                result.append(f"{val:3} ")
            result.append("\n")
        return "".join(result)

    def __repr__(self):
        """Отображение матрицы."""
        return f"Matrix(matrix={self.__matrix})"

    def __eq__(self, other):
        """Сравнение матриц."""
        result = True
        if self.__rows != other.__rows or self.__cols != other.__cols:
            result = False
        else:
            for i in range(self.__rows):
                for j in range(self.__cols):
                    if self.__matrix[i][j] != other.__matrix[i][j]:
                        result = False
                        break
                if not result:
                    break

        return result

    def __mul__(self, other):
        """Умножение матриц."""
        # Две матрицы можно перемножить между собой тогда и только тогда, когда количество
        # столбцов первой матрицы равно количеству строк второй матрицы.
        if self.__cols != other.__rows:
            return None

        result = Matrix(self.__rows, other.__cols)
        for i in range(self.__rows):
            for j in range(other.__cols):
                for k in range(self.__cols):
                    result.__matrix[i][j] += self.__matrix[i][k] * other.__matrix[k][j]

        return result
