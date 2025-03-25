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
    
    # Pokračování v dalších výpočtech s koeficientem
    # ...
