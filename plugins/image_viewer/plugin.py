from PIL import Image
from PyQt5.QtWidgets import QFileDialog


class Main():
    def __init__(self):
        self.filename, _ = QFileDialog.getOpenFileName()
        if self.filename:
            with Image.open(self.filename) as self.img:
                self.img.load()

    def show(self):
        self.img.show()
