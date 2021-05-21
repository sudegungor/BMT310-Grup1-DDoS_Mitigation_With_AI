import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

from DogrulukTesti.Dogruluk import dogruluguTestEt
from Veriler.OnHazirlik import veriHazirla
from Gorsellestir import Grafik as grafik
from Veriler.VerileriGetir import setiBol

X_train, X_test, y_train, y_test = setiBol()

knn = KNeighborsClassifier(n_neighbors=3)  # n_neighbors=5 --> varsayılan değer

knn.fit(X_train, y_train)

def basari():
    basliklar = np.unique(y_test)
    pred = knn.predict(X_test)  # tahminleri oluşturuyorum.
    cm = confusion_matrix(pred, y_test, labels=basliklar)
    print(pd.DataFrame(data=cm, index=basliklar, columns=basliklar))

    # confusion matrisini (doğruluk matrisini göstermek için kullanıyorum)

    dogruluguTestEt(y_true=y_test, y_pred=pred)

    plot_confusion_matrix(knn, X_test, y_test)
    plt.show()
    # grafik.veriyiGorsellestir(y_test,pred)


def tahminEt(x):
    x = veriHazirla(x)
    return knn.predict(x)
