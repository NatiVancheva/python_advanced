n = int(input())
names = set()

for _ in range(n):
    name = input()
    names.add(name) #сета сам ще провери дали има дубликати

for name in names:
    print(name)