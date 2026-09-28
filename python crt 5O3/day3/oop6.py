#Multi level inheritance
class Animal:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight

    def details(self):
        print("Name:",self.name)
        print("Weight:",self.weight)
        
class Dog(Animal):
    def sound(self):
        print("Barks")

class Gershe(Dog):
    pass

gs=Gershe("German Shepered",19)
gs.sound()
