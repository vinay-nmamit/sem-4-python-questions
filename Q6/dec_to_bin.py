dec = int(input("enter decimal: "))
temp = dec
list = []

while dec!=0:
    num = dec % 2
    list.append(num)
    dec = dec // 2

print("decimal: ",temp)
print("binary: ",end=" ")

n = len(list)
for i in range(1,n+1):
    i = i * -1
    print(list[i],end=" ")