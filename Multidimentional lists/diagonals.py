rows = int(input())
matrix = []

for _ in range(rows):
    data = [int(el) for el in input().split(", ")]
    matrix.append(data)

primary_diagonal = []
primary_sum = 0
secondary_diagonal = []
secondary_sum = 0

for i in range(rows):
    primary_diagonal.append(matrix[i][i])
    primary_sum += matrix[i][i]
    secondary_diagonal.append(matrix[i][rows - 1 - i])
    secondary_sum += matrix[i][rows - 1 - i]
print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {secondary_sum}")
