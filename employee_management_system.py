class Personel:
    
    personel_sayisi = 0
    zam_orani = 1.05
    
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.eposta = f'{isim.lower()}.{soyisim.lower()}@firmam.com'
        
        Personel.personel_sayisi += 1
    
    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'
    
    def zam_uygula(self):
        self.maas = int(self.maas *self.zam_orani)
    
    @classmethod
    def zam_orani_belirle(cls, oran):
        eski_oran = cls.zaman_orani
        cls.zam_orani = oran    
        print(f'Eski zam oran ({eski_oran}) güncellndi. Yeni oran: {cls.zam_orani}')
        
    @classmethod
    def from_string(cls, per_str):
        isim, soyisim, maas = per_str.split('-')
        return cls(isim, soyisim, maas) 
    
    @staticmethod
    def mesai_gunu(gun):
        if gun.weekday == 5 or gun.weekday() == 6:
            return 'Hafta Sonu'
        else:
            return 'Hafta İçi'
 
 #Method Resolution Order  kalıtım zinciri       
class Yazilimci(Personel):
    zam_orani = 1.1                 

    def __init__(self, isim, soyisim, maas, prog_dili):
        super().__init__(isim, soyisim, maas)
        self.prog_dili = prog_dili
        # print(f'Yeni personel yazilimci kategorisine tasindi: {self.isim} {self.soyisim}')

class Mudur(Personel):
    
    def __init__(self, isim, soyisim, maas, personeller = None):
        super().__init__(isim, soyisim, maas)
        if personeller is None:
            self.personeller = []
        else:    
            self.personeller = personeller
    
    def personel_ekle(self, per):
        if per not in self.personeller:
            self.personeller.append(per)    
    
    def personel_cikar(self, per):
        if per in self.personeller:
            self.personeller.remove(per)
            
    def personelleri_listele(self):
        for e, per in enumerate(self.personeller):
            e += 1
            print(e, per.tam_isim())
                        



yaz_1 = Yazilimci('John', 'Smith', 30000, 'Python')
yaz_2 = Yazilimci('Mary', 'Smith', 35000, 'Java')
yaz_3 = Yazilimci('Test', 'User', 1000, 'C')

mdr_1 = Mudur('John', 'Wick', 50000, [yaz_1, yaz_2])
mdr_2 = Mudur('John', 'Snow', 50000, [yaz_1, yaz_2])




