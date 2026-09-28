class Student:
    def __init__(self,name,rollno,branch):
        print("self:",self)
        self.name=name
        self.rollno=rollno
        self.branch=branch

s1=Student("Lokesh",18,"CSE")
s2=Student("Raja",19,"ECE")
print("dir(student)):")
print(dir(Student))
print("dir(list):")
print(dir(list))
