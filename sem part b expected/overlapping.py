f1=open("a.txt",'w')
for i in range(2,1001):
    for x in range(2,i):
        if(i%x==0):
             break
    else:
     f1.write(str(i)+"\n")
f1.close()

f2=open("b.txt",'w')
for i in range(1001):
    f2.write(str(i)+"\n")
f2.close()
        
r1=open("a.txt").read()
r2=open("b.txt").read()

for i,j in ((x,y) for x in r1.split() for y in r2.split()):
 if(i==j):
     print(i)
