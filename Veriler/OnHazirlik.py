from sklearn import preprocessing
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


veriler = pd.read_csv('RahatGor.csv')

# with open('verilerinAciklamasi.txt', 'w') as file:
#     file.write(str(veriler.describe(include = 'all')))

def donustur(data, index):
    oneHotEncoder = preprocessing.OneHotEncoder()
    # kategorik veriden sayısal bir ifadeye geçmek için one hot encoder kullanıyorum
    tmp = data.iloc[:, index].values  # ilgili kolonu alıyorum

    print(tmp[:10], type(tmp))

    tmp = oneHotEncoder.fit_transform(tmp.reshape((-1, 1))).toarray()
    columnNames = oneHotEncoder.get_feature_names()
    tmp = pd.DataFrame(data=tmp, columns=columnNames)
    return pd.concat([tmp, data.drop(columns=[data.columns[index]])], axis=1)
    #print(data.columns)



Y = veriler['outcome']
y = veriler.values # Seriden --> numpy dizisine çeviriyorum
X = veriler.drop(columns=['outcome']) # --> Y ulaşmak istediğimiz sonuç X ise parametrelerimiz
x = veriler.values

print(X.shape) # (4940, 42)
print(Y.shape) # (4940,)

X = donustur(X,X.columns.get_loc('service'))
X = donustur(X,X.columns.get_loc('protocol_type'))
X = donustur(X,X.columns.get_loc('flag'))

print(len(X.columns))
print('x:', len(X), ' Y: ', len(Y)) # x: 4940  Y:  4940 farklı olmasını beklemiyorduk zaten
Y = pd.DataFrame(data = Y.values, columns=['outcome'])
X = pd.concat([X,Y], axis=1)
X.to_csv('BakalımOlmusMu.csv')









'''
        ONE HOT ENCODER BU İŞE YARIYOR

['icmp' 'icmp' 'tcp' 'icmp' 'icmp' 'tcp' 'icmp' 'icmp' 'tcp' 'icmp'] 
                                 |
                                 |
                                 |
                                 |
                                 V
                            [[1. 0. 0.]
                             [1. 0. 0.]
                             [0. 1. 0.]
                             [1. 0. 0.]
                             [1. 0. 0.]
                             [0. 1. 0.]
                             [1. 0. 0.]
                             [1. 0. 0.]
                             [0. 1. 0.]
                             [1. 0. 0.]]

BURADAN ŞUNU ANLIYORUZ --> KOLON BAŞLIKLARIMIZ [icmp,tcp,udp] 

(udp burada çıkmamış 33. satıra kadar veriyi almış olsaydık onu da görecektik.)

'''