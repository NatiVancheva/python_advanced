from collections import deque
kids = deque(input().split())
num = int(input())
#kids.rotate(1) завърта като последния елемент на първа позиция, ако искам да е на обратно е -1
while len(kids) > 1:
    kids.rotate(-num + 1) #-(n-1)
    print(f"Removed {kids.popleft()}")
print(f"Last is {kids.popleft()}")