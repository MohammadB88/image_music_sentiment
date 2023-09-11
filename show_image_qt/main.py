import sys

from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QWidget
from imagesite import Ui_Imagesite


class ShowImage(QWidget, Ui_Imagesite):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User data")
        
        # self.label = QLabel(self)
        # pixmap = QPixmap('happy_images/happy_guy.jpg')
        pixmap = QPixmap('sad_images/sad_man.jpg')
        # TODO: Write if Statement to cahnge between set of happy and sad images
        self.label.setPixmap(pixmap)

app = QtWidgets.QApplication(sys.argv)

window = ShowImage()
window.show()
app.exec()