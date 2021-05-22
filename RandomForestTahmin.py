from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
import pandas as pd
from DogrulukTesti.Dogruluk import dogruluguTestEt
from Veriler.VeriIsleme import veriHazirla
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from Veriler.VerileriGetir import setiBol

X_train, X_test, y_train, y_test = setiBol()

classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)


def basari():
    basliklar = np.unique(y_test)
    pred = classifier.predict(X_test)  # tahminleri oluşturuyorum.
    cm = confusion_matrix(pred, y_test, labels=basliklar)
    print(pd.DataFrame(data=cm, index=basliklar, columns=basliklar))

    # confusion matrisini (doğruluk matrisini göstermek için kullanıyorum)

    dogruluguTestEt(y_true=y_test, y_pred=pred)

    plot_confusion_matrix(classifier, X_test, y_test)
    plt.show()
    # grafik.veriyiGorsellestir(y_test,pred)

def tahminEt(x):
    x = veriHazirla(x)
    return classifier.predict(x)