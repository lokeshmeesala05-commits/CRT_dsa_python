class Student:
    def __init__(self,name,rollno,branch):
        print("self:",self)
        self.name=name
        self.rollno=rollno
        self.branch=branch

s1=Student("Lokesh",18,"CSE")
s2=Student("Raja",19,"ECE")

print("Address:",s1)
print("Name:",s1.name)
print("Rollno:",s1.rollno)
print("Address:",s2)
print("Name:",s2.name)
print("Rollno:",s2.rollno)


        
