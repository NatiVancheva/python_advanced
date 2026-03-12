SIZE = 5
matrix = []
my_position = []
targets = 0

for row in range(SIZE):
    line = input().split()
    matrix.append(line)
    for col in range(SIZE):
        if line[col] == "A":
            my_position = [row, col]
        elif line[col] == "x":
            targets += 1

number_of_commands = int(input())
possible_moves = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

shot_targets = []

for _ in range(number_of_commands):
    command = input().split()
    action = command[0]
    direction = command[1]

    if action == "shoot":
        row = my_position[0] + possible_moves[direction][0]
        col = my_position[1] + possible_moves[direction][1]
        while 0 <= row < SIZE and 0 <= col < SIZE:
            if matrix[row][col] == "x":
                shot_targets.append([row, col])
                matrix[row][col] = "."
                targets -= 1
                break
            row += possible_moves[direction][0]
            col += possible_moves[direction][1]
        if targets == 0:
            print(f"Training completed! All {len(shot_targets)} targets hit.")
            break

    elif action == "move":
        steps = int(command[2])
        row = my_position[0] + possible_moves[direction][0] * steps
        col = my_position[1] + possible_moves[direction][1] * steps
        if 0 <= row < SIZE and 0 <= col < SIZE and matrix[row][col] == ".":
            matrix[my_position[0]][my_position[1]] = "." #сменяме с точка предишната ни позиция
            matrix[row][col] = "A"
            my_position = [row, col]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

for target in shot_targets:
    print(target)