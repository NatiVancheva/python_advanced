n = int(input())
students = {}
for i in range(n):
    name, grade = input().split()
    if name not in students:
        students[name] = []
        students[name].append(float(grade))
for name, grades in students.items():
    average = sum(grades) / len(grades)
    print(f"{name} -> {" ".join([str(el) for el in grades])} (avg: {average:.2f})")
