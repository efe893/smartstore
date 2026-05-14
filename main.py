import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QListWidget, 
                             QMessageBox, QFrame)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

from urun_modulu import Magaza
from kullanici_modulu import Musteri

class SmartStoreArayuz(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SmartStore v1.0 - Premium Arayüz")
        self.setGeometry(100, 100, 650, 450)
        
        # Backend Bağlantıları
        self.magaza = Magaza()
        self.musteri = Musteri("ogrenci", "1234")
        
        self.init_ui()
        self.uygula_stil() # Modern tasarımı uygulayan fonksiyon

    def init_ui(self):
        # Ana Widget ve Yatay Layout (Sol ve Sağ bölme olarak ayırıyoruz)
        merkez_widget = QWidget()
        ana_layout = QHBoxLayout() 

        # --- SOL BÖLME: Ürün Listesi ---
        sol_layout = QVBoxLayout()
        
        baslik = QLabel("📦 Mağaza Ürünleri")
        baslik.setFont(QFont("Segoe UI", 14, QFont.Bold))
        sol_layout.addWidget(baslik)

        self.urun_listesi = QListWidget()
        self.guncelle_liste()
        sol_layout.addWidget(self.urun_listesi)

        # --- SAĞ BÖLME: Butonlar ve İşlemler ---
        sag_layout = QVBoxLayout()
        
        islem_baslik = QLabel("⚙️ İşlemler")
        islem_baslik.setFont(QFont("Segoe UI", 14, QFont.Bold))
        islem_baslik.setAlignment(Qt.AlignCenter)
        sag_layout.addWidget(islem_baslik)

        self.ekle_butonu = QPushButton("🛒 Sepete Ekle")
        self.ekle_butonu.setCursor(Qt.PointingHandCursor)
        self.ekle_butonu.clicked.connect(self.sepete_ekle_islem)
        sag_layout.addWidget(self.ekle_butonu)

        self.sepet_butonu = QPushButton("💳 Sepeti Onayla")
        self.sepet_butonu.setCursor(Qt.PointingHandCursor)
        self.sepet_butonu.clicked.connect(self.sepeti_goster)
        sag_layout.addWidget(self.sepet_butonu)
        
        # Görsel ayırıcı çizgi
        cizgi = QFrame()
        cizgi.setFrameShape(QFrame.HLine)
        cizgi.setFrameShadow(QFrame.Sunken)
        sag_layout.addWidget(cizgi)
        
        # Aktif kullanıcı bilgisi
        kullanici_bilgi = QLabel(f"👤 Aktif Kullanıcı:\n@{self.musteri.kullanici_adi}")
        kullanici_bilgi.setAlignment(Qt.AlignCenter)
        kullanici_bilgi.setObjectName("kullanici_etiketi") # CSS'te özel seçmek için
        sag_layout.addWidget(kullanici_bilgi)
        
        sag_layout.addStretch() # Elemanları yukarı yaslamak için boşluk ekler

        # Layoutları oranlayarak birleştir (Sol %65, Sağ %35 yer kaplar)
        ana_layout.addLayout(sol_layout, 2) 
        ana_layout.addLayout(sag_layout, 1) 

        merkez_widget.setLayout(ana_layout)
        self.setCentralWidget(merkez_widget)

    def uygula_stil(self):
        # QSS (Qt Style Sheets) ile gelişmiş arayüz giydirmesi
        stil = """
        QMainWindow {
            background-color: #f0f2f5;
        }
        QLabel {
            color: #2c3e50;
            padding-bottom: 5px;
        }
        #kullanici_etiketi {
            color: #7f8c8d;
            font-size: 12px;
            font-style: italic;
            margin-top: 20px;
        }
        QListWidget {
            background-color: #ffffff;
            border: 1px solid #d1d8e0;
            border-radius: 8px;
            padding: 5px;
            font-size: 14px;
            font-family: 'Segoe UI';
            color: #34495e;
        }
        QListWidget::item {
            padding: 12px;
            border-bottom: 1px solid #ecf0f1;
        }
        QListWidget::item:hover {
            background-color: #f7f9fa;
        }
        QListWidget::item:selected {
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            font-weight: bold;
        }
        QPushButton {
            background-color: #2ecc71;
            color: white;
            font-weight: bold;
            font-size: 14px;
            font-family: 'Segoe UI';
            padding: 12px;
            border-radius: 8px;
            border: none;
            margin-bottom: 10px;
        }
        QPushButton:hover {
            background-color: #27ae60;
        }
        QPushButton:pressed {
            background-color: #1e8449;
        }
        QPushButton:last-child {
            background-color: #e74c3c;
        }
        QPushButton:last-child:hover {
            background-color: #c0392b;
        }
        """
        self.setStyleSheet(stil)

    def guncelle_liste(self):
        self.urun_listesi.clear()
        for urun in self.magaza.urunleri_getir():
            self.urun_listesi.addItem(f"{urun.isim}   |   {urun.fiyat} TL   |   Stok: {urun.stok}")

    def sepete_ekle_islem(self):
        secili_indeks = self.urun_listesi.currentRow()
        if secili_indeks >= 0:
            urun = self.magaza.urunler[secili_indeks]
            if self.musteri.sepete_ekle(urun):
                QMessageBox.information(self, "İşlem Başarılı", f"✅ {urun.isim} sepete eklendi.")
                self.guncelle_liste()
            else:
                QMessageBox.warning(self, "Stok Hatası", "❌ Bu ürünün stoğu tükenmiş!")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen listeden bir ürün seçiniz!")

    def sepeti_goster(self):
        toplam = sum(u.fiyat for u in self.musteri.sepet)
        adet = len(self.musteri.sepet)
        
        mesaj = f"Sepetinizdeki Toplam Ürün: {adet} adet\n\n"
        mesaj += f"Ödenecek Toplam Tutar: {toplam} TL"
        
        kutu = QMessageBox()
        kutu.setWindowTitle("Sepet Özeti")
        kutu.setText(mesaj)
        kutu.setIcon(QMessageBox.Information)
        kutu.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion") # Windows'un eski tarzından kurtulup modern çizgilere geçer
    pencere = SmartStoreArayuz()
    pencere.show()
    sys.exit(app.exec_())