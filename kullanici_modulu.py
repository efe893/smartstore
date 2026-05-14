class Kullanici:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.__sifre = sifre

    @property
    def sifre(self):
        return "*" * len(self.__sifre)  # Şifreyi gizli tutma örneği

    def kontrol_et(self, k_adi, sifre):
        return self.kullanici_adi == k_adi and self.__sifre == sifre

class Musteri(Kullanici):
    def __init__(self, kullanici_adi, sifre):
        super().__init__(kullanici_adi, sifre)
        self.sepet = []

    def sepete_ekle(self, urun):
        if urun.stok > 0:
            self.sepet.append(urun)
            urun.stok -= 1
            return True
        return False