from collections import deque

color_strings = deque(input().split())

main_colors = ["red", "yellow", "blue"]

secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

collected_colors = []

while color_strings:
    first_string = color_strings.popleft()
    last_string = color_strings.pop() if color_strings else ""

    for color in (first_string + last_string, last_string + first_string):
        if color in main_colors or color in secondary_colors:
            collected_colors.append(color)
            break
    else:
        if len(first_string) > 1:
            color_strings.insert(len(color_strings) // 2, first_string[::-1])
        if len(last_string) > 1:
            color_strings.insert(len(color_strings) // 2, last_string[::-1])

for color in collected_colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)

from collections import deque

color_strings = deque(input().split())

main_colors = {"red", "yellow", "blue"}

secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

collected_colors = []

while color_strings:
    first = color_strings.popleft()
    last = color_strings.pop() if color_strings else ""

    found_color = None

    for color in (first + last, last + first):
        if color in main_colors or color in secondary_colors:
            found_color = color
            break

    if found_color:
        collected_colors.append(found_color)
    else:
        if len(first) > 1:
            color_strings.insert(len(color_strings) // 2, first[:-1])
        if len(last) > 1:
            color_strings.insert(len(color_strings) // 2, last[:-1])


final_colors = []

for color in collected_colors:
    if color in secondary_colors:
        if secondary_colors[color].issubset(collected_colors):
            final_colors.append(color)
    else:
        final_colors.append(color)

print(final_colors)
