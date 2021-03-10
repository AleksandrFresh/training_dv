from math import sqrt

a, b, c = map(int, input("Введите 3-и числа через пробел: ").split())
#a*x**2+b*x+c=0
D=b**2-4*a*c
x=-b/2*a
x1=(-b+sqrt(D))/(2*a)
x2=(-b-sqrt(D))/(2*a)
if D < 0:
    print("корней нет!")
elif D == 0 :
    print(round(x))

else :
    print(round(x1))
    print(round(x2))

print("конец")