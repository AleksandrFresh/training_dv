#a=[]
#a=map(int, input("Введите 10-ть чисел через пробел: ").split())
#m = max(a)
#print(m)


#iteres = int(input("введите колво итраций: "))
#myMax=0

#for i in  range (iteres):
#    a = int(input("enter num: "))
#    if a > myMax :
#        myMax = a

#print(myMax)

iteres = int(input("введите колво итраций: "))
myMax = 0
a = 0

while True:
    a = int(input("enter num: "))
    if a == 13:
        break
    elif a > myMax :
        myMax = a

print(myMax)
