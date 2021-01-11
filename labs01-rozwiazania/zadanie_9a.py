"""
Zadania: Zaimportuj bibliotekę statistics, która zawiera funckje do obliczenia podstawych wielkości statystycznych (średnia, mediana, moda):
    statistics.mean -- obliczenie średniej
    statistics.median -- obliczenie mediany
    statistics.variance -- obliczenie wariancji
    statistics.stdev -- obliczenie odchylenia standardowego Oblicz te wielkości dla wartości z poniższego słownika.
Każda z tych funkcji przyjmuje jeden argument: listę wartości.
"""

members = {
    'April': 211819,
    'May': 682758,
    'June': 737011,
    'July': 779511,
    'August': 673790,
    'September': 673790,
    'October': 444177,
    'November': 136791,
}

import statistics

# statistics.mean -- obliczenie średniej
print(statistics.mean(members.values()))

# statistics.median -- obliczenie mediany
print(statistics.median(members.values()))

# statistics.variance -- obliczenie wariancji
print(statistics.variance(members.values()))

# statistics.stdev -- obliczenie odchylenia standardowego
print(statistics.stdev(members.values()))
