from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Display(QLineEdit):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
    
    def configStyle(self):
        self.setStyleSheet("font-size: 30px")