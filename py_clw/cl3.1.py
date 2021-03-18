from random import randint

def generateList(num, minVal=0, maxVal=100):
    lst = []
    for i in range(num):
        lst.append(randint(minVal, maxVal))
    return lst

def solver(lst, value):
    print(min(lst))
    print(max(lst))
    
    sortLst = []
    for i in lst:
        if i % value == 0:
            sortLst.append(i)
    if sortLst:
        print(sortLst)
    else:
        print("not num")

        
MyList = generateList(20)
solver(MyList, 10)
print(MyList)
