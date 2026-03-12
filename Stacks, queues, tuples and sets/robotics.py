from collections import deque
robots_names = input().split(";")
robots = []
hours, minutes, seconds = map(int, input().split(":"))
current_time_in_seconds = hours * 3600 + minutes * 60 + seconds
products = deque()

for robot in robots_names:
    name, process_time = robot.split("-")
    robots.append([name, int(process_time), 0]) # 0 shows when the robot will be free again

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

    while product:
        current_time_in_seconds += 1
        products.popleft()
        assigned = False

        for robot in robots:
            if robot[2] <= current_time_in_seconds:
                robot[2] = robot[1] + current_time_in_seconds # the time it will be free
                time = (current_time_in_seconds % 24) * 3600
                h = time // 3600
                m = (time % 3600) // 60
                s = time % 60
                print(f"{robot[0]} - {product} [{h:02d}:{m:02d}:{s:02d}]")
                break

        if not assigned:
            products.append(product)


# from collections import deque
#
# robots_names = input().split(";")
# robots = []
# 
# hours, minutes, seconds = map(int, input().split(":"))
# current_time_in_seconds = hours * 3600 + minutes * 60 + seconds
#
# products = deque()
#
# for robot in robots_names:
#     name, process_time = robot.split("-")
#     robots.append([name, int(process_time), 0])
#
# while True:
#     product = input()
#     if product == "End":
#         break
#     products.append(product)
#
# while products:
#     current_time_in_seconds += 1
#     product = products.popleft()
#     assigned = False
#
#     for robot in robots:
#         if robot[2] <= current_time_in_seconds:
#             robot[2] = robot[1] + current_time_in_seconds
#             t = current_time_in_seconds % (24 * 3600)
#             h = t // 3600
#             m = (t % 3600) // 60
#             s = t % 60
#             print(f"{robot[0]} - {product} [{h:02d}:{m:02d}:{s:02d}]")
#             assigned = True
#             break
#
#     if not assigned:
#         products.append(product)

