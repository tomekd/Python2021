"""
Niech x oznacza liczbę uzyskanych punktów. Standardowa skala ocen jest następująca:
* x >= 90 -- 5.0
* 90 > x >= 80 -- 4.5
* 80 > x >= 70 -- 4.0
* 70 > x >= 60 -- 3.5
* 60 > x >= 50 -- 3.0
* x < 50 -- 2.0

Zmienna `points` zawiera liczbę uzyskanych punktów przez studenta.
Napisz instrukcję warunką, która wyświetli ocenę studenta w zależności od liczby punktów.
"""

points = 85

if points >= 90:
    print('5')
elif points >= 80:
    print('4.5')
elif points >= 70:
    print('4')
elif points >= 60:
    print('3.5')
elif points >= 50:
    print('3')
else:
    print('2')