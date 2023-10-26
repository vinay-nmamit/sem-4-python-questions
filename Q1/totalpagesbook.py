#class book with instance such as title and pages
class book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

    def __add__(self,other):
        return (book(self.title,self.pages+other.pages))
    

a = book("a",30)
b = book("b",40)
c = a + b
print(c.pages)
    




    
