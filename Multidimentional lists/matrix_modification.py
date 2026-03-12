n =int(input())
matrix = []

for _ in range(n):
    data = [int(x) for x in input().split()]
    matrix.append(data)


while True:
    commands = input().split()
    if commands[0] == "END":
        break

    r, c, value = map(int, commands[1:])
    if 0 > r or r >= n or 0 > c or c >= n:
        print("Invalid coordinates")
        continue

    if commands[0] == "Add":
        matrix[r][c] += value
    elif commands[0] == "Subtract":
        matrix[r][c] -= value

[print(*row) for row in matrix]





