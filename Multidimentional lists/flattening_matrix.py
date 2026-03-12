rows = int(input())
nums = []
# matrix = [map(int, input().split(", ")) for _ in range(rows)]
# flattered = [num for row in matrix for num in row]
# print(flattered)
for i in range(rows):
    data = [int(el) for el in input().split(", ")]
    nums.extend(data) #добавя (много) елементи в друг итеригруем обект поотделно(слива списъци)
print(nums)

# flattened = []
# for sublist in nums:
#     for num in sublist:
#         flattened.append(num)
# print(flattened)


