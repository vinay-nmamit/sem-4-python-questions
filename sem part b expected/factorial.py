#6.recursive func to find factorial of a given number

def fact(n):
    if n<=1:
        return 1
    else:
        return fact(n-1)*n

n = int(input("ener the elemenmt: "))
f = fact(n)
print(f"factorial of {n} is {f}")
