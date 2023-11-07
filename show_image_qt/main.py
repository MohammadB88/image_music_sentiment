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
        
        self.pushButton_happy.clicked.connect(self.get_happy)
        # print(self.get_happy)
        self.pushButton_sad.clicked.connect(self.get_sad)
        # print(self.get_sad)
        
        # print(self.pushButton_happy.text())
        # print(self.pushButton_sad.text())
        
    # TODO set API for each of these emotions to get the image
    # TODO WORK with APIs and then rewrite the app in microservices
    def get_happy(self):
        pixmap = QPixmap('happy_images/happy_guy.jpg')
        self.label.setPixmap(pixmap)
    
    def get_sad(self):
        pixmap = QPixmap("sad_images/sad_man.jpg")
        self.label.setPixmap(pixmap)
        

    #  TODO SETUP the English Teacher with QT Designer and API call to OpenAI

    # def sad_or_happy(self, emotion="sad"):
    #     if emotion == "happy":
    #         pixmap = QPixmap('happy_images/happy_guy.jpg')
    #         self.label.setPixmap(self.pixmap)
    #     elif emotion == "sad":
    #         pixmap = QPixmap("sad_images/sad_man.jpg")
    #         self.label.setPixmap(self.pixmap)
    #     else: 
    #         return "Please specify your emotions!!!"

app = QtWidgets.QApplication(sys.argv)

window = ShowImage()
window.show()
app.exec()