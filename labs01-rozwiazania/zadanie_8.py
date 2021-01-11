"""
Otwórz plik `zen_of_python.txt` i zlicz liczbę linii i słów w tym pliku. 
Następnie przerób kod na funkcję, która jako argument będzie przyjmować ściężkę do pliku i będzie zwracać 
słownik z dwoma kluczami: `liczba_linii` i `liczba_slow`.
"""

def count(path):
    num_lines = 0
    num_words = 0
    with open(path) as ffile:
        for line in ffile:
            num_lines += 1
            num_words += len(line.strip().split())
    return {
        'liczba_linii': num_lines,
        'liczba_slow': num_words,
    }

print(count('./labs01/zen_of_python.txt'))
