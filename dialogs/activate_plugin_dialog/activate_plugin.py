from dialogs.activate_plugin_dialog.activate_plugin_design import Ui_Dialog
from PyQt5 import QtWidgets


class Dialog(Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.Dialog = QtWidgets.QDialog()
        ui = super()
        ui.setupUi(self.Dialog)

        self.cancel.clicked.connect(self.Dialog.close)