from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtWidgets
from ui.login_form import Ui_MainWindow as Ui_LoginForm


class LoginForm(QtWidgets.QMainWindow, Ui_LoginForm):

    login_correct = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.pushButton.clicked.connect(self.check_user)
        self.pushButton_2.clicked.connect(self.exit)
