import os
try:
    from PyQt5 import QtWidgets, QtGui
except:
    os.system("pip install -r requirements.txt")
    from PyQt5 import QtWidgets, QtGui
from design import Ui_MainWindow
from dialogs.install_plugin_dialog import install_plugin
from dialogs.activate_plugin_dialog import activate_plugin
from dialogs.remove_plugin_dialog import remove_plugin
from libs import sqlCoder as sql
from widgets.plugin_design import Ui_Plugin
from libs import network
from dialogs.install_plugin_dialog import install_plugin
import shutil
import requests
import zipfile
import re
import os
import time
import threading
import sys


BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET = """QPushButton {
                                            border: 0px;
                                            color: #C2C2C2;
                                            font: 25px "Verdana";
                                            }

                                            QPushButton::hover {
                                                color: white;
                                            }
                                        """
CLICKED_TOP_MENU_PANEL_BUTTON_STYLESHEET = """QPushButton {
                                            border: 0px;
                                            color: white;
                                            font: 25px "Verdana";
                                            }

                                            QPushButton::hover {
                                                color: white;
                                            }
                                         """
# BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET = """QPushButton {
#                                             border: 0px;
#                                             color: white;
#                                             font: 25px "Verdana";
#                                             border-radius: 10px;
#                                             }

#                                             QPushButton::hover {
#                                                 background-color: #5a6677;
#                                             }
#                                         """
# CLICKED_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET = """QPushButton {
#                                             border: 0px;
#                                             background-color: #18202c;
#                                             font: 25px "Verdana";
#                                             border-radius: 10px;
#                                             }

#                                             QPushButton::hover {
#                                                 background-color: #18202c;
#                                             }
#                                         """


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        ui = super()
        ui.setupUi(self.MainWindow)
        # Setup sql
        sql.initTable()
        # Update plugin info
        sql.updateDB()
        self.is_db_updating = True
        self.db_updating_thread = threading.Thread(target=self.db_updating)
        self.db_updating_thread.start()
        self.add_functions_to_top_menu_panel_buttons()
        self.add_functions_to_left_menu_panel_buttons()

    def db_updating(self):
        while self.is_db_updating:
            sql.updateDB()
            time.sleep(1)

    def add_functions_to_top_menu_panel_buttons(self):
        def show_whats_new_frame():
            self.whats_new_btn.setStyleSheet(
                CLICKED_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.eternal_arts_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.credits_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.about_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            # self.settings_btn.setStyleSheet(
            #    BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)

            self.whats_new_frame.raise_()

        def show_eternal_arts_frame():
            self.whats_new_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.eternal_arts_btn.setStyleSheet(
                CLICKED_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.credits_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.about_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            # self.settings_btn.setStyleSheet(
            #    BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)

            self.eternal_arts_frame.raise_()

        def show_credits_frame():
            self.whats_new_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.eternal_arts_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.credits_btn.setStyleSheet(
                CLICKED_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.about_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            # self.settings_btn.setStyleSheet(
            #    BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)

            self.credits_frame.raise_()

        def show_about_frame():
            self.whats_new_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.eternal_arts_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.credits_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.about_btn.setStyleSheet(
                CLICKED_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            # self.settings_btn.setStyleSheet(
            #    BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)

            self.about_frame.raise_()

        # def show_settings_frame():
        #     self.whats_new_btn.setStyleSheet(
        #         BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
        #     self.eternal_arts_btn.setStyleSheet(
        #         BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
        #     self.credits_btn.setStyleSheet(
        #         BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
        #     self.about_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
        #     # self.settings_btn.setStyleSheet(
        #     #    CLICKED_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)

        #     self.settings_frame.raise_()

        self.whats_new_btn.clicked.connect(show_whats_new_frame)
        self.eternal_arts_btn.clicked.connect(show_eternal_arts_frame)
        self.credits_btn.clicked.connect(show_credits_frame)
        self.about_btn.clicked.connect(show_about_frame)
        # self.settings_btn.clicked.connect(show_settings_frame)

    def add_functions_to_left_menu_panel_buttons(self):
        self.show_plugins_btn.clicked.connect(self.show_show_plugins_frame)
        self.install_plugin_btn.clicked.connect(
            self.show_install_plugin_dialog)
        self.activate_plugin_btn.clicked.connect(
            self.show_activate_plugin_dialog)
        self.remove_plugin_btn.clicked.connect(self.show_remove_plugin_dialog)
        self.exit_btn.clicked.connect(self.MainWindow.close)

    def show_show_plugins_frame(self):
        self.set_base_stylesheet_to_top_menu_panel_buttons()
        self.install.clicked.connect(
            lambda: install_plugin.Dialog.install_plugin(self.plugin_input.text(), self))

        self.show_plugins_frame.raise_()

        for widget in self.plugins_area_content.children():
            widget.setParent(None)
        y_move = 2
        for name, version, image in sql.getPluginsList():
            Plugin = QtWidgets.QWidget(self.plugins_area_content)
            ui = Ui_Plugin()
            ui.setupUi(Plugin)
            try:
                icon = QtGui.QPixmap(f"plugins/{name}/{image}")
                ui.icon.setPixmap(icon)
            except FileNotFoundError:
                icon = QtGui.QPixmap("images/icons/ITTOOLS_icon.ico")
                ui.icon.setPixmap(icon)
            ui.name.setText(name)
            ui.version.setText(version)
            ui.remove.clicked.connect(
                lambda: remove_plugin.Dialog.remove_plugin(name, self))
            ui.activate.clicked.connect(
                lambda: activate_plugin.Dialog.activate_plugin(name))
            Plugin.move(2, y_move)
            y_move += Plugin.height() + 10
            Plugin.show()
            if Plugin.y() >= self.plugins_area_content.height():
                self.plugins.setFixedWidth(
                    self.plugins_area_content.width() + 5)
                self.plugins_area_content.setFixedHeight(
                    y_move + Plugin.height())

    def show_install_plugin_dialog(self):
        self.set_base_stylesheet_to_top_menu_panel_buttons()
        install_plugin.Window = self
        dialog = install_plugin.Dialog()
        dialog.Dialog.exec_()

    def show_activate_plugin_dialog(self):
        self.set_base_stylesheet_to_top_menu_panel_buttons()
        dialog = activate_plugin.Dialog()
        dialog.Dialog.exec_()

    def show_remove_plugin_dialog(self):
        self.set_base_stylesheet_to_top_menu_panel_buttons()
        remove_plugin.Window = self
        dialog = remove_plugin.Dialog()
        dialog.Dialog.exec_()

    def set_base_stylesheet_to_top_menu_panel_buttons(self):
        self.whats_new_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
        self.eternal_arts_btn.setStyleSheet(
            BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
        self.credits_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
        self.about_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
        # self.settings_btn.setStyleSheet(
        #     BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.MainWindow.show()
    window.is_db_updating = False
    sys.exit(app.exec_())
