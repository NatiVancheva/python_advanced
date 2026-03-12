from collections import deque
rows, cols = [int(el) for el in input().split()]
text = deque(input())

matrix = []

for row in range(rows):
    matrix.append([""] * cols)
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = text[0] #мести отляво надясно
        else:
            matrix[row][-1-col] = text[0] # мести отдясно наляво
        text.rotate(-1)

for row in matrix:
    print(*row, sep="")