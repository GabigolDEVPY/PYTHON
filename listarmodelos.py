from PySide6.QtWidgets import QApplication, QStyleFactory

app = QApplication([])

# Listar todos os estilos disponíveis
print(QStyleFactory.keys())

app.exec()
