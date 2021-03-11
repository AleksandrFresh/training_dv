def getSum(x, y=0, op='+'):
    if op == '+':
        return x + y
    elif op == "*":
        return x * y
    elif op == '-':
        return x - y
    return None

print(getSum(5, 20, '*'))
print(getSum(5, 213, '+'))
a = getSum(5, 21, '%')
print(a)




def findMax(stopValue=10):
    iteres = int(input("введите колво итраций: "))
    myMax = 0
    a = 0
    while True:
        a = int(input("enter num: "))
        if a == stopValue:
            break
        elif a > myMax :
            myMax = a
    print(myMax)

#findMax()
#findMax(int(input("enter stop-num: ")))
