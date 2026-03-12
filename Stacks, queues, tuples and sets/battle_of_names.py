n = int(input())

sum_of_set = 0
odd_set = set()
even_set = set()

for row in range(1, n + 1):
    name = input()
    suma = 0
    for char in name:
        ascii_number = ord(char)
        suma += ascii_number

    value = suma // row

    if value % 2 == 0:
        even_set.add(value)
    else:
        odd_set.add(value)

if sum(odd_set) == sum(even_set):
    result = odd_set.intersection(even_set)
    #print(", ".join(str(x) for x in even_set | odd_set))
    #print(*even_set | odd_set, sep=", ")

elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
    #print(", ".join(str(x) for x in even_set - odd_set))
    # print(*even_set - odd_set, sep=", ")

elif sum(even_set) > sum(odd_set):
    result = odd_set.symmetric_difference(even_set)
    #print(", ".join(str(x) for x in even_set ^ odd_set))
    # print(*even_set ^ odd_set, sep=", ")

print(*result, sep=", ")
