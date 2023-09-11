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
        # emotion_image = self.sad_or_happy("sad")
        # pixmap = QPixmap(emotion_image)
        # TODO: Write if Statement to cahnge between set of happy and sad images
        
        self.pushButton_pos.clicked.connect(self.update_label)
        # self.label.setPixmap(self.pixmap)

    def sad_or_happy(self, emotion):
        if emotion == "happy":
            return 'happy_images/happy_guy.jpg'
        elif emotion == "sad":
            return "sad_images/sad_man.jpg"
        else: 
            return "Please specify your emotions!!!"

    def update_label(self):
        print("changing the image")
        emotion_image = self.sad_or_happy("sad")
        pixmap = QPixmap(emotion_image)
        self.label.setPixmap(pixmap)

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