#to display name and usn
class student:
    name=""
    usn=""
    def read(self):
        self.name=input("Enter Name ")
        self.usn=input("Enter usn ")

    def display(self):
        print("Name :%s\nUSN :%s "%(self.name,self.usn))

s=student()
s.read()
s.display()
