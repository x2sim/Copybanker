import sys
import win32clipboard
from PyQt5 import QtWidgets, QtCore
from  PyQt5.QtWidgets import QPushButton
from  PyQt5.QtCore import *

class QMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(QMain, self).__init__()
        self.X_START = 20
        self.Y_STEP = 45
        self.y_current = 0
        self.quanity_buttons = 8

        self.button_clear = QPushButton(self)
        self.button_clear.setGeometry(QtCore.QRect(195, 20, 30, 30))
        self.button_clear.setText('&X')
        self.button_clear.setStyleSheet("background-color:#6DAC70;color:black;" "font: 75 8pt \"Times New Roman\";")

        self.button_clear_line = QPushButton(self)
        self.button_clear_line.setGeometry(QtCore.QRect(195, 390, 30, 30))
        self.button_clear_line.setText('&clear')
        self.button_clear_line.setStyleSheet("background-color:#6DAC70;color:black;" "font: 75 8pt \"Times New Roman\";")

        self.verticalSlider = QtWidgets.QSlider(self)
        self.verticalSlider.setGeometry(QtCore.QRect(200, 60, 22, 315))
        self.verticalSlider.setStyleSheet("#946B89")
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(20, 390, 150, 30))
        self.lineEdit.setStyleSheet("background-color:#C4DEC5;color:black;" )
        self.lineEdit.setObjectName("lineEdit")

        self.name=['']*self.quanity_buttons
        self.buffer_name = ['']*self.quanity_buttons
        self.buttons=[]

        for item_button in range(self.quanity_buttons):
            button_for_copy = QPushButton(self)
            button_for_copy.setStyleSheet("background-color:#828282;color:black;" "font: 75 12pt \"Times New Roman\";")
            self.calculate()
            button_for_copy.setGeometry(QtCore.QRect(self.X_START, self.y_current, 150, 35))
            button_for_copy.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.buttons.append(button_for_copy)
        self.setStyleSheet("background-color:#6D89AC")
        self.init_ui()
        
    def init_ui(self):
        for item_button in range(self.quanity_buttons):
            self.buttons[item_button].clicked.connect(self.add_text)
            self.buttons[item_button].installEventFilter(self)
            self.buttons[item_button].customContextMenuRequested.connect(self.copy_to_clipboard)

        self.button_clear_line.clicked.connect(self.clear_line)
        self.button_clear.clicked.connect(self.clear_all)
        self.verticalSlider.valueChanged.connect(self.make_opacity)
        self.setFixedSize(250,450)
        self.setWindowTitle('copybanker')

    def copy_to_clipboard(self):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(self.name[self.buttons.index(self.sender())])
        win32clipboard.CloseClipboard()

    def clear_all(self):
        for item_button in range(self.quanity_buttons):
            self.buttons[item_button].setText('')
            self.name[item_button]=''
            self.buffer_name[item_button]=''
            self.lineEdit.setText('')

    def add_text(self):
        if self.lineEdit.text()=='':
            win32clipboard.OpenClipboard()
            dat = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            self.name[self.buttons.index(self.sender())] = dat

        else:
            self.buffer_name[self.buttons.index(self.sender())]=self.lineEdit.text()
            self.sender().setText(self.lineEdit.text())

    def clear_line(self):
        self.lineEdit.setText('')

    def make_opacity(self,value):
        self.setWindowOpacity((100-value)/100)

    def calculate(self):
        if self.y_current == 0:
            self.y_current = 20
        else:
            self.y_current += self.Y_STEP

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            index_button = self.buttons.index(object)
            self.buffer_name[index_button] = object.text()
            self.buttons[index_button].setText(self.name[index_button])
            return True
        elif event.type() == QEvent.Leave:
            index_button = self.buttons.index(object)
            object.setText(self.buffer_name[index_button])
        return False

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    game = QMain()
    game.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
    game.show()
    sys.exit(app.exec_())
