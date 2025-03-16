import math #modul math
from abc import ABC, abstractmethod

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property(ABC):
   
    @abstractmethod
    def __init__(self, locality, locality_coefficient): #třída Property reprezentuje nemovitost, třída má atribut locality 
        self.locality = Locality(locality, locality_coefficient)
    
    @abstractmethod
    def calculate_tax(self): #Abstraktní metoda pro výpočet daně.
        pass

    @abstractmethod
    def __str__(self):      #Abstraktní metoda pro reprezentaci objektu jako řetězce.
        pass

class Estate(Property):
    def __init__(self, locality, estate_type, area, locality_coefficient):
        super().__init__(locality, locality_coefficient)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        if self.estate_type == "Zemědělský pozemek":
            koeficient = 0.85
        if self.estate_type == "Stavební pozemek":
            koeficient = 9
        if self.estate_type == "Les":
            koeficient = 0.35
        if self.estate_type == "Zahrada":
            koeficient = 2

        dan_z_nemovitosti = self.area * koeficient * self.locality.locality_coefficient #vzorec pro výpočet daně
        return math.ceil(dan_z_nemovitosti) #tak aby hodnota daně byla zobrazená jako celé číslo
    
    def __str__(self):
        return f'{self.estate_type}, lokalita {self.locality.name}, koeficient {self.locality.locality_coefficient}, {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč.'

class Residence(Property):
    def __init__(self, type, locality, area, locality_coefficient, commercial=False):
        super().__init__(locality, locality_coefficient)
        self.type = type
        self.area = area
        self.commercial = commercial
    
    def calculate_tax(self)->int: #spočítá výši daně pro byt a vrátí hodnotu jako číslo
        hodnota_dane_pro_rezidenci = self.area * self.locality.locality_coefficient * 15
        if self.commercial: 
            hodnota_dane_pro_rezidenci = hodnota_dane_pro_rezidenci * 2
        return math.ceil(hodnota_dane_pro_rezidenci)

    def __str__(self):
        return f'{self.type}, lokalita {self.locality.name}, koeficient {self.locality.locality_coefficient}, {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč.'

class TaxReport:
    def __init__(self, name):
        self.name = name
        self.property_list = []
    
   
    def add_property(self, property):
        self.property_list.append(property)

    def calculate_tax(self):
        tax = 0
        for property in self.property_list:
            tax = property.calculate_tax() + tax
        return tax
    
    def __str__(self):
        return f'{self.name} bude odvádět daň ve výši {self.calculate_tax()} Kč.' 
            

pozemek_1 = Estate("lokalita", "Les", 500, 2)
print(pozemek_1.calculate_tax())
print(pozemek_1)

byt_1 = Residence("Byt pro osobní bydlení", "lokalita", 60, 3)        #byt určený k bydlení
print(byt_1.calculate_tax())
print(byt_1)

byt_2 = Residence("Byt ke komerčním účelům", "lokalita", 60, 3, True)  #byt určený ke komerčním účelům
print(byt_2.calculate_tax())
print(byt_2)

#testy
pozemek_2 = Estate("Manětín", "Zemědělský pozemek", 900, 0.8)
print(pozemek_2.calculate_tax())
print(pozemek_2)

dum_1 = Residence("Dům pro osobní bydlení", "Manětín", 120, 0.8)
print(dum_1.calculate_tax())
print(dum_1)

kancelar_1 = Residence("Kancelář", "Brno", 90, 3, True)
print(kancelar_1.calculate_tax())
print(kancelar_1)

report = TaxReport("Jan Novák")      #výpočet daně pro poslední tři testovací subjekty
report.add_property(pozemek_2)
report.add_property(dum_1)
report.add_property(kancelar_1)
print(report.calculate_tax())
print(report)