class Personel:
    """
    bu sinifi kullanarak...
    bu sinifin içindeki fonk tam_isim()
    """
    personel_sayisi = 0
    
    
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.__zam_orani = 1.05  # PRIVATE  dışardan erişilmez
        Personel.personel_sayisi += 1
    
    @property
    def eposta(self):
        return f'{self.isim.lower()}.{self.soyisim.lower()}@firmam.com'
    
    @property
    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'
   
    @tam_isim.setter
    def tam_isim(self, ad):
        isim, soyisim = ad.split(' ')
        self.isim = isim
        self.soyisim = soyisim
    
    @tam_isim.deleter
    def tam_isim(self):
        print('DEGİSKENLER SİLİNDİ!!!!!')
        self.isim = None
        self.soyisim = None       
    
    def getZamOrani(self):
        return self.__zam_orani     
    
    def zam_uygula(self):
        self.maas = int(self.maas * self.__zam_orani)
    
    def __repr__(self):
        return f"Personel('{self.isim}', '{self.soyisim}', {self.maas})"
    
    def __str__(self):
        return f'{self.tam_isim} - {self.eposta}'
    
    def __add__(self, other):
        return self.maas + other.maas
    
    def __len__(self):
        return len(self.tam_isim)
    
    @classmethod
    def zam_orani_belirle(cls, oran):
        eski_oran = cls.zam_orani
        cls.zam_orani = oran    
        print(f'Eski zam oran ({eski_oran}) güncellendi. Yeni oran: {cls.zam_orani}')
        
    @classmethod
    def from_string(cls, per_str):
        isim, soyisim, maas = per_str.split('-')
        return cls(isim, soyisim, maas) 
    
    @staticmethod
    def mesai_gunu(gun):
        if gun.weekday() == 5 or gun.weekday() == 6:
            return 'Hafta Sonu'
        else:
            return 'Hafta İçi'


class Yazilimci(Personel):
    zam_orani = 1.1                 

    def __init__(self, isim, soyisim, maas, prog_dili):
        super().__init__(isim, soyisim, maas)
        self.prog_dili = prog_dili


class Mudur(Personel):
    
    def __init__(self, isim, soyisim, maas, personeller=None):
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
        for e, per in enumerate(self.personeller, start=1):
            print(e, per.tam_isim)


per1 = Personel('Lucifer', 'Michaelson', 10000)
per2 = Personel('Luci', 'Michael', 20000)



yaz_1 = Yazilimci('John', 'Smith', 30000, 'Python')
yaz_2 = Yazilimci('Mary', 'Smith', 35000, 'Java')
yaz_3 = Yazilimci('Test', 'User', 1000, 'C')
yaz_4 = Yazilimci('Emir', 'Turan',125000, 'C') 
mdr_1 = Mudur('John', 'Wick', 50000, [yaz_1, yaz_2])
mdr_2 = Mudur('John', 'Snow', 50000, [yaz_1, yaz_2])



yaz_4.zam_orani_belirle(12.4)
yaz_4.zam_uygula()
print(yaz_4.maas)
