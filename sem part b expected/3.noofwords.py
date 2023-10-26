#3.no of characters in string and no of words in sentence
s = input("enter the strng : ")
words = s.split()
print("no of words : ",len(words))
for i in words:
    print(f'{i} has {len(i)} characters')
