from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from database import DatabaseConnect
from server import ServerConnect

# QtDesigner sahifalarini import qilish
from ui_pyfiles.main import Ui_MainWindow as Ui_MainWindow
from ui_pyfiles.edit import Ui_Frame as Ui_EditFrame
from ui_pyfiles.login import Ui_Frame as Ui_LoginFrame



# Databasega bog'lanish
database = DatabaseConnect()

# Serverga bog'lanish
server = ServerConnect()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(MainWindow)

# Sahifalarni activlashtirish
EditFrame = QtWidgets.QFrame()
edit_ui = Ui_EditFrame()
edit_ui.setupUi(EditFrame)
# EditFrame.show()

LoginFrame = QtWidgets.QFrame()
login_ui = Ui_LoginFrame()
login_ui.setupUi(LoginFrame)
# LoginFrame.show()

# Bosh sahifaga o'tkazuvchi funksiya
def show_home_page():
    ui.admins_button_2.setStyleSheet("""
        background-color: rgb(50, 100, 200);
        color: rgb(0,255,0);
        text-align:  center;""")
    ui.admins_button.setStyleSheet("")
    ui.hisob_button.setStyleSheet("")
    ui.stackedWidget.setCurrentIndex(1)
ui.admins_button_2.clicked.connect(show_home_page)

# Profile sahifasiga o'tkazuvchi funksiya
def show_profile_page():
    ui.hisob_button.setStyleSheet("""
        background-color: rgb(50, 100, 200);
        color: rgb(0,255,0);
        text-align:  center;""")
    ui.admins_button_2.setStyleSheet("")
    ui.admins_button.setStyleSheet("")
    ui.stackedWidget.setCurrentIndex(0)
ui.hisob_button.clicked.connect(show_profile_page)

# Data sahifasiga o'tkazuvchi funksiya
def show_data_page():
    ui.admins_button.setStyleSheet("""
        background-color: rgb(50, 100, 200);
        color: rgb(0,255,0);
        text-align:  center;""")
    ui.admins_button_2.setStyleSheet("")
    ui.hisob_button.setStyleSheet("")
    ui.stackedWidget.setCurrentIndex(2)
ui.admins_button.clicked.connect(show_data_page)

# Login uchun code olish funksiyasi
def get_login_code():
    username = login_ui.lineEdit.text().strip()
    password = login_ui.lineEdit_2.text().strip()
    try:
        server.get_login(username, password)
    except:
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Username yoki parol xato")
        msg.setInformativeText("ProjectsPlatforms.uz saytidan ruyxatdan o'tgan akkountingizga kirishingiz kerak.")
        msg.setWindowTitle("Xatolik!")
        msg.exec_()

# Login funksiyasi
def login_func():
    username = login_ui.lineEdit.text().strip()
    password = login_ui.lineEdit_2.text().strip()
    kod = login_ui.lineEdit_3.text().strip()
    try:
        token = server.login(username, password, int(kod))["token"]

        LoginFrame.close()
        MainWindow.show()
    except:
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Kod xato kiritildi")
        msg.setInformativeText("Telegram botdan kelgan 6 belgili kodni kiritishingiz kerak")
        msg.setWindowTitle("Xatolik!")
        msg.exec_()

# tugmalarga ulash
login_ui.pushButton_2.clicked.connect(get_login_code)
login_ui.pushButton.clicked.connect(login_func)






if __name__ == "__main__":
    if database.isLogined():
        MainWindow.showMaximized()
    else:
        LoginFrame.show()
    sys.exit(app.exec_())