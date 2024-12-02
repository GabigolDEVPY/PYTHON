from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(589, 437)

        # Botão Register
        self.pushButtonRegister = QPushButton(Dialog)
        self.pushButtonRegister.setObjectName(u"Register_button")
        self.pushButtonRegister.setText("Register")
        self.pushButtonRegister.setGeometry(470, 20, 100, 40)  # Define posição e tamanho (x, y, largura, altura)


class MainApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("REGISTER SOFTWARE")

        # Conectando o botão "Register" para adicionar informações
        self.ui.pushButtonRegister.clicked.connect(self.add_infos)

    def add_infos(self):
        # Cria uma nova janela de diálogo para capturar informações
        info_dialog = QDialog(self)
        info_dialog.setWindowTitle("Enter Infos")
        info_layout = QVBoxLayout(info_dialog)

        # Campo para Nome
        name_label = QLabel("Enter Name:")
        name_input = QLineEdit()
        info_layout.addWidget(name_label)
        info_layout.addWidget(name_input)

        # Campo para CPF
        cpf_label = QLabel("Enter CPF:")
        cpf_input = QLineEdit()
        info_layout.addWidget(cpf_label)
        info_layout.addWidget(cpf_input)

        # Botão para confirmar
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(info_dialog.accept)  # Fecha a janela com 'OK'
        info_layout.addWidget(ok_button)

        # Mostra a janela de diálogo e pega as infos
        if info_dialog.exec():
            name = name_input.text()
            cpf = cpf_input.text()
            print(f"Name: {name}, CPF: {cpf}")  # Faz o que quiser com os dados aqui!


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
