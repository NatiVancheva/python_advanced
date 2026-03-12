rows, cols = [int(el) for el in input().split()]

matrix = []

for _ in range(rows):
    data = [int(el) for el in input().split()]
    matrix.append(data)

count = 0

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        below_element = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]

        if current_element == next_element == below_element == diagonal_element:
            count += 1

print(count)