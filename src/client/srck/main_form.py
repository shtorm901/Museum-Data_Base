from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtWidgets
from ui.main_form import Ui_MainWindow as Ui_MainForm


class MainForms(QtWidgets.QMainWindow, Ui_MainForm):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)


