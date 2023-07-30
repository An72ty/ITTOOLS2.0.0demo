from dialogs.activate_plugin_dialog.activate_plugin_design import Ui_Dialog
from PyQt5 import QtWidgets
from libs import sqlCoder as sql
import importlib


class Dialog(Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.Dialog = QtWidgets.QDialog()
        ui = super()
        ui.setupUi(self.Dialog)

        self.add_items_to_plugin_input()

        self.cancel.clicked.connect(self.Dialog.close)
        self.activate.clicked.connect(
            lambda: self.activate_plugin(self.plugin_input.currentText(), self))

    def add_items_to_plugin_input(self):
        for name, _, _ in sql.getPluginsList():
            self.plugin_input.addItem(name)

    @staticmethod
    def activate_plugin(name: str, activate_plugin_dialog=None):
        plugin = importlib.import_module(f'plugins.{name}.plugin')
        if activate_plugin_dialog:
            activate_plugin_dialog.Dialog.close()
        p = plugin.Main()
        p.show()
