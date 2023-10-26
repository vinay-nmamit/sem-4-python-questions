#2.list of list
def getsec(a):
    return a[1]

lst = []
n = int(input("number of sublists: "))
for i in range(0,n):
    x = input("enter name: "),input("enter age: ")
    lst.append(x)

print("list before sort: ",lst)

lst.sort(key=getsec, reverse=True)
print("list after sort: ",lst)


