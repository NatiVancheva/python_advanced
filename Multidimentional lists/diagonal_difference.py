rows = int(input())
matrix = []

for _ in range(rows):
    data = [int(el) for el in input().split()]
    matrix.append(data)

primary_sum = 0
secondary_sum = 0

for i in range(rows):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][rows - 1 - i]
    difference = abs(primary_sum - secondary_sum)
print(difference)