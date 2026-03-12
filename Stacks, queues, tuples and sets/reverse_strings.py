#text = input()
#print(text[::-1])
text = list(input())
for _ in range(len(text)):
    print(text.pop(), end="")