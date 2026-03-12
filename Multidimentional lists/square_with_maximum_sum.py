rows, cols = [int(el) for el in input().split(", ")]
matrix = []

for _ in range(rows):
    data = [int(el) for el in input().split()]
    matrix.append(data)

max_sum = float("-inf")
sub_matrix = []

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        below_element = matrix[row_index + 1][col_index]
        diag_element = matrix[row_index + 1][col_index + 1]
        sum_elements =  current + next_element + below_element + diag_element

        if sum_elements > max_sum:
            max_sum = sum_elements
            sub_matrix = [[current, next_element], [below_element][diag_element]]

print(*sub_matrix[0])
print(sub_matrix[1])
print(max_sum)
