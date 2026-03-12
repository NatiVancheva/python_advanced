from collections import deque
weight_packages = [int(x) for x in input().split()]
couriers_capacity = deque(int(x) for x in input().split())
total_weight = 0

while weight_packages and couriers_capacity:
    last_package = weight_packages[-1]
    first_courier = couriers_capacity.popleft()

    if first_courier >= last_package:
        first_courier -= last_package * 2
        if first_courier > 0:
            couriers_capacity.append(first_courier)
        total_weight += last_package
        weight_packages.pop()
    else:
        weight_packages[-1] -= first_courier
        total_weight += first_courier
    
print(f"Total weight: {total_weight} kg")

if not weight_packages and not couriers_capacity:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif weight_packages and not couriers_capacity:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(str(p) for p in weight_packages)}")
else:
    print(f"Couriers are still on duty: {', '.join(str(c) for c in couriers_capacity)} but there are no more packages to deliver.")
