# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kundalik_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(599, 599)
        Frame.setStyleSheet("\n"
"background-color: white;\n"
"color: white;\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setMaximumSize(QtCore.QSize(500, 550))
        self.frame.setStyleSheet("color: black;\n"
"font-size: 30px;\n"
"font-family: \"Mongolian Baiti\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(500, 130))
        self.label.setMaximumSize(QtCore.QSize(500, 130))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/kundalik_kom.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"font-size: 20px;\n"
"color: blue;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(0,0,0,80);\n"
"background-color: rgba(0, 0, 0, 10);\n"
"padding: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"border-color: blue;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(0,0,0,80);\n"
"background-color: rgba(0, 0, 0, 10);\n"
"padding: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"border-color: blue;\n"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setStyleSheet("font-size: 20px;\n"
"color: red;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"color: white;\n"
"border: 1px solid rgb(0,0,0,80);\n"
"padding: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(175, 214, 82, 255), stop:1 rgba(109, 182, 46, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(175, 214, 82, 255), stop:1 rgba(109, 182, 46, 255));\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Maktabni kiritish"))
        self.label_6.setText(_translate("Frame", "Maktab administratori yoki biror bir o\'qituvchining kundalik.com dagi hisobiga login qilishingiz kerak"))
        self.label_2.setText(_translate("Frame", "  Login"))
        self.label_3.setText(_translate("Frame", "  Parol"))
        self.pushButton.setText(_translate("Frame", "Tizimga kirish"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
