#calculate length of strng add ing at the end len sud be more than 3 if it is already ing then add ly if len less than 3 leave it unchanged
a = input("enter the string: ")
b = len(a)

if b<3:
    print(a)
elif b>3:
    if(a[b-3:b+1]=="ing"):
        a= a + "ly"
        print(a)
    else:
        a = a + "ing"
        print(a)
        
