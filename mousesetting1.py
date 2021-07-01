import keyboard
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import pyautogui
import mouse
import keyboard
import asyncio
import sys, json
import os.path


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self._counter = 0
        self.data_setting = {}
        if os.path.exists('settingmouse.json'):
            with open("settingmouse.json", "r") as read_file:
                data = json.load(read_file)
                self.ADRESS = data['address']
                self.IDENTIFICATION = data['identificate']
                self.MESSAGE = data['message']
        else:
            self.ADRESS = (0, 0)
            self.IDENTIFICATION = (0, 0)
            self.MESSAGE = (0, 0)
            data = {'address': self.ADRESS, 'identificate': self.IDENTIFICATION, 'message': self.MESSAGE}
            with open("settingmouse.json", "w") as write_file:
                json.dump(data, write_file) 
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(303, 294)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/pngtr.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.message = QtWidgets.QLabel(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(20, 150, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.message.setFont(font)
        self.message.setObjectName("message")
        self.text2 = QtWidgets.QLabel(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(40, 40, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text2.setFont(font)
        self.text2.setObjectName("text2")
        self.message_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.message_1.setGeometry(QtCore.QRect(120, 150, 113, 20))
        self.message_1.setReadOnly(True)
        self.message_1.setObjectName("message_1")
        self.identificate = QtWidgets.QLabel(self.centralwidget)
        self.identificate.setGeometry(QtCore.QRect(20, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.identificate.setFont(font)
        self.identificate.setObjectName("identificate")
        self.address = QtWidgets.QLabel(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(20, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.address.setFont(font)
        self.address.setObjectName("address")
        self.text1 = QtWidgets.QLabel(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(20, 20, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text1.setFont(font)
        self.text1.setObjectName("text1")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setGeometry(QtCore.QRect(70, 210, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonCancel = QtWidgets.QPushButton("Cancel")
        self.buttonOk = QtWidgets.QPushButton("Ok")
        self.buttonBox.addButton(self.buttonCancel, QtWidgets.QDialogButtonBox.RejectRole)
        self.buttonBox.addButton(self.buttonOk, QtWidgets.QDialogButtonBox.ActionRole)
        self.identificate_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.identificate_1.setGeometry(QtCore.QRect(160, 120, 113, 20))
        self.identificate_1.setReadOnly(True)
        self.identificate_1.setObjectName("identificate_1")
        self.address_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.address_1.setGeometry(QtCore.QRect(80, 90, 113, 20))
        self.address_1.setReadOnly(True)
        self.address_1.setObjectName("address_1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 303, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        if os.path.exists('settingmouse.json'):
            with open("settingmouse.json", "r") as read_file:
                data = json.load(read_file)
                self.address_1.setText(str(data['address']))
                self.identificate_1.setText(str(data['identificate']))
                self.message_1.setText(str(data['message']))
        self.buttonOk.clicked.connect(lambda: self.savesetting())
        self.buttonCancel.clicked.connect(lambda: self.close())

    def savesetting(self):
        with open("settingmouse.json", "w") as write_file:
            json.dump(self.data_setting, write_file)
        self.close()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            self._counter += 1
        event.accept()
        x = pyautogui.position()[0]
        y = pyautogui.position()[1]
        if self._counter == 1:
            self.ADRESS = (x, y)
            self.address_1.setText(str(self.ADRESS))
        elif self._counter == 2:
            self.IDENTIFICATION = (x, y)
            self.identificate_1.setText(str(self.IDENTIFICATION))
        elif self._counter == 3:
            self.MESSAGE = (x, y)
            self.message_1.setText(str(self.MESSAGE))
            self.data_setting = {'address': self.ADRESS, 'identificate': self.IDENTIFICATION, 'message': self.MESSAGE}

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.message.setText(_translate("MainWindow", "Сообщение -"))
        self.text2.setText(_translate("MainWindow", "элементы и нажмите пробел"))
        self.identificate.setText(_translate("MainWindow", "Идентификация -"))
        self.address.setText(_translate("MainWindow", "Адрес -"))
        self.text1.setText(_translate("MainWindow", "Наведите указатель на следующие")) 
    
# if __name__ == "__main__": 
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
