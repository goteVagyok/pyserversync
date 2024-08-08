import PyQt6.uic

from PyQt6.QtWidgets import *


app = QApplication([])
call = PyQt6.uic.loadUi("src/ui/main.ui")

call.show()
