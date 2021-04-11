# BMT310-Grup1-DDoS_Mitigation_With_AI
BMT310-Grup1-DDoS_Mitigation_With_AI

![](https://www.flowmon.com/CMSPages/GetFile.aspx?guid=4cec8e92-4689-4529-8fb7-5737d8b7340c&maxsidesize=2500)
## YAPAY ZEKA
### Kdd99 Veri Seti İnceleme ve Ön İşleme

Bu alanda alt problemimiz ise ddos saldırılarını sınıflandırmak.

Öğrenme algoritmaları büyük verileri işleyerek ilerde karşılaşacakları örneklerin çıktılarını tahmin etmeye çalışırlar.
bu tahmini matematiksel işlemlerle yaparlar. Dolayısıyla, verilerin algoritmalar tarafından anlaşılır olması 
için sayısal veri olması gerekir.
 

Kdd99 veri setinde 3 kolon kategorik veri içeriyor bunlar:<br/>
protocol_type,<br/>
flag,<br/>
service<br/>
Bu kolonları sayısal verilere çeviriyoruz.

#### Örnek olarak
![](KategorikVeriler.png)

### Tahminler

<hr/>

#### Decision tree

##### Doğruluk matrisi (confusion matrix)

![](Plotlar/DecisionTreeConfMat.png)

#### DOĞRULUK ORANI
0.9951

#### KNN k nearest neighbors

##### Doğruluk matrisi (confusion matrix)

![](Plotlar/KnnConfMat.png)

##### DOĞRULUK ORANI
0.9755

## TASARIM



## SAVUNMA