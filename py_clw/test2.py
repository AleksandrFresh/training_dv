from random import randint

x = randint(1, 10)
a = int(input('введите число: '))
while x != a:
    
        if a == x :
            print ("ok")
            break
        else:
            print ("wrong, try again")
            a = int(input('введите число: '))


