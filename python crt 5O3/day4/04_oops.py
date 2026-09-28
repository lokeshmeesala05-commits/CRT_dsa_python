class Employee:
    #static/class varialble
    companyName="Infosys"
    def __init__(self,name,designation,sal):
        self.name=name
        self.designation=designation
        self.sal=sal

    def details(self):
        print("Name:",self.name)
        print("Designation:",self.designation)
        print("Salary:",self.sal)

e1=Employee("NarayanaMurthy","CEO",50000)  #object/non static variables
e2=Employee("SudhaMurthy","ChairWoman",100000)
e1.details()
e2.details()
# print(Employee.name)      ---->error
# print(Employee.companyName) ----->error
print(e1.name)
