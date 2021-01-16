
"""
* Zainstaluj biblioteki pandas i scikit-learn, o ile ich nie masz.
* Sprawdź wszystkie k od 1 do 50 w modelu k-najbliższych sąsiadów dla poniższego zadania.
"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data = datasets.load_iris()


features = pd.DataFrame(data['data'], columns=data['feature_names'])
labels = pd.Series(data['target'])

features.head()

train_x, test_x, train_y, test_y = train_test_split(features, labels, test_size=0.33, random_state=0)

model = KNeighborsClassifier(5)
model.fit(train_x, train_y)

predictions = model.predict(test_x)
accuracy_score(predictions, test_y)
