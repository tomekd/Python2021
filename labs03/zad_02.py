"""
Przerób poniższy kod, żeby korzystał z StandardScaler.
* Czy teraz model działa lepiej? Jeżeli tak, to o ile?
"""

from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

wine = load_wine()
train_x, test_x, train_y, test_y = train_test_split(wine.data, wine.target, test_size=0.2, random_state=0)
model = KNeighborsClassifier(5)
model.fit(train_x, train_y)

predictions = model.predict(test_x)
accuracy_score(predictions, test_y)
