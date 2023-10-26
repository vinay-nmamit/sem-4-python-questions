#to perform divison operation on wo random numbers
import random

try:
    a=random.randint(0,5)
    b=random.randint(0,5)
    c=a/b
    f=open("res.txt",'w')
    f.write(" a= %d b= %d result= %f "%(a,b,c))
    f.close()
    r=open("res.txt").read()
    print(" contents of file :",r)
except:
    print("Error! denominator is zero")
