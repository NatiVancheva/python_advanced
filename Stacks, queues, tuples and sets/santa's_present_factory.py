# from collections import deque
# materials = [int(x) for x in input().split()]
# magic_level = deque(int(x) for x in input().split())
#
# points = {
#     150: "Doll",
#     250: "Wooden train",
#     300: "Teddy bear",
#     400: "Bicycle"
# }
# toys = {}
#
# while materials and magic_level:
#     total_magic = materials[-1] * magic_level[0]
#     if total_magic in points:
#         materials.pop()
#         magic_level.popleft()
#         new_toy = points[total_magic]
#         if toys[new_toy] not in toys:
#             toys[new_toy] = 0
#         toys[new_toy] += 1
#     if total_magic < 0:
#         materials.append(materials.pop() + magic_level.popleft())
#     elif total_magic > 0:
#         materials[-1] += 15
#         magic_level.popleft()
#     else:
#         if materials[-1] == 0:
#             materials.pop()
#             continue
#         if magic_level[0] == 0:
#             magic_level.popleft()
#             continue
#
# if ("Doll" in toys and "Wooden train" in toys) or ("Teddy bear" in toys and "Bicycle" in toys):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
#
# if materials:
#     print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
#
# if magic_level:
#     print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
#
# for key, value in sorted(toys.items()):
#     print(f"{key}: {value}")


from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

points = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

toys = {}

while materials and magic_level:
    if materials[-1] == 0:
        materials.pop()
        continue
    if magic_level[0] == 0:
        magic_level.popleft()
        continue

    total_magic = materials[-1] * magic_level[0]

    if total_magic in points:
        toy = points[total_magic]
        toys[toy] = toys.get(toy, 0) + 1
        materials.pop()
        magic_level.popleft()

    elif total_magic < 0:
        result = materials.pop() + magic_level.popleft()
        materials.append(result)

    else:
        magic_level.popleft()
        materials[-1] += 15

if ("Doll" in toys and "Wooden train" in toys) or ("Teddy bear" in toys and "Bicycle" in toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")

if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for toy, count in sorted(toys.items()):
    print(f"{toy}: {count}")


