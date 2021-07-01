from time import sleep
import pyautogui
import mouse
import keyboard
import asyncio
import sys, json, webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from mousesetting1 import Ui_MainWindow


class Ui_EnmvAddressSearch(object):

    def __init__(self):
        super().__init__()
        self.points = []
        self._counter = 0
        
    def setupUi(self, EnmvAddressSearch):
        EnmvAddressSearch.setObjectName("EnmvAddressSearch")
        EnmvAddressSearch.resize(500, 570)
        EnmvAddressSearch.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ENMV-1W.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EnmvAddressSearch.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(EnmvAddressSearch)
        self.centralwidget.setObjectName("centralwidget")
        self.AddressEnmv = QtWidgets.QLabel(self.centralwidget)
        self.AddressEnmv.setGeometry(QtCore.QRect(20, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AddressEnmv.setFont(font)
        self.AddressEnmv.setObjectName("AddressEnmv")
        self.FindAddress = QtWidgets.QPushButton(self.centralwidget)
        self.FindAddress.setGeometry(QtCore.QRect(150, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.FindAddress.setFont(font)
        self.FindAddress.setObjectName("FindAddress")
        self.StartAddress_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.StartAddress_1.setGeometry(QtCore.QRect(190, 40, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StartAddress_1.setFont(font)
        self.StartAddress_1.setMaximum(256)
        self.StartAddress_1.setProperty("value", 0)
        self.StartAddress_1.setObjectName("StartAddress_1")
        self.LastAddress_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.LastAddress_1.setGeometry(QtCore.QRect(190, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LastAddress_1.setFont(font)
        self.LastAddress_1.setMaximum(256)
        self.LastAddress_1.setProperty("value", 256)
        self.LastAddress_1.setObjectName("LastAddress_1")
        self.StartAddress = QtWidgets.QLabel(self.centralwidget)
        self.StartAddress.setGeometry(QtCore.QRect(10, 40, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.StartAddress.setFont(font)
        self.StartAddress.setObjectName("StartAddress")
        self.LastAddress = QtWidgets.QLabel(self.centralwidget)
        self.LastAddress.setGeometry(QtCore.QRect(10, 70, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LastAddress.setFont(font)
        self.LastAddress.setObjectName("LastAddress")
        self.SleepTime = QtWidgets.QLabel(self.centralwidget)
        self.SleepTime.setGeometry(QtCore.QRect(10, 10, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SleepTime.setFont(font)
        self.SleepTime.setObjectName("SleepTime")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(190, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox.setProperty("value", 1.15)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.AddressEnmv_1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.AddressEnmv_1.setGeometry(QtCore.QRect(150, 190, 64, 31))
        self.AddressEnmv_1.setObjectName("AddressEnmv_1")
        EnmvAddressSearch.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EnmvAddressSearch)
        self.statusbar.setObjectName("statusbar")
        EnmvAddressSearch.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(EnmvAddressSearch)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menuBar.setObjectName("menuBar")
        self.Setting_2 = QtWidgets.QMenu(self.menuBar)
        self.Setting_2.setObjectName("Setting_2")
        self.About = QtWidgets.QMenu(self.menuBar)
        self.About.setObjectName("About")
        EnmvAddressSearch.setMenuBar(self.menuBar)
        self.action_3 = QtWidgets.QAction(EnmvAddressSearch)
        self.action_3.setText("")
        self.action_3.setObjectName("action_3")
        self.MouseSetting = QtWidgets.QAction(EnmvAddressSearch)
        self.MouseSetting.setObjectName("MouseSetting")
        self.Certificate = QtWidgets.QAction(EnmvAddressSearch)
        self.Certificate.setObjectName("Certificate")
        self.Setting_2.addAction(self.MouseSetting)
        self.About.addAction(self.Certificate)
        self.menuBar.addAction(self.Setting_2.menuAction())
        self.menuBar.addAction(self.About.menuAction())
        self.retranslateUi(EnmvAddressSearch)
        QtCore.QMetaObject.connectSlotsByName(EnmvAddressSearch)
        if self.FindAddress.clicked.connect(self.buttonClicked):
            pass

    def retranslateUi(self, EnmvAddressSearch):
        _translate = QtCore.QCoreApplication.translate
        EnmvAddressSearch.setWindowTitle(_translate("EnmvAddressSearch", "ENMV Address Search"))
        self.AddressEnmv.setText(_translate("EnmvAddressSearch", "Адрес ЭНМВ - "))
        self.FindAddress.setText(_translate("EnmvAddressSearch", "Найти адрес"))
        self.StartAddress.setText(_translate("EnmvAddressSearch", "Начальный адрес -"))
        self.LastAddress.setText(_translate("EnmvAddressSearch", "Конечный адрес -"))
        self.SleepTime.setText(_translate("EnmvAddressSearch", "Время ожидания -"))
        self.Setting_2.setTitle(_translate("EnmvAddressSearch", "Настройки"))
        self.About.setTitle(_translate("EnmvAddressSearch", "О программе"))
        self.MouseSetting.setText(_translate("EnmvAddressSearch", "Положение курсора"))
        self.Certificate.setText(_translate("EnmvAddressSearch", "Справка"))

    def buttonClicked(self):
        with open("settingmouse.json", "r") as read_file:
            data = json.load(read_file)
            address = data['address']
            identificate = data['identificate']
            message = data['message']
        for i in range(self.StartAddress_1.value(), self.LastAddress_1.value() + 1):
            enmv = asyncio.run(find_adress(str(i), address, identificate, message, self.doubleSpinBox.value()))
            if enmv['color'] == 240:
                find_enmv = enmv['adress']
                self.AddressEnmv_1.display(find_enmv)
                break
            if enmv['button']:
                break

async def find_adress(adress_enmv, address, identification, message, findtime):
    with open("settingmouse.json", "r") as read_file:
        data = json.load(read_file)
        message = tuple(data['message'])
    key = await stop()
    pyautogui.click(address, clicks=2)
    pyautogui.typewrite(adress_enmv)
    pyautogui.click(identification)
    await asyncio.sleep(findtime)
    pixelColor = pyautogui.screenshot().getpixel((message))
    result = {'button': key, 'adress': adress_enmv, 'color': pixelColor[0]}
    return result

async def stop():
    key = keyboard.is_pressed('space')
    if key:
        return True
    else:
        return False


class AboutPorgram():
    pass


class MyInst(QtWidgets.QMainWindow, Ui_MainWindow):                          
    def __init__(self, parent=None):
        super(MyInst, self).__init__(parent)
        self.setupUi(self)
        

class Main1(QtWidgets.QMainWindow, Ui_EnmvAddressSearch):                           
    def __init__(self, parent=None):
        super(Main1 , self).__init__(parent)
        self.setupUi(self)
        self.MouseSetting.triggered.connect(self.set_mouse)
        self.Certificate.triggered.connect(self.set_certificate)

    def set_mouse(self):
        self.inst = MyInst()
        self.inst.show()

    def set_certificate(self):
        webbrowser.open('help.docx')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Main1()
    w.show()
    sys.exit(app.exec_())
