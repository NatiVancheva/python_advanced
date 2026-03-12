n, m = [int(x) for x in input().split()]
matrix = []

p_row, p_col = 0, 0
bunnies = set()

for row in range(n):
    matrix.append(list(input()))
    for col in range(m):
        if matrix[row][col] == "P":
            p_row, p_col = row, col
        elif matrix[row][col] == "B":
            bunnies.add((row, col))

commands = list(input())

movements = {
    "L": lambda r, c: (r, c - 1),
    "R": lambda r, c: (r, c + 1),
    "U": lambda r, c: (r - 1, c),
    "D": lambda r, c: (r + 1, c)
}

def spread_bunnies(mat, bunnies_set):
    new_bunnies = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for b_row, b_col in bunnies_set:
        for d_row, d_col in directions:
            new_row, new_col = b_row + d_row, b_col + d_col
            if 0 <= new_row < len(mat) and 0 <= new_col < len(mat[0]):
                mat[new_row][new_col] = "B"
                new_bunnies.add((new_row, new_col))

    return mat, bunnies_set.union(new_bunnies)

has_won = False
is_dead = False
for command in commands:
    new_p_row, new_p_col = movements[command](p_row, p_col)
    matrix, bunnies = spread_bunnies(matrix, bunnies)

    if (p_row, p_col) not in bunnies:
        matrix[p_row][p_col] = "."

    if new_p_row < 0 or new_p_col >= n or new_p_col < 0 or new_p_col >= m:
        has_won = True
        break

    p_row, p_col = new_p_row, new_p_col
    if matrix[p_row][p_col] == "B":
        is_dead = True
        break

for row in matrix:
    print("".join(row))

if has_won:
    print(f"won: {p_row} {p_col}")
elif is_dead:
    print(f"dead: {p_row} {p_col}")