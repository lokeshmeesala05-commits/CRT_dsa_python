class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bow Bow")   

class Cat(Animal):
    def sound(self):
        print("Meow Meow")

class Parrot(Animal):
    pass

d=Dog()
d.sound()
c=Cat()
c.sound()
p=Parrot()
p.sound()