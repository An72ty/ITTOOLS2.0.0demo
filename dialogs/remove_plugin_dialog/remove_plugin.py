from dialogs.remove_plugin_dialog.remove_plugin_design import Ui_Dialog
from libs import sqlCoder as sql
from PyQt5 import QtWidgets
import shutil


class Dialog(Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.Dialog = QtWidgets.QDialog()
        ui = super()
        ui.setupUi(self.Dialog)

        self.add_items_to_plugin_input()

        self.cancel.clicked.connect(self.Dialog.close)
        self.remove.clicked.connect(
            lambda: self.remove_plugin(self.plugin_input.currentText()))

    def add_items_to_plugin_input(self):
        for name, _, _ in sql.getPluginsList():
            self.plugin_input.addItem(name)

    @staticmethod
    def remove_plugin(name: str):
        shutil.rmtree(f'plugins/{name}')
        sql.updateDB()
