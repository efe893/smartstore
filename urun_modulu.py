class Urun:
    def __init__(self, urun_id, isim, fiyat, stok):
        self.urun_id = urun_id
        self.isim = isim
        self.__fiyat = fiyat
        self.__stok = stok

    @property
    def fiyat(self):
        return self.__fiyat

    @fiyat.setter
    def fiyat(self, deger):
        if deger < 0:
            raise ValueError("Fiyat negatif olamaz!")
        self.__fiyat = deger

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, miktar):
        if miktar < 0:
            print("Uyarı: Stok yetersiz!")
        else:
            self.__stok = miktar

class Magaza:
    def __init__(self):
        self.urunler = [
            Urun("1", "Laptop", 25000, 10),
            Urun("2", "Mouse", 500, 50),
            Urun("3", "Klavye", 1200, 20)
        ]

    def urunleri_getir(self):
        return self.urunler