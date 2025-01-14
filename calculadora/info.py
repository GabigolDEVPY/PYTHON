from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)