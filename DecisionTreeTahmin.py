from sklearn import tree
from matplotlib import pyplot as plt
from Veriler.VerileriGetir import setiBol
from DogrulukTesti.Dogruluk import dogruluguTestEt
from sklearn.metrics import plot_confusion_matrix, confusion_matrix

x_train, x_test, y_train, y_test = setiBol()
dt = tree.DecisionTreeClassifier() # MAX depth

# Karar ağacını eğtiyoruz.
dt.fit(x_train,y_train)

# Karar ağacı test verisiyle tahmin sonuçları üretiyor.
pred = dt.predict(x_test)

cm = confusion_matrix(y_pred=pred, y_true=y_test)
print(cm)
dogruluguTestEt(y_true=y_test, y_pred = pred)

plot_confusion_matrix(dt, x_test, y_test)
plt.show()
