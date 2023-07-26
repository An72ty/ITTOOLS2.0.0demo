from PyQt5 import QtWidgets, QtGui

class Main():
    def __init__(self):
        self.error = QtWidgets.QMessageBox()
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(
            "images/icons/ITTOOLS_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.error.setWindowIcon(self.icon)
        self.error.setWindowTitle("Work")
        self.error.setText("Все работает")
        self.error.setIcon(QtWidgets.QMessageBox.Warning)
        self.error.setStandardButtons(
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
    def show(self):
        self.error.exec_()