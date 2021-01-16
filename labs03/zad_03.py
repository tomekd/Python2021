"""
* Wczytaj za pomocą biblioteki pandas dane z https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
* Stwórz nowy DataFrame `features`, który nie będzie mieć kolumny `tip`.
* Przetwórz dane w następujący sposób:
 * kolumny ['smoker', 'sex'] powinny zostać zakodowane przy pomocy OrdinalEncoder
 * kolumny ['day', 'time'] powinny zostać przetworzone za pomocą OneHotEncoder
 * pozostałe cechy nie powinny ulec zmianie.
 * Sprawdź czy po przetworzeniu danych otrzymałeś same wartości liczbowe.
"""