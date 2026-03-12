from collections import deque
pumps_number = int(input())
pumps = deque()

for _ in range(pumps_number):
    current_fuel, current_distance = input().split()
    pumps.append({"fuel": int(current_fuel), "distance": int(current_distance)}) # запълваме като речник

start_position = 0
stops = 0

while stops < pumps_number:
    fuel = 0
    for i in range(pumps_number):
        fuel += pumps[i]["fuel"] #because of dictionary
        distance = pumps[i]["distance"]
        if fuel < distance:
            pumps.rotate(-1) # the first pump is last
            start_position += 1 # местим стартовата позиция
            stops = 0
            break
        fuel -= distance
        stops += 1

print(start_position)