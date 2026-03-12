n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs = input().split()

for bomb in bombs:
    r, c = map(int, bomb.split(","))
    bomb_value = matrix[r][c]

    if bomb_value <= 0:
        continue

    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if 0 <= i < n and 0 <= j < n:
                if matrix[i][j] > 0:
                    matrix[i][j] -= bomb_value
    matrix[r][c] = 0

alive_cells = [cell for row in matrix for cell in row if cell > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for row in matrix:
    print(*row)

