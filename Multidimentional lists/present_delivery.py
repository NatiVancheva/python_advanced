count_of_presents = int(input())
neighborhood = int(input())
matrix = []
santa = []
nice_kids = 0
nice_kids_gifted = 0

for row in range(neighborhood):
    matrix.append(input().split())
    for col in range(neighborhood):
        if matrix[row][col] == "S":
            santa = [row, col]
        elif matrix[row][col] == "V":
            nice_kids += 1

directions = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while count_of_presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    r, c = santa[0] + directions[command[0]], santa[1] + directions[command[1]]
    if 0 <= r < neighborhood and 0 <= c < neighborhood:
        if matrix[r][c] == "V":
            count_of_presents -= 1
            nice_kids_gifted += 1
            matrix[r][c] = "-"
        elif matrix[r][c] == "C":
            for d in directions.values():
                next_row, next_col = r + d[0], c + d[1]
                if matrix[next_row][next_col] in "VX" and count_of_presents > 0:
                    if matrix[next_row][next_col] == "V":
                        nice_kids_gifted += 1
                    count_of_presents -= 1
                    matrix[next_row][next_col] = "-"

        matrix[santa[0]][santa[1]] = "-"
        santa = [r, c]
        matrix[r][c] = "S"

if count_of_presents < 1 and nice_kids_gifted < nice_kids:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row)

if nice_kids - nice_kids_gifted > 0:
    print(f"No presents for {nice_kids - nice_kids_gifted} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_gifted} happy nice kid/s.")


# presents = int(input())
# n = int(input())
#
# neighborhood = []
# santa_pos = []
# nice_kids = 0
# gifted_nice_kids = 0
#
# # Read the matrix
# for row in range(n):
#     line = input().split()
#     neighborhood.append(line)
#     for col in range(n):
#         if line[col] == "S":
#             santa_pos = [row, col]
#         elif line[col] == "V":
#             nice_kids += 1
#
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1)
# }
#
# while presents > 0:
#     command = input()
#     if command == "Christmas morning":
#         break
#
#     dr, dc = directions[command]
#     r, c = santa_pos[0] + dr, santa_pos[1] + dc
#
#     if not (0 <= r < n and 0 <= c < n):
#         continue
#
#     # Move Santa
#     neighborhood[santa_pos[0]][santa_pos[1]] = "-"
#
#     if neighborhood[r][c] == "V":
#         presents -= 1
#         gifted_nice_kids += 1
#
#     elif neighborhood[r][c] == "C":
#         for d in directions.values():
#             nr, nc = r + d[0], c + d[1]
#             if 0 <= nr < n and 0 <= nc < n:
#                 if neighborhood[nr][nc] in ("V", "X") and presents > 0:
#                     if neighborhood[nr][nc] == "V":
#                         gifted_nice_kids += 1
#                     presents -= 1
#                     neighborhood[nr][nc] = "-"
#
#     santa_pos = [r, c]
#     neighborhood[r][c] = "S"
#
# # Output messages
# if presents == 0 and gifted_nice_kids < nice_kids:
#     print("Santa ran out of presents!")
#
# for row in neighborhood:
#     print(" ".join(row))
#
# if gifted_nice_kids == nice_kids:
#     print(f"Good job, Santa! {gifted_nice_kids} happy nice kid/s.")
# else:
#     print(f"No presents for {nice_kids - gifted_nice_kids} nice kid/s.")
#
