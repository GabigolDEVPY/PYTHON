from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys
from backend import teste_base_dir as tb


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

def edit(user):
    layout = QGridLayout()
    central_widget = QWidget()
    window.setWindowTitle("SYSTEM REGISTER")
    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)
    
    Name_line = QLineEdit()
    cpf_line = QLineEdit()
    phone_line = QLineEdit()
    # nametext = QTextLine()
    
    
    
    # layout.addWidget(nametext)
    layout.addWidget(Name_line)
    layout.addWidget(cpf_line)
    layout.addWidget(phone_line)
    
    

button.clicked.connect(add_name)
delete_button.clicked.connect(delete)
edit_button.clicked.connect(edit)

def charge_names():
    users = tb.load_file()
    for user in users:
        lista.addItem(f"Name: {user["Name"]}")

charge_names()
window.show()
app.exec()

