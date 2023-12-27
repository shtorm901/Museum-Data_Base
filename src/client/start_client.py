import sys

from PyQt6 import QtWidgets

from srck.login_form import LoginForm

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginForm()
    login_window.show()
    app.exec()