n = int(input())
matrix = []
health = 100
stars = 0
pacman_r = 0
pacman_c = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "P":
            pacman_r = row
            pacman_c = col
            matrix[row][col] = "-"
        elif matrix[row][col] == "*":
            stars += 1

has_freeze = False

while True:
    command = input()
    if command == "end":
        break

    row, col = directions[command]
    new_row = (pacman_r + row) % n
    new_col = (pacman_c + col) % n

    stars_cell = matrix[new_row][new_col]

    if stars_cell == "*":
        stars -= 1
        matrix[new_row][new_col] = "-"
        pacman_r, pacman_c = new_row, new_col
        if stars == 0:
            break

    elif stars_cell == "G":
        if has_freeze:
            has_freeze = False
        else:
            health -= 50
        matrix[new_row][new_col] = "-"
        pacman_r, pacman_c = new_row, new_col
        if health <= 0:
            break

    elif stars_cell == "F":
        has_freeze = True
        matrix[new_row][new_col] = "-"
        pacman_r, pacman_c = new_row, new_col

    else:
        pacman_r, pacman_c = new_row, new_col

matrix[pacman_r][pacman_c] = "P"

if health <= 0:
    print(f"Game over! Pacman last coordinates [{pacman_r},{pacman_c}]")
elif stars == 0:
    print("Pacman wins! All the stars are collected.")
else:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")

if stars > 0:
    print(f"Uncollected stars: {stars}")

for row in matrix:
    print("".join(row))