# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 8, 7],
          [6, 12, 10, 5]]

print("исходная матрица:\n", matrix)


def matrix_transposition_1(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in
                    range(len(matrix[0]))]  # структура транспонированной матрицы
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    print(trans_matrix)


print("транспонированная матрица:")
matrix_transposition_1(matrix)
