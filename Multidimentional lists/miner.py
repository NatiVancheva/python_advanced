n = int(input())
commands = input().split()
matrix = [input().split() for _ in range(n)]

start_row = start_col = 0
total_coal = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "s":
            start_row, start_col = i, j
        elif matrix[i][j] == "c":
            total_coal += 1

collected_coal = 0

for command in commands:
    next_row, next_col = start_row, start_col

    if command == "left":
        next_col -= 1
    elif command == "right":
        next_col += 1
    elif command == "up":
        next_row -= 1
    elif command == "down":
        next_row += 1

    if 0 <= next_row < n and 0 <= next_col < n:
        start_row, start_col = next_row, next_col
        cell = matrix[start_row][start_col]

        if cell == "c":
            collected_coal += 1
            matrix[start_row][start_col] = "*"
            if collected_coal == total_coal:
                print(f"You collected all coal! ({start_row}, {start_col})")
                break
        elif cell == "e":
            print(f"Game over! ({start_row}, {start_col})")
            break

else:
    remaining = total_coal - collected_coal
    print(f"{remaining} pieces of coal left. ({start_row}, {start_col})")