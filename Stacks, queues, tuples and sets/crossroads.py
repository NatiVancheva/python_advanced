from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()

total_cars_passed = 0

while True:
    command = input()
    if command == "END":
        print("Everyone is safe.")
        print(f"{total_cars_passed} total cars passed the crossroads.")
        break

    elif command == "green":
        green = green_light_duration

        while cars and green > 0:
            car = cars.popleft()
            car_length = len(car)

            if car_length <= green:
                green -= car_length
                total_cars_passed += 1
            else:
                remaining = car_length - green
                if remaining <= free_window_duration:
                    total_cars_passed += 1
                else:
                    hit_index = green + free_window_duration
                    print("A crash happened!")
                    print(f"{car} was hit at {car[hit_index]}.")
                    exit()

    else:
        cars.append(command)


