
"""
Słownik `oceny` zawiera oceny kilku osób. Kluczami są imiona dzieci, a wartosciami -- ich oceny.
Uzupełnij słownik `rozklad`, którego kluczami są oceny, a wartosciami -- listy... 
"""

oceny = {
    'Albert': 4.5,
    'Beata': 5,
    'Cecylia': 4,
    'Dariusz': 4,
    'Eliza': 3,
    'Feliks': 5,
    'Grzegorz': 4.5,
    'Izabela': 4.5
}

rozklad = {
    5: [],
    4.5: [],
    4: [],
    3: []
}

for osoba in oceny:
    rozklad[oceny[osoba]].append(osoba)

print(rozklad)
