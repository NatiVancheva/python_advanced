def fill_the_box(height, length, width, *args):
    area = height * length * width
    sum_arg = 0
    result = ""
    for curr_arg in args:
        if curr_arg == "Finish":
            break
        sum_arg += curr_arg
        if area > sum_arg:
            return f"There is free space in the box. You could put {area - sum_arg} more cubes."
        return f"No more free space! You have {sum_arg - area} more cubes."


print(fill_the_box(2, 8,
2, 2, 1, 7, 3, 1, 5,
"Finish"))

print(fill_the_box(5, 5,
2, 40, 11, 7, 3, 1, 5,
"Finish"))

print(fill_the_box(10, 10,
10, 40, "Finish", 2, 15,
30))