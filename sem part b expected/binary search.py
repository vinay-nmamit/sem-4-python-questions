#binary search
def binarysearch(lst,l,h,key):
    if l<=h:
        mid=(l+h)//2
        if lst[mid]==key:
            return mid
        elif lst[mid]>key:
            return binarysearch(lst,mid+1,h,key)
        else:
            return binarysearch(lst,mid-1,h,key)
    else:
        return -1


lst = []
n = int(input("enter no of elements: "))
for i in range(0,n):
    x = int(input("enter elements: :"))
    lst.append(x)
lst.sort()
key = int(input("enter key element: "))
print("list of elements: ",lst)

r = binarysearch(lst,0,len(lst)-1,key)
if r!= -1:
    print("key found at index: ", r)
else:
    print("key element not found")
