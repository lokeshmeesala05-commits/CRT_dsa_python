#Hierarchical inheritance
class Aeroplane:
    def __init__(self,type,company_name):
        self.type=type
        self.company_name=company_name
class Indigo(Aeroplane):
    pass
class Spicejet(Aeroplane):
    pass
class Airindia(Aeroplane):
    pass
