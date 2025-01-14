from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from display import Display
import sys

from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    
    #display
    
    display = Display()
    window.addWidgetToVLayout(display)


    window.adjustFixedSize()
    

    window.show()
    app.setStyle("Windows11")
    app.exec()
    