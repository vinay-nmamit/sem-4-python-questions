filename = input("enter file name: ")
infile=open(filename,"r")
vowels=set("AEIOUaeiou")
cons=set("bdfghjklmnpqrstvwxyzBDFGHJKLMNPQRSTVWXYZ")
text=infile.read()

countv = 0
for v in text:
    for v in vowels:
        countv+=1

countc = 0
for v in text:
    for v in cons:
        countc += 1
   
print("The number of vowels is",countv)
print("the number of consonents is",countc)