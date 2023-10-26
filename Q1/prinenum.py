#1.prime numbers in given range
for i in range(2,int(input(" Enter end range: "))+1):
    for x in range(2,i):
        if(i%x==0):
            break
    else:
        print(i,end=" ")


