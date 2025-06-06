from PyQt5.QtWidgets import *
from giris import Ui_MainWindow
from _8_bit_code import _8bit
from _16_bit_code import _16bit
from _32_bit_code import _32bit

class giris(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.giris_ekran = Ui_MainWindow()
        self.giris_ekran.setupUi(self)
        self.bit8 = _8bit()
        self.bit16 = _16bit()
        self.bit32 = _32bit()
        self.giris_ekran.pushButton_8bit.clicked.connect(self.bit8_islem)
        self.giris_ekran.pushButton_16bit.clicked.connect(self.bit16_islem)
        self.giris_ekran.pushButton_32bit.clicked.connect(self.bit32_islem)

    def bit8_islem(self):
        self.close()
        self.bit8.show()
    def bit16_islem(self):
        self.close()
        self.bit16.show()
    def bit32_islem(self):
        self.close()
        self.bit32.show()