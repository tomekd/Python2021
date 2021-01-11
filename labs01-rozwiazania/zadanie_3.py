"""
Korzystając ze poniższego słownika, który zawiera informacje z WikiData nt. Adama Mickiewiecza wykonaj następujące zadania:
* Wyświetl miejsce urodzenia (place of birth) A. Mickiewicza.
* Oblicz ile lat żył A. Mickiewicz.
* Dodaj nowy klucz `place of death` o wartości `Istanbul`.
* Zamień wartość klucza `place of birth` na `Zaosie`.
* Dodaj nowy klucz `spouse`, a którego wartością niech będzie słownik `cecylia_data`.
* Wyświetl liczbę elementów listy, która znajduje się pod kluczem `occupation`.
* Wyświetl nazwiko żony A. Mickiewicza.
"""

data = {
    'name': 'Adam',
    'surname': 'Mickiewicz',
    'native language': 'polish',
    'year of birth': 1798,
    'place of birth': 'Zavosse',
    'year of death': 1855,
    'occupation': ['poet', 'professor', 'playwright']
}

cecylia_data = {
    'name': 'Cecylia',
    'surname': 'Szymanowska',
}

# * Wyświetl miejsce urodzenia (place of birth) A. Mickiewicza.
print(data['place of birth'])

# * Oblicz ile lat żył A. Mickiewicz.
print(data['year of death'] - data['year of birth'])

# * Dodaj nowy klucz `place of death` o wartości `Istanbul`.
data['place of death'] = 'Istanbul'

# * Zamień wartość klucza `place of birth` na `Zaosie`.
data['place of birth'] = 'Zaosie'

# * Dodaj nowy klucz `spouse`, a którego wartością niech będzie słownik `cecylia_data`.
data['spouse'] = cecylia_data

# * Wyświetl liczbę elementów listy, która znajduje się pod kluczem `occupation`.
print(len(data['occupation']))

# * Wyświetl nazwiko żony A. Mickiewicza.
print(data['spouse']['surname'])
