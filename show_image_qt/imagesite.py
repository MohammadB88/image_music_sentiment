# Form implementation generated from reading ui file 'showimage.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Imagesite(object):
    def setupUi(self, Imagesite):
        Imagesite.setObjectName("Imagesite")
        Imagesite.resize(591, 494)
        self.line = QtWidgets.QFrame(parent=Imagesite)
        self.line.setGeometry(QtCore.QRect(170, 60, 20, 351))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Imagesite)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 90, 251, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("happy_images/happy_kid.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(parent=Imagesite)
        self.widget.setGeometry(QtCore.QRect(50, 170, 77, 56))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_pos = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_pos.setObjectName("pushButton_pos")
        self.verticalLayout.addWidget(self.pushButton_pos)
        self.pushButton_neg = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_neg.setObjectName("pushButton_neg")
        self.verticalLayout.addWidget(self.pushButton_neg)

        self.retranslateUi(Imagesite)
        self.pushButton_pos.clicked.connect(self.pushButton_pos.deleteLater) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Imagesite)

    def retranslateUi(self, Imagesite):
        _translate = QtCore.QCoreApplication.translate
        Imagesite.setWindowTitle(_translate("Imagesite", "imagesite"))
        self.pushButton_pos.setText(_translate("Imagesite", "Positive"))
        self.pushButton_neg.setText(_translate("Imagesite", "Negative"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Imagesite = QtWidgets.QWidget()
#     ui = Ui_Imagesite()
#     ui.setupUi(Imagesite)
#     Imagesite.show()
#     sys.exit(app.exec())