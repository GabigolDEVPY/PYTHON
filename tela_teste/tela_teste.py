from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys
from backend import teste_base_dir as tb

def janela():
    app = QApplication(sys.argv)
    window = QMainWindow()
    layout = QGridLayout()
    central_widget = QWidget()
    window.setWindowTitle("SYSTEM REGISTER")
    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)

    lista = QListWidget()

    linha_name = QLineEdit()
    linha_name.setPlaceholderText("ENTER NAME")

    linha_cpf = QLineEdit()
    linha_cpf.setPlaceholderText("ENTER CPF")

    linha_phone = QLineEdit()
    linha_phone.setPlaceholderText("ENTER NUMBER PHONE")

    button = QPushButton("REGISTER")
    delete_button = QPushButton("DELETE")
    edit_button = QPushButton("EDIT")


    layout.addWidget(lista)
    layout.addWidget(linha_name)
    layout.addWidget(linha_cpf)
    layout.addWidget(linha_phone)
    layout.addWidget(delete_button)
    layout.addWidget(button)
    layout.addWidget(edit_button)



    def add_name():
        if len(linha_name.text()) > 2 and len(linha_cpf.text()) > 8 and len(linha_phone.text()) > 8:
            users = tb.load_file()
            name = linha_name.text()
            lista.addItem(name)
            user = {"Name": linha_name.text(),
                    "Phone": linha_phone.text(),
                    "CPF": linha_cpf.text()         
            }
            users.append(user)
            tb.save_file(users)
        

    def delete():
        users = tb.load_file()
        select_line = lista.currentRow()
        print(select_line)
        del users[select_line]
        lista.takeItem(select_line)
        tb.save_file(users)

    def edit():
        window_edit = QDialog()
        window_edit.setWindowTitle("EDIT USER")
        window_edit.resize(400, 200)

        layout = QVBoxLayout()
        window_edit.setLayout(layout)

        button_save = QPushButton("SAVE")
        button_cancel = QPushButton("CANCEL")
        


        Name_line = QLineEdit()
        cpf_line = QLineEdit()
        phone_line = QLineEdit()

        
        Hlayout_name = QHBoxLayout()
        name_text = QLabel("Name:")
        Hlayout_name.addWidget(name_text)
        Hlayout_name.addWidget(Name_line)
        layout.addLayout(Hlayout_name)
        
        Hlayout_cpf = QHBoxLayout()
        cpf_text = QLabel("CPF:")
        Hlayout_cpf.addWidget(cpf_text)
        Hlayout_cpf.addWidget(cpf_line)
        layout.addLayout(Hlayout_cpf)
        
        Hlayout_phone = QHBoxLayout()
        phone_text = QLabel("PHONE:")
        Hlayout_phone.addWidget(phone_text)
        Hlayout_phone.addWidget(phone_line)
        layout.addLayout(Hlayout_phone)
        
        layout.addWidget(button_cancel)
        layout.addWidget(button_save)
        
        window_edit.exec()
        
        
        
        
        
        
        
        
        



    button.clicked.connect(add_name)
    delete_button.clicked.connect(delete)
    edit_button.clicked.connect(edit)

    def charge_names():
        users = tb.load_file()
        for user in users:
            lista.addItem(f"Name: {user['Name']}")

    charge_names()
    window.show()
    app.exec()

janela()