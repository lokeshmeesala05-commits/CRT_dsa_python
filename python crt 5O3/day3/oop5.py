#single level inheritance
class Animal:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight

    def details(self):
        print("Name:",self.name)
        print("Weight:",self.weight)
        
class Cat(Animal):
    pass

c=Cat("Tom",10)
print(c)
print(c.details())
