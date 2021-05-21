import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

from Veriler.VeriIsleme import veriHazirla
from Veriler.VerileriGetir import setiBol

X_train, X_test, y_train, y_test = setiBol()

knn = KNeighborsClassifier(n_neighbors=3)  # n_neighbors=5 --> varsayılan değer

knn.fit(X_train, y_train)
print('Xtrain Kolonları: ', X_train.columns)
def tahminEt(x):
    x = veriHazirla(x)
    print('Tahminin Kolonları',x.columns)
    return knn.predict(x)
