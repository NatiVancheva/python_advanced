# n = int(input())
# stack = []
#
# for _ in range(n):
#     query = input().split()
#     if query[0] == "1":
#         stack.append(int(query[1]))
#     elif stack:
#         if query[0] == "2":
#             stack.pop()
#         elif query[0] == "3":
#             print(max(stack))
#         elif query[0] == "4":
#             print(min(stack))
#
# print(", ".join(str(x) for x in reversed(stack))) # join samo raboti s string затова е със str

n = int(input())
stack = []

functions = {
    "1": lambda x: stack.append(int(x)),
    "2": lambda: stack.pop() if stack else None,
    "3": lambda: print(max(stack)) if stack else None,
    "4": lambda: print(min(stack)) if stack else None
}

for _ in range(n):
    query = input().split()
    functions[query[0]](*query[1:]) # извиква функцията която е на ключ на query на нулева позиция
    # 1: се използва когато хем имаме хем нямаме параметър затова : е да чете след първия индекс нататък
    # * се използва за разпакетиране на лист (да вземе всяка една стойност по отделно)

print(*reversed(stack), sep=", ") #  sep показва интервала между двете числа
