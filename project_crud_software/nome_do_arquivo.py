from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class Ui_Dialog(object):
    def setupUI(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog") #Atribua um nome interno para que Dialogele ainda não tenha um ( objectNameé útil para identificar objetos no código).
            Dialog.resize(589, 437) # Defina o tamanho da janela principal: largura 589px e altura 437px.
    
    #Adicionando a Área de Rolagem  
    
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 20, 411, 391))
        self.scrollArea.setWidgetResizable(True)
        # Crie uma área rolável ( QScrollArea), posicionada com QRect(x=20, y=20, largura=411, altura=391).
        # Defina que o conteúdo dentro da área de rolagem pode ser redimensionado automaticamente.
        self.scrollAreaWidgetContents = QWidget()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        
        #Adicionando a Barra de Rolagem Vertical
        self.verticalScrollBar = QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(390, 10, 16, 371))
        self.verticalScrollBar.setOrientation(Qt.Vertical)    
