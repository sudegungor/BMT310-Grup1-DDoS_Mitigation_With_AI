from sklearn.metrics import accuracy_score

def dogruluguTestEt(y_true, y_pred):
    acc = accuracy_score(y_true=y_true, y_pred=y_pred)
    print('Doğruluk oranı'.upper().center(50,'*'))
    print('{:.4f}'.format(acc))