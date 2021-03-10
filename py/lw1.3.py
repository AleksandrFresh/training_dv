a, b, c = map(int, input("Введите 3-и числа через пробел: ").split())
if (a+b>=c and b+c>=a and c+a>=b):
    print("ok")
else:
    print("no")