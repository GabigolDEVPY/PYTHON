from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(589, 437)
        
        # Scroll Area (mantido)
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 20, 411, 391))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 409, 389))
        self.verticalScrollBar = QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(390, 10, 16, 371))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        # Splitter para botões
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(450, 20, 121, 191))
        self.splitter.setOrientation(Qt.Vertical)
        
        self.pushButton = QPushButton(self.splitter)
        self.pushButton.setObjectName(u"pushButton")
        self.splitter.addWidget(self.pushButton)
        
        self.pushButton_2 = QPushButton(self.splitter)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.splitter.addWidget(self.pushButton_2)
        
        self.pushButton_3 = QPushButton(self.splitter)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.splitter.addWidget(self.pushButton_3)
        
        self.pushButton_4 = QPushButton(self.splitter)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.splitter.addWidget(self.pushButton_4)
        
        # List Widget para exibir nomes
        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 20, 411, 391))  # Alocado no mesmo espaço que o ScrollArea

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"REGISTER", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"DELETE", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"EDIT", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"SEARCH", None))


class MainApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Conectando o botão "REGISTER" para adicionar nomes
        self.ui.pushButton.clicked.connect(self.add_name)

    def add_name(self):
        # Exibe uma caixa de entrada para o usuário digitar o nome
        name, ok = QInputDialog.getText(self, "Add Name", "Enter a name:")
        if ok and name:
            self.ui.listWidget.addItem(name)  # Adiciona o nome ao QListWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
