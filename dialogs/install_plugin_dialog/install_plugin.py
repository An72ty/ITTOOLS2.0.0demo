from dialogs.install_plugin_dialog.install_plugin_design import Ui_Dialog
from PyQt5 import QtWidgets, QtGui
from libs import network
from libs import sqlCoder as sql
import shutil
import re
import requests
import os
import zipfile

App = None
class Dialog(Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.Dialog = QtWidgets.QDialog()
        ui = super()
        ui.setupUi(self.Dialog)

        self.cancel.clicked.connect(self.Dialog.close)
        self.install.clicked.connect(
            lambda: self.install_plugin(self.plugin_input.text(), App))

    @staticmethod
    def install_plugin(text, app):
        error = QtWidgets.QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "images/icons/ITTOOLS_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        error.setWindowIcon(icon)
        error.setWindowTitle("Error")
        error.setText("Text")
        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.setStandardButtons(
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        answer = text
        if re.compile(r"""[A-Za-zА-Яа-яёЁ0-9_]+\\[A-Za-zА-Яа-яёЁ0-9_]+""").fullmatch(answer):
            # if plugin is not downloaded...
            repName = "ittoolplugin."+answer.split('\\')[1]
            pluginName = answer.split('\\')[1]
            developerName = answer.split('\\')[0]
            if not os.path.exists(f'plugins/{pluginName}'):

                url = f"https://raw.githubusercontent.com/{developerName}/{repName}/main/info.json"
                if network.networkConnectionCheck(url):
                    os.mkdir(f'plugins/{pluginName}')
                    # read info.json
                    response = requests.get(url)
                    with open(f'plugins/{pluginName}/info.json', 'wb') as file:
                        file.write(response.content)
                    response = requests.get(
                        f"https://raw.githubusercontent.com/{developerName}/{repName}/main/README.md")
                    with open(f'plugins/{pluginName}/README.md', 'wb') as file:
                        file.write(response.content)
                    response = requests.get(
                        f"https://raw.githubusercontent.com/{developerName}/{repName}/main/main.zip")
                    with open(f'plugins/{pluginName}/main.zip', 'wb') as file:
                        file.write(response.content)
                    try:
                        response = requests.get(
                            f"https://raw.githubusercontent.com/{developerName}/{repName}/main/requirements.txt")
                        with open(f'plugins/{pluginName}/requirements.txt', 'wb') as file:
                            file.write(response.content)
                    except:
                        pass
                    # Unpack zip
                    with zipfile.ZipFile(f'plugins/{pluginName}/main.zip', mode='a') as file:
                        file.extractall(
                            path=f'plugins/{pluginName}')
                    os.remove(f'plugins/{pluginName}/main.zip')
                else:
                    error.setText("Unknow rep or user name")
                    error.exec_()
            else:
                url = f"https://raw.githubusercontent.com/{developerName}/{repName}/main/info.json"
                if network.networkConnectionCheck(url):
                    shutil.rmtree(f'plugins/{pluginName}')
                    os.mkdir(f'plugins/{pluginName}')
                    # read info.json
                    response = requests.get(url)
                    with open(f'plugins/{pluginName}/info.json', 'wb') as file:
                        file.write(response.content)
                    response = requests.get(
                        f"https://raw.githubusercontent.com/{developerName}/{repName}/main/README.md")
                    with open(f'plugins/{pluginName}/README.md', 'wb') as file:
                        file.write(response.content)
                    response = requests.get(
                        f"https://raw.githubusercontent.com/{developerName}/{repName}/main/main.zip")
                    with open(f'plugins/{pluginName}/main.zip', 'wb') as file:
                        file.write(response.content)
                    try:
                        response = requests.get(
                            f"https://raw.githubusercontent.com/{developerName}/{repName}/main/requirements.txt")
                        with open(f'plugins/{pluginName}/requirements.txt', 'wb') as file:
                            file.write(response.content)
                    except:
                        pass
                    # Unpack zip
                    with zipfile.ZipFile(f'plugins/{pluginName}/main.zip', mode='a') as file:
                        file.extractall(
                            path=f'plugins/{pluginName}')
                    os.remove(f'plugins/{pluginName}/main.zip')
                else:
                    error.setText("Unknow rep or user name")
                    error.exec_()

        else:
            error.setText("Unknow rep or user name")
            error.exec_()

        sql.updateDB()
        app.show_show_plugins_frame()
