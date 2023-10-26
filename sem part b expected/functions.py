#function to find sum of all numbers in a list
def sum_of_lst(num):
    total_sum = 0
    for i in num:
        total_sum = total_sum + i
    return total_sum

num_list = [1, 2, 3, 4, 5]
result = sum_of_lst(num_list)
print(result)

#product
def productoflst(num):
    pro = 1
    for i in num:
        pro = pro * i
    return pro

num_list = [1, 2, 3, 4, 5]
result = productoflst(num_list)
print(result)

#recursive func to find sum of first n intergers
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

num = int(input("Enter the number: "))
result = sum(num)
print("Sum of numbers from 1 to", num, "is:", result)

#pascals triangle
from math import factorial

n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        coefficient = factorial(i) // (factorial(j) * factorial(i-j))
        print(coefficient, end=" ")
    print()



