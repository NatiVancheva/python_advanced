from functools import reduce
def sum_nums(*args):
    return sum(args)

def sub_nums(*args):
    return reduce(lambda x, y: x-y, args) # взимат се два елемента от колекцията докато се получи резултата

def mul_num(*args):
    return reduce(lambda x, y: x * y, args)

def div_num(*args):
    return reduce(lambda x, y: x / y, args)

mapper = {
    "+": sum_nums, #referenciq kum funciq
    "-": sub_nums,
    "*": mul_num,
    "/": div_num
}

def operate(sign, *args):
    func = mapper[sign]
    return func[*args]

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))