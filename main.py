from PyQt5.QtWidgets import QApplication
from giris_kod import giris

app = QApplication([])
window = giris()
window.show()
app.exec_()