import pandas as pd
import os
import datetime
from DecisionTreeTahmin import tahminEt     # Gerekli
from Raporlama.Rapor import Rapor           # Gerekli
from UI.MainApp import App
from Util import Util
from Veriler.VeriIsleme import veriHazirla  # Gerekli

# Burası bir simulasyondur.
# Gerçekte veri kaynağı eşzamanlı
# olarak akan trafikten alınacantır.

path = os.getcwd()
veri = pd.read_csv(path + '/Veriler/RahatGor.csv')
X = veri.drop(columns=['outcome'])
X = veriHazirla(X)
trafik = X[:110]

tahminler = tahminEt(trafik)

rapor = Util.rapor

for tahmin in tahminler:
    if tahmin == 'normal.':
        pass
    else:

        rapor.log(tahmin, datetime.datetime.now())

rapor.raporla()
# print(rapor.logkayilaridict)
App()