#lab 4
#find length of the list
lst = [1,2,3,4,5,6,2,3,4]
x = len(lst)
print(x)

#find largest number in the list
def largestnum(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

numbers = [45, 12, 67, 89, 23, 56, 99, 34]
result = largestnum(numbers)
print("The largest number in the list is:", result)

#fnd sum of all elements
lst = [1,2,3,4,5,6]
sum = 0
for i in lst:
    sum += i
print(sum)


#ascending'
lst = [1,2,3,4,5]
for i in range(len(lst)-1):
    if lst[i]<lst[i+1]:
        continue
    else:
        print("not in ascending")
        exit(0)
print("its in ascending order")

#even numbers in a list
lst = [2, 3, 4, 5, 6]
lst2= []

for num in lst:
    if num % 2 == 0:
        lst2.append(num)

if lst2:
    print("Even numbers in the list:", lst2)
else:
    print("No even numbers in the list")

#merge two lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

def merge_lists(list1, list2):
    merged_list = list1 + list2
    return merged_list

merged_list = merge_lists(list1, list2)
print("Merged list:", merged_list)

#to interchange first and last element in the list
# Sample list
lst = [1, 2, 3, 4, 5]
if len(lst) >= 2:
    lst[0], lst[-1] = lst[-1], lst[0]
else:
    print("The list must have at least 2 elements to perform interchange.")
print(lst)


#reverse list
lst = [1, 2, 3, 4, 5]
for i in range(len(lst) - 1, -1, -1):
    print(lst[i])

#print this pattern
n = int(input("Enter the size: "))
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

#cube of all numbers
def calculate_cube_up_to_given_number(n):
    for num in range(1, n + 1):
        cube = num ** 3
        print(f"The cube of {num} is: {cube}")

given_number = int(input("Enter a number: "))
calculate_cube_up_to_given_number(given_number)

#sum of n series
def sum_of_arithmetic_series(n, first_term, last_term):
    return n * (first_term + last_term) / 2

try:
    n = int(input("Enter the number of terms in the series: "))
    first_term = float(input("Enter the first term of the series: "))
    last_term = float(input("Enter the last term of the series: "))

    result = sum_of_arithmetic_series(n, first_term, last_term)
    print(f"The sum of the arithmetic series up to {n} terms is: {result}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")



