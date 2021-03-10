a, b = map(int, input("Введите 2-а числа через пробел: ").split())
print(a)
print(b)
if a % b == 0:
    print("Число", a, "делится на число", b, "без остатка")
else:
    print("Число", a, "не кратно числу", b)