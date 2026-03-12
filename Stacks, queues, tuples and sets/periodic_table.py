n = int(input())
chemical_elements = set()

for _ in range(n):
    elements = input().split()
    for el in elements:
        chemical_elements.add(el)

print(*chemical_elements, sep="\n")