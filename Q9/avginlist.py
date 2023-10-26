def avg(lst):
    return sum(lst)/len(lst)

lst = []
n = int(input("enter n: "))
for i in range(n):
    lst.append(int(input("enter number: ")))
print("Avg=",avg(lst))