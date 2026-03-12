from collections import deque

substances = [int(x) for x in input().split(", ")]
crystals = deque(int(x) for x in input().split(", "))

potions = {
    "Brew of Immortality": 110,
    "Essence of Resilience": 100,
    "Draught of Wisdom": 90,
    "Potion of Agility": 80,
    "Elixir of Strength": 70
}

crafted = []

while substances and crystals and len(crafted) < 5:
    substance = substances.pop()
    crystal = crystals.popleft()
    total_energy = substance + crystal

    crafted_now = False
    for name, value in potions.items():
        if value == total_energy and name not in crafted:
            crafted.append(name)
            crafted_now = True
            break

    if crafted_now:
        continue

    best_value = -1
    best_potion = None

    for name, value in potions.items():
        if value < total_energy and name not in crafted:
            if value > best_value:
                best_value = value
                best_potion = name

    if best_potion:
        crafted.append(best_potion)
        crystal -= 20
        if crystal > 0:
            crystals.append(crystal)
    else:
        crystal -= 5
        if crystal > 0:
            crystals.append(crystal)

if len(crafted) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted:
    print(f"Crafted potions: {', '.join(crafted)}")

if substances:
    print(f"Substances: {', '.join(map(str, reversed(substances)))}")

if crystals:
    print(f"Crystals: {', '.join(map(str, crystals))}")

