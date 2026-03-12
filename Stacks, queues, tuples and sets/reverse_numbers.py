numbers = list(input().split())
# for _ in range(len(numbers)):
#     print(numbers.pop(), end=" ")
stack = []
while numbers:
    stack.append(numbers.pop())
print(" ".join(stack))