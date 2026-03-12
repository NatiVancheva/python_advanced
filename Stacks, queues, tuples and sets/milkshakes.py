from collections import deque
chocolate = [int(x) for x in input().split(", ")]
milk_cups = deque(int(x) for x in input().split(", "))
milkshakes = 0

while chocolate and milk_cups and milkshakes < 5:
    if chocolate[-1] <= 0 and milk_cups[0] <= 0:
        chocolate.pop()
        milk_cups.popleft()
        continue

    if chocolate[-1] <= 0:
        chocolate.pop()
        continue

    if milk_cups[0] <= 0:
        milk_cups.popleft()
        continue

    if chocolate[-1] == milk_cups[0]:
        milkshakes += 1
        chocolate.pop()
        milk_cups.popleft()

    else:
        milk_cups.rotate(-1)
        chocolate[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(el) for el in chocolate) if chocolate else 'empty'}")
print(f"Milk: {', '.join(str(el) for el in milk_cups) if milk_cups else 'empty'}")