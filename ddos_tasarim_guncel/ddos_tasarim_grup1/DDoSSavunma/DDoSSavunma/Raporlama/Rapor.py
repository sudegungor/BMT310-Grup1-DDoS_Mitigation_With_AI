import pandas as pd
from datetime import datetime


class Rapor:
    logkayitlari = [['','','']]


    def raporla(self):
        pd.DataFrame(
            data=self.logkayitlari[1:],
            columns=['saldırı', 'gün', 'saat']).to_excel(
            f'Raporlar/rapor_{datetime.date(datetime.now())}.xlsx')

    def log(self, log, zaman: datetime):
        self.logkayitlari.append([log,
                                  datetime.date(zaman),
                                  datetime.time(zaman)])

