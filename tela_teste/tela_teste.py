from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys
import os
from backend import teste_base_dir as tb, gen_id as gi, valid_cpf as vc

def janela():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setFixedSize(500, 500)
    layout = QGridLayout()
    central_widget = QWidget()
    window.setWindowTitle("SYSTEM REGISTER")
    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)
    lista = QListWidget()
    message = QLabel()
    

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
    layout.addWidget(message)
    layout.addWidget(delete_button)
    layout.addWidget(button)
    layout.addWidget(edit_button)



    def add_name():
        users = tb.load_file()
        name = linha_name.text()
        phone = linha_phone.text()
        cpf = linha_cpf.text()
        cpf_valid = vc.verify(cpf)
        print(cpf_valid)
        users = tb.load_file()
        
        numerate = 0
        for user in users:
            numerate += 1
            
        if len(linha_name.text()) > 2 and cpf_valid == 4 and len(linha_phone.text()) == 11:
            user = {
                "ID": gi.id(),
                "Name": linha_name.text(),
                    "Phone": linha_phone.text(),
                    "CPF": linha_cpf.text()         
            }
            lista.addItem(f"{numerate+1}. Name: {user['Name']}")
            users.append(user)
            tb.save_file(users)
        elif cpf_valid == 1:
            message.setText('CPF DOES NOT CONTAIN 11 DIGITS')
                
        elif cpf_valid == 2:
            message.setText('ONLY TYPE NUMBERS IN YOUR CPF')
                
        elif cpf_valid == 1:
            message.setText('CPF DOES NOT CONTAIN 11 DIGITS')
                
        elif len(name) < 3:
            message.setText('Name incomplete')    

        elif len(phone) != 11:
            message.setText('Phone inválid')    

        
    
    def delete():
        users = tb.load_file()
        select_line = lista.currentRow()
        print(select_line)
        del users[select_line]
        lista.takeItem(select_line)
        tb.save_file(users)
        lista.clear()
        charge_names()
        
    def edit(user):
        user_num = int(user[0])
        users = tb.load_file()
        user_atual = users[user_num - 1]
        def save_user():
            user_atual["Name"] = Name_line.text()
            user_atual["CPF"] = cpf_line.text()
            user_atual["Phone"] = phone_line.text()
            tb.save_file(users)
            lista.clear()
            charge_names()
            window_edit.close()
    

        
        
        window_edit = QDialog()
        window_edit.setWindowTitle("EDIT USER")
        window_edit.resize(400, 200)

        layout = QVBoxLayout()
        window_edit.setLayout(layout)

        button_save = QPushButton("SAVE")
        button_cancel = QPushButton("CANCEL")
        


        Name_line = QLineEdit()
        Name_line.setText(user_atual["Name"])
        
        cpf_line = QLineEdit()
        cpf_line.setText(user_atual["CPF"])
        
        phone_line = QLineEdit()
        phone_line.setText(user_atual["Phone"])


        
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
        button_cancel.clicked.connect(window_edit.close)
        button_save.clicked.connect(save_user)
        window_edit.exec()
        
        
        
        
    button.clicked.connect(add_name)
    delete_button.clicked.connect(delete)
    edit_button.clicked.connect(lambda: edit(lista.currentItem().text() if lista.selectedIndexes() else message.setText("   NO USERS WERE SELECTED")))


    def charge_names():
        users = tb.load_file()
        numerate = 0
        for user in users:
            lista.addItem(f"{numerate+1}. Name: {user['Name']}")
            numerate += 1

    charge_names()
    window.show()
    app.exec()

janela()