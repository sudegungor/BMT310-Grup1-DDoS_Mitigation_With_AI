import pandas as pd
import os

from DecisionTreeTahmin import tahminEt
from Veriler.VeriIsleme import veriHazirla

# Burası bir simulasyondur.
# Gerçekte veri kaynağı eşzamanlı
# olarak akan trafikten alınacantır.

path = os.getcwd()
veri = pd.read_csv(path + '/Veriler/RahatGor.csv')
X = veri.drop(columns=['outcome'])
X = veriHazirla(X)
tmp = X[19:20]

tahmin = tahminEt(tmp)
print(tahmin)
