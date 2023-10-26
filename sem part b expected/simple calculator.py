#simple calculator

print("CALCULATOR")
print("\n1.Add \n2.Subtract \n3.Multiply \n4.Divide")
ch = int(input("enter choice (1-4) = "))

if ch == 1:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = a + b
    print("sum is:", c)
elif ch == 2:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = a - b
    print("difference is:", c)
elif ch == 3:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = a * b
    print("product is:", c)
elif ch == 4:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = a / b
    print("quotient is:", c)
else:
    print("Invalid choice")

#sum of numbers in a list, print all numbers, sqaures of all numbers, first 5 natural numbers
lst = [ 9,4,5,15,6,1]
lst2 = []
sum = 0
for i in lst:
    sum = sum + i
print("sum is: ",sum)

for i in range(len(lst)):
    print("numbers: ",lst[i])
    
for i in lst:
    sq = i*i
    lst2.append(sq)
print(lst2)

for val in range(1,6):
    print(val)


    
         
