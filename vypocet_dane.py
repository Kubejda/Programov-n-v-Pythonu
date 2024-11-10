import math

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property:
    def __init__(self, locality):
        self.locality = locality

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        if self.estate_type == "land":
            return math.ceil(self.area * 0.85 * self.locality.locality_coefficient)
        if self.estate_type == "building site":
            return math.ceil(self.area * 9 * self.locality.locality_coefficient)
        if self.estate_type == "forrest":
            return math.ceil(self.area * 0.35 * self.locality.locality_coefficient)
        if self.estate_type == "garden":
            return math.ceil(self.area * 2 * self.locality.locality_coefficient)

    
# Čelákovice = Locality("Čelákovice", 2)
# pozemek = Estate(Čelákovice, "forrest", 500)
# print(pozemek.calculate_tax())

class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        if self.commercial == True:
            return self.area * self.locality.locality_coefficient * 15 * 2
        if self.commercial == False:
            return self.area * self.locality.locality_coefficient * 15
    
    
# Manětín = Locality("Manětín", 0.8)
# Brno = Locality("Brno", 3)
# zemedelsky_pozemek = Estate(Manětín, "land", 900)
# dum = Residence(Manětín, 120, False)
# kancelar = Residence(Brno, 90, True)

# print(zemedelsky_pozemek.calculate_tax())
# print(dum.calculate_tax())
# print(kancelar.calculate_tax())

    