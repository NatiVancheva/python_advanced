def sum_neg(*args):
    suma_neg = 0
    for el in args:
        if el < 0:
            suma_neg += el
    return suma_neg

def sum_pos(*args):
    suma_pos = 0
    for el in args:
        if el > 0:
            suma_pos += el
    return suma_pos

numbers = list(map(int, input().split()))
negative_sum = sum_neg(*numbers)
positive_sum = sum_pos(*numbers)
print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")