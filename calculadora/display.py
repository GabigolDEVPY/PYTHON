from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUN_WIDTH

class Display(QLineEdit):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        margins = [TEXT_MARGIN - 10 for _ in range(4)]
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px;")
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUN_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)