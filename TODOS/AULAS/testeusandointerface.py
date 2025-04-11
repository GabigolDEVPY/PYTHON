import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, 
                               QPushButton, QListWidget, QLineEdit, QMessageBox)
from PySide6.QtCore import QTimer


class ListaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.lista = []

        # Configuração da interface
        self.setWindowTitle('Gerenciador de Lista')
        self.setGeometry(200, 200, 400, 300)

        # Layout principal
        self.layout = QVBoxLayout()

        # Label de status
        self.status_label = QLabel(f'Sua lista tem atualmente {len(self.lista)} ITEM(S)')
        self.layout.addWidget(self.status_label)

        # Lista de itens
        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        # Entrada para adicionar itens
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Digite o item para adicionar')
        self.layout.addWidget(self.input_field)

        # Botões
        self.add_button = QPushButton('Adicionar Item')
        self.add_button.clicked.connect(self.adicionar_item)
        self.layout.addWidget(self.add_button)

        self.delete_button = QPushButton('Apagar Item Selecionado')
        self.delete_button.clicked.connect(self.apagar_item)
        self.layout.addWidget(self.delete_button)

        # Atualizar interface
        self.setLayout(self.layout)
    
    def atualizar_status(self):
        self.status_label.setText(f'Sua lista tem atualmente {len(self.lista)} ITEM(S)')

    def adicionar_item(self):
        item = self.input_field.text()
        
        if not item.isalpha():
            QMessageBox.warning(self, "Erro", "Apenas letras são permitidas!")
        elif item in self.lista:
            QMessageBox.warning(self, "Aviso", "Item já existe na lista!")
        else:
            self.lista.append(item)
            self.list_widget.addItem(item)
            self.input_field.clear()
            self.atualizar_status()

    def apagar_item(self):
        current_item = self.list_widget.currentItem()
        if current_item:
            item_text = current_item.text()
            self.lista.remove(item_text)
            self.list_widget.takeItem(self.list_widget.row(current_item))
            self.atualizar_status()
        else:
            QMessageBox.warning(self, "Erro", "Selecione um item para apagar!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    janela = ListaApp()
    janela.show()
    
    sys.exit(app.exec())
