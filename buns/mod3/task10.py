size = int(input())

# Генерируем исходную матрицу
matrix = [[i for i in range(1, size + 1)] for _ in range(size)]

print("Исходная матрица:")
for row in matrix:
    print(row)
for i in range(size):
    for j in range(i+1, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print("\nТранспонированная матрица:")
for row in matrix:
    print(row)