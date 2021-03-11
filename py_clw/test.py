a = int(input('введите число: '))

if a % 15 == 0:
    print ("ping-pong")
elif a % 3 == 0:
    print("ping")
elif a % 5 == 0:
    print("pong")
else:
    print("bay-bay)))")


x = 10
while x > 0:
    if x % 2 == 0:
        print(x)
    x -= 1

print("the end")


for i in range(11,0,-1):
    if i % 2 == 0:
        print(i)
          
print("the end")
