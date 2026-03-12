n = int(input())

matrix = []

for i in range(n):
    data = [int(el) for el in input().split()]
    matrix.append(data)

diag_sum = 0
for row_index in range(n):
    for col_index in range(n):
        if row_index == col_index:
            diag_sum += matrix[row_index][col_index]

print(diag_sum)

for index in range(n):
    diag_sum += matrix[index][index]

for i in range(n):
    second_diag = matrix[i][n - 1 - i]
    