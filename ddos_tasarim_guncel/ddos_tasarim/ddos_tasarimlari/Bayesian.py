from sklearn.naive_bayes import GaussianNB

from Veriler.VeriIsleme import veriHazirla
from Veriler.VerileriGetir import setiBol

X_train, X_test, y_train, y_test = setiBol()

naifBayes = GaussianNB()
naifBayes.fit(X_train, y_train)

def tahminEt(X):
    X = veriHazirla(X)
    return naifBayes.predict(X)