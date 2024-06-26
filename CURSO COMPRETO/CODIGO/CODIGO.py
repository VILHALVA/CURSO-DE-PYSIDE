import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QGridLayout, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Login')
        self.setFixedSize(300, 250)
        self.setStyleSheet('QMainWindow {background: #cfcfcf;}')

        label_nome = QLabel('Nome', self)
        label_nome.setStyleSheet("font-size:20px;")

        self.label_dig_nome = QLineEdit(self)
        self.label_dig_nome.setPlaceholderText('Digite aqui!')
        self.label_dig_nome.setStyleSheet("background-color: white; font-size:20px; border-radius: 5px;")

        label_senha = QLabel('Senha', self)
        label_senha.setStyleSheet("font-size:20px;")

        self.label_dig_senha = QLineEdit(self)
        self.label_dig_senha.setPlaceholderText('Digite aqui!')
        self.label_dig_senha.setEchoMode(QLineEdit.Password)
        self.label_dig_senha.setStyleSheet("background-color: white; font-size:20px; border-radius: 5px;")

        label_button = QPushButton('Enviar!', self)
        label_button.setFixedSize(100, 50)
        label_button.setStyleSheet("background-color: #457b9d; border-radius: 5px; font-size:20px;")

        label_button.clicked.connect(self.logar)

        label_button_cancel = QPushButton('Sair!', self)
        label_button_cancel.clicked.connect(self.cancelar)

        label_button_cancel.setFixedSize(100, 50)
        label_button_cancel.setStyleSheet("background-color: #e63946; border-radius: 5px; font-size:20px;")

        Layout = QGridLayout()
        Layout.addWidget(label_nome, 0 , 0)
        Layout.addWidget(self.label_dig_nome, 0 , 1)
        Layout.addWidget(label_senha, 1 , 0)
        Layout.addWidget(self.label_dig_senha, 1 , 1)
        Layout.addWidget(label_button, 2 , 1)
        Layout.addWidget(label_button_cancel, 2 , 0)

        widget = QWidget()
        widget.setLayout(Layout)
        self.setCentralWidget(widget)

    def logar(self):
        user_text = str(self.label_dig_nome.text())
        user_password = str(self.label_dig_senha.text())

        with open('credenciais.txt', 'r') as credenciais_file:
            credenciais = credenciais_file.readlines()

        user_credencias = f'{user_text}, {user_password}\n'

        if user_credencias in credenciais:
            tittle = 'Login Success'
            message = 'Login success'
        else:
            tittle = 'Failure'
            message = 'Login Failure você tera de se cadastrar antes!'

        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(tittle)
        msg.setText(message)
        msg.exec_()
        self.openSecondWindow()

    def cancelar(self):
        self.close()

    def openSecondWindow(self):
        self.hide()

        secondWindow = SecondWindow(self)
        secondWindow.show()

class SecondWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setStyleSheet('QMainWindow {background: #005f73;}')
        self.setWindowTitle('LobbyWindow')
        self.setFixedSize(300, 250)

        label_button = QPushButton("Cadastrar")
        label_button.setStyleSheet("background-color: #0a9396; border-radius: 5px; font-size:17px;")
        label_button.setFixedSize(90, 30)
        label_button.clicked.connect(self.CadastreWindow)
        
        label_button_search = QPushButton("Buscar")
        label_button_search.setStyleSheet("background-color: #ee9b00; border-radius: 5px; font-size:17px;")
        label_button_search.setFixedSize(90, 30)
        label_button_search.clicked.connect(self.searchWindow)

        label_button_cancel = QPushButton("Voltar")
        label_button_cancel.setStyleSheet("background-color: #ae2012; border-radius: 5px; font-size:17px;")
        label_button_cancel.setFixedSize(90, 30)
        label_button_cancel.clicked.connect(self.close)

        Layout = QGridLayout()
        Layout.addWidget(label_button, 2 , 1)
        Layout.addWidget(label_button_search, 2 , 2)
        Layout.addWidget(label_button_cancel, 2 , 0)

        widget = QWidget()
        widget.setLayout(Layout)
        self.setCentralWidget(widget)

    def CadastreWindow(self):
        self.hide()

        Cadastre = CadastreWindow(self)
        Cadastre.show()

    def searchWindow(self):
        self.hide()

        search = searchWindow(self)
        search.show()

    def closeEvent(self, event):
        self.parent().show()
        event.accept()

class CadastreWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setStyleSheet('QMainWindow {background: #cdb4db;}')
        self.setWindowTitle('Cadastro')
        self.setFixedSize(300, 250)

        label_nome = QLabel('Nome', self)
        label_nome.setStyleSheet("font-size:20px;")

        self.label_dig_nome = QLineEdit(self)
        self.label_dig_nome.setPlaceholderText('Digite aqui!')
        self.label_dig_nome.setStyleSheet("background-color: white; font-size:20px; border-radius: 5px;")

        label_senha = QLabel('Senha', self)
        label_senha.setStyleSheet("font-size:20px;")

        self.label_dig_senha = QLineEdit(self)
        self.label_dig_senha.setPlaceholderText('Digite aqui!')
        self.label_dig_senha.setEchoMode(QLineEdit.Password)
        self.label_dig_senha.setStyleSheet("background-color: white; font-size:20px; border-radius: 5px;")

        label_button = QPushButton("Cadastrar")
        label_button.setStyleSheet("background-color: #a2d2ff; border-radius: 5px; font-size:20px;")
        label_button.setFixedSize(100, 50)
        label_button.clicked.connect(self.cadastre)

        label_button_cancel = QPushButton("Voltar")
        label_button_cancel.setStyleSheet("background-color: #ffafcc; border-radius: 5px; font-size:20px;")
        label_button_cancel.setFixedSize(100, 50)
        label_button_cancel.clicked.connect(self.close)

        Layout = QGridLayout()
        Layout.addWidget(label_nome, 0 , 0)
        Layout.addWidget(self.label_dig_nome, 0 , 1)
        Layout.addWidget(label_senha, 1 , 0)
        Layout.addWidget(self.label_dig_senha, 1 , 1)
        Layout.addWidget(label_button, 2 , 1)
        Layout.addWidget(label_button_cancel, 2 , 0)

        widget = QWidget()
        widget.setLayout(Layout)
        self.setCentralWidget(widget)

    def cadastre(self):
        user_text = str(self.label_dig_nome.text())
        user_password = str(self.label_dig_senha.text())

        user_credencias = f'{user_text}, {user_password}\n'

        with open ('credenciais.txt', 'r') as credenciais_file:
            credenciais = credenciais_file.readlines()

        if  user_credencias in credenciais:
            tittle = 'Failure'
            message = 'Sua conta já esta cadastrada! ou a conta já existe!'
        else:
            with open ('credenciais.txt', 'a') as credenciais_file_register:
                credenciais_register = credenciais_file_register.writelines(user_credencias)
            credenciais_register
            tittle = 'Register Success'
            message = 'Registro efetuado com sucesso!'

        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(tittle)
        msg.setText(message)
        msg.exec_()

    def closeEvent(self, event):
        self.parent().show()
        event.accept()

class searchWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setStyleSheet('QMainWindow {background: #ffa69e;}')
        self.setWindowTitle('SearchWindow')
        self.setFixedSize(300, 250)

        label_nome = QLabel('Nome', self)
        label_nome.setStyleSheet("font-size:20px;")

        self.label_dig_nome = QLineEdit(self)
        self.label_dig_nome.setStyleSheet("background-color: white; font-size:20px; border-radius: 5px;")
        self.label_dig_nome.setPlaceholderText('Digite aqui!')

        label_senha = QLabel('Senha', self)
        label_senha.setStyleSheet("font-size:20px;")

        self.label_dig_senha = QLineEdit(self)
        self.label_dig_senha.setStyleSheet("background-color: white; font-size:20px; border-radius: 5px;")
        self.label_dig_senha.setPlaceholderText('Digite aqui!')
        self.label_dig_senha.setEchoMode(QLineEdit.Password)

        label_button = QPushButton("Buscar")
        label_button.setStyleSheet("background-color: #a5ffd6; border-radius: 5px; font-size:20px;")
        label_button.setFixedSize(100, 50)
        label_button.clicked.connect(self.search)

        label_button_cancel = QPushButton("Voltar")
        label_button_cancel.setStyleSheet("background-color: #ff686b; border-radius: 5px; font-size:20px;")
        label_button_cancel.setFixedSize(100, 50)
        label_button_cancel.clicked.connect(self.close)

        Layout = QGridLayout()
        Layout.addWidget(label_nome, 0 , 0)
        Layout.addWidget(self.label_dig_nome, 0 , 1)
        Layout.addWidget(label_senha, 1 , 0)
        Layout.addWidget(self.label_dig_senha, 1 , 1)
        Layout.addWidget(label_button, 2 , 1)
        Layout.addWidget(label_button_cancel, 2 , 0)

        widget = QWidget()
        widget.setLayout(Layout)
        self.setCentralWidget(widget)

    def search(self):
        user_text = str(self.label_dig_nome.text())
        user_password = str(self.label_dig_senha.text())

        user_credencias = f'{user_text}, {user_password}\n'

        with open ('credenciais.txt', 'r') as credenciais_file:
            credenciais = credenciais_file.readlines()

        if  user_credencias in credenciais:
            tittle = 'Verifição completa'
            message = (f'Essa "{user_text}, {user_password}" conta já esta cadastrada!')
        else:
            tittle = 'Verifição completa'
            message = (f'Essa "{user_text}, {user_password}" conta NÃO esta cadastrada no sistema! ')

        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(tittle)
        msg.setText(message)
        msg.exec_()

    def closeEvent(self, event):
        self.parent().show()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())