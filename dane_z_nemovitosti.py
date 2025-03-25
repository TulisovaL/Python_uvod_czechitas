import math 
from abc import ABC, abstractmethod

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property(ABC):
    def __init__(self, locality): #třída Property reprezentuje nemovitost, třída má atribut locality 
        self.locality = locality
    @abstractmethod
    def calculate_tax(self): #Abstraktní metoda pro výpočet daně.
        pass

    @abstractmethod
    def __str__(self):      #Abstraktní metoda pro reprezentaci objektu jako řetězce.
        pass

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        estate_types = {
            "Zemědělský pozemek": 0.85,
            "Stavební pozemek": 9,
            "Les": 0.35,
            "Zahrada": 2
        }

     
        # Získání koeficientu z dictionary, pokud existuje
        koeficient = estate_types.get(self.estate_type, None)
    
        if koeficient is None:
        # Pokud nebyl nalezen odpovídající typ nemovitosti, můžeme přidat výchozí hodnotu nebo chybu
            raise ValueError(f"Neznámý typ nemovitosti: {self.estate_type}")
        dan_z_nemovitosti = self.area * koeficient * self.locality.locality_coefficient #vzorec pro výpočet daně
        
        return math.ceil(dan_z_nemovitosti) #tak aby hodnota daně byla zobrazená jako celé číslo
    
    def __str__(self):
        return f'{self.estate_type}, lokalita {self.locality.name}, koeficient {self.locality.locality_coefficient}, {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč.'

class Residence(Property):
   
    def __init__(self, locality, estate_type, area, commercial=False):
        super().__init__(locality)

        self.type = estate_type
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
            

pozemek_1 = Estate(Locality("lokalita", 2), "Les", 500)
print(pozemek_1)

byt_1 = Residence(Locality("lokalita", 3), "Byt pro osobní bydlení", 60)        #byt určený k bydlení
print(byt_1)

byt_2 = Residence(Locality("lokalita", 3), "Byt ke komerčním účelům", 60, True)  #byt určený ke komerčním účelům
print(byt_2)

#testy
pozemek_2 = Estate(Locality("Manětín", 0.8), "Zemědělský pozemek", 900)
print(pozemek_2)

dum_1 = Residence(Locality("Manětín", 0.8), "Dům pro osobní bydlení", 120)
print(dum_1)

kancelar_1 = Residence(Locality("Brno", 3), "Kancelář", 90, True)
print(kancelar_1)

report = TaxReport("Jan Novák")      #výpočet daně pro poslední tři testovací subjekty
report.add_property(pozemek_2)
report.add_property(dum_1)
report.add_property(kancelar_1)
print(report)