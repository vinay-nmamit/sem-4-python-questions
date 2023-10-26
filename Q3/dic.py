#keys as first characters and value as words with characters
lst = []
dic = {}

n = int(input("enter the range: "))
for i in range(n):
    x = input("enter the words : ")
    lst.append(x)
print("List: ",lst)

for word in lst:
    first = word[0]
    if first in dic:
        dic[first].append(word)
    else:
        dic[first] = [word]
print("Dictionary: ",dic)
        

    





        