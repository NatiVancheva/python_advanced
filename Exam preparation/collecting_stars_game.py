n = int(input())
matrix = []
player_r =0
player_c = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "P":
            player_r, player_c = row, col
            matrix[row][col] = "."

while True:
    