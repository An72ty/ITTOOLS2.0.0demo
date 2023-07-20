from PyQt5 import QtWidgets
from PyQt5 import QtGui
from design import Ui_MainWindow
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
BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET = """QPushButton {
                                            border: 0px;
                                            color: white;
                                            font: 25px "Verdana";
                                            border-radius: 10px;
                                            }

                                            QPushButton::hover {
                                                background-color: #5a6677;
                                            }
                                        """
CLICKED_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET = """QPushButton {
                                            border: 0px;
                                            background-color: #18202c;
                                            font: 25px "Verdana";
                                            border-radius: 10px;
                                            }

                                            QPushButton::hover {
                                                background-color: #18202c;
                                            }
                                        """


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        ui = super()
        ui.setupUi(self.MainWindow)
        # Set main window icon
        self.MainWindow.setWindowIcon(QtGui.QIcon('images/icons/ITTOOLSicon.ico'))

        self.add_functions_to_top_menu_panel_buttons()

    def add_functions_to_top_menu_panel_buttons(self):
        def show_whats_new_frame():
            self.whats_new_btn.setStyleSheet(
                CLICKED_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.eternal_arts_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.credits_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.about_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.settings_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)

            self.whats_new_frame.show()
            self.eternal_arts_frame.hide()
            self.credits_frame.hide()
            self.about_frame.hide()
            self.settings_frame.hide()

        def show_eternal_arts_frame():
            self.whats_new_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.eternal_arts_btn.setStyleSheet(
                CLICKED_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.credits_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.about_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.settings_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)

            self.whats_new_frame.hide()
            self.eternal_arts_frame.show()
            self.credits_frame.hide()
            self.about_frame.hide()
            self.settings_frame.hide()

        def show_credits_frame():
            self.whats_new_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.eternal_arts_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.credits_btn.setStyleSheet(
                CLICKED_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.about_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.settings_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)

            self.whats_new_frame.hide()
            self.eternal_arts_frame.hide()
            self.credits_frame.show()
            self.about_frame.hide()
            self.settings_frame.hide()

        def show_about_frame():
            self.whats_new_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.eternal_arts_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.credits_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.about_btn.setStyleSheet(
                CLICKED_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.settings_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)

            self.whats_new_frame.hide()
            self.eternal_arts_frame.hide()
            self.credits_frame.hide()
            self.about_frame.show()
            self.settings_frame.hide()

        def show_settings_frame():
            self.whats_new_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.eternal_arts_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.credits_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.about_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.settings_btn.setStyleSheet(
                CLICKED_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)
            self.whats_new_frame.hide()
            self.eternal_arts_frame.hide()
            self.credits_frame.hide()
            self.about_frame.hide()
            self.settings_frame.show()

        self.whats_new_btn.clicked.connect(show_whats_new_frame)
        self.eternal_arts_btn.clicked.connect(show_eternal_arts_frame)
        self.credits_btn.clicked.connect(show_credits_frame)
        self.about_btn.clicked.connect(show_about_frame)
        self.settings_btn.clicked.connect(show_settings_frame)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Set app icon
    app.setWindowIcon(QtGui.QIcon('images/icons/ITTOOLSicon.ico'))
    window = MainWindow()
    window.MainWindow.show()
    sys.exit(app.exec_())
