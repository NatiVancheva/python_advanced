from collections import deque
food_quantity = int(input())
orders = deque(int(x) for x in input().split()) # трябва да вземе в числена стойност от въведеното

print(max(orders))

while orders and orders[0] <= food_quantity: # take the first element
    food_quantity -= orders.popleft() # popleft вади първия елемент и изважда количеството храна

if orders:
    print(f"Orders left:", *orders)
else:
    print("Orders complete")