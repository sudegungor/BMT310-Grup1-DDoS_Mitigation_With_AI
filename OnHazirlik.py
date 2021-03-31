from sklearn import preprocessing
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
veriler = pd.read_csv('RahatGor.csv')

# with open('verilerinAciklamasi.txt', 'w') as file:
#     file.write(str(veriler.describe(include = 'all')))


Y = veriler['outcome']
y = veriler.values # Seriden --> numpy dizisine çeviriyorum
X = veriler.drop(columns=['outcome']) # --> Y ulaşmak istediğimiz sonuç X ise parametrelerimiz
x = veriler.values

print(X.shape) # (4940, 42)
print(Y.shape) # (4940,)

oneHotEncoder = preprocessing.OneHotEncoder()
# kategorik veriden sayısal bir ifadeye geçmek için one hot encoder kullanıyorum
tmp = X.iloc[:,2].values # ilgili kolonu alıyorum

print(tmp[:10], type(tmp))

tmp = oneHotEncoder.fit_transform(tmp.reshape((-1,1))).toarray()

print(tmp[:10])

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
print(X)