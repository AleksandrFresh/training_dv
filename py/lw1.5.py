line=input("Введите текст: ")
li=[]
sought=["a", "o", "e", "i", "u", "y"]
num=0
for i in line:
    li += i.lower()
for x in li:
    for j in sought:
        if x == j:
            num += 1
print(num)

