"""
Dane w pliku gapminder.csv zawierają podstawowe informacje  o kilku czynnikich (PKB, dzietność, itp) dla 175 krajów.
Celem tego zadania jest wytrenowanie modelu, który przewidzi oczekiwaną długość życia w zaleźności od pozostałych zmiennych.

* Wczytaj dane z pliku gapminder.csv
* Ustaw jako cechy wszystkie kolumny o wartościach numerycznych z wyłączeniem `life_expectancy`.
* Przetwórz kolumny ['population', 'gdp'] za pomocą funkcji np.log. Użyj do tego transformera FunctionTransformer
( FunctionTransformer(np.log) )
* Stwórz pipeline składający się z powyższego transformera i modelu regresji liniowej.
* Wytrenuj model.
* Wyświetl atrybuty modelu: `coef_` i  `intercept_`.

"""

import numpy as np
from sklearn.preprocessing import FunctionTransformer
from sklearn.linear_model import LinearRegression

