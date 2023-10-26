#5.to find second largest and second smallest
lst = []
n = int(input("enter the no of elements: "))
for i in range (0,n):
    x = int(input("enter elements: "))
    lst.append(x)
lst.sort()
n = len(lst)

print('Second Largest Number: ',lst[n-2])

print('Second Smallest Number: ',lst[1])
