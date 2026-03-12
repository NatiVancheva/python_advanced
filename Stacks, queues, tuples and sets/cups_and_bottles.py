from collections import deque
cups_quantity = deque(map(int, input().split()))
bottles_quantity = list(map(int, input().split()))
wasted_water = 0


while cups_quantity and bottles_quantity:
    current_cup = cups_quantity[0]
    current_bottle = bottles_quantity.pop()
    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
        cups_quantity.popleft()
    else:
        cups_quantity[0] -= current_bottle

if not cups_quantity:
    print("Bottles:", " ".join(map(str, bottles_quantity)))
else:
    print("Cups:", " ".join(map(str, cups_quantity)))

print(f"Wasted litters of water: {wasted_water}")
