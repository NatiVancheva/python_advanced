from collections import deque
bees = deque(int(x) for x in input().split())
bee_eaters = [int(x) for x in input().split()]

while bees and bee_eaters:
    first_bees = bees.popleft()
    last_eaters = bee_eaters.pop()

    needed_bees = last_eaters * 7
    if needed_bees == last_eaters:
        continue

    elif needed_bees < first_bees:
        first_bees -= needed_bees
        bees.append(first_bees)
    else:
        dead_eaters = first_bees // 7
        last_eaters -= dead_eaters
        if last_eaters > 0:
            bee_eaters.append(last_eaters)
    
print("The final battle is over!")
if not bees and not bee_eaters:
    print("But no one made it out alive!")
elif bees:
    print(f"Bee groups left: {', '.join(map(str, bees))}")
elif bee_eaters:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters))}")