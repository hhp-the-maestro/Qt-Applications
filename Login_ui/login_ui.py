import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QLineEdit, QPushButton, QCheckBox, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import csv
import pandas as pd


class SignUp(QWidget):

    def __init__(self):
        super().__init__()
        self.initialize_ui2()

    def initialize_ui2(self):
        self.setGeometry(100, 200, 400, 300)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.display_signup()
        self.setWindowTitle('Sign Up Form')
        self.show()

    def display_signup(self):
        sign_up_title = QLabel(self)
        sign_up_title.setText('Sign Up')
        sign_up_title.setFont(QFont('Arial', 20))
        sign_up_title.move(160, 20)

        name_label = QLabel(self)
        name_label.setText('Username')
        name_label.move(40, 80)

        password_label = QLabel(self)
        password_label.setText('Password')
        password_label.move(40, 120)

        confirm_password_label = QLabel(self)
        confirm_password_label.setText('Confirm\nPassword')
        confirm_password_label.move(40, 150)

        self.username_entry = QLineEdit(self)
        self.username_entry.move(130, 75)
        self.username_entry.resize(200, 30)

        self.password_entry = QLineEdit(self)
        self.password_entry.move(130, 115)
        self.password_entry.resize(200, 30)

        self.confirm_password_entry = QLineEdit(self)
        self.confirm_password_entry.move(130, 155)
        self.confirm_password_entry.resize(200, 30)

        sign_up_btn = QPushButton('Sign Up', self)
        sign_up_btn.move(150, 200)
        sign_up_btn.resize(90, 30)
        sign_up_btn.clicked.connect(self.create_account)

    def create_account(self):
        wrong_pass = self.check_password()
        if wrong_pass == False:
            try:
                file = open('users.csv', 'r')
            except FileNotFoundError:
                file = open('users.csv', 'a')
                fields = ['username', 'password']
                writer = csv.writer(file)
                writer.writerow(fields)
            file = open('users.csv', 'a')
            get_user = self.username_entry.text()
            get_pass = self.password_entry.text()
            info = [get_user, get_pass]
            writer = csv.writer(file)
            writer.writerow(info)
            file.close()

            self.msg_success_box(get_user)

    def msg_success_box(self, username):
        QMessageBox.information(self, 'account_info', f'Account created for {username}',
                                QMessageBox.Ok, QMessageBox.Ok)
        self.close()

    def check_password(self):
        password = self.password_entry.text()
        confirm_password = self.confirm_password_entry.text()
        username = self.username_entry.text()
        if username == '':
            QMessageBox.warning(self, 'username error', 'enter a username',
                                QMessageBox.Close, QMessageBox.Close)
            wrong_pass = True
            return wrong_pass
        try:
            file = pd.read_csv('users.csv')
            if username in list(file['username']):
                QMessageBox.warning(self, 'username error', 'This username is already taken')
                wrong_pass = True
                return wrong_pass
        except FileNotFoundError:
            pass
        if password != confirm_password:
            QMessageBox.warning(self, 'password error', 'Passwords does not match',
                                QMessageBox.Close, QMessageBox.Close)
            wrong_pass = True
            return wrong_pass
        if len(password) < 4:
            if len(password) == 0:
                QMessageBox.warning(self, 'password error', 'enter a password',
                            QMessageBox.Close, QMessageBox.Close)
                wrong_pass = True
                return wrong_pass
            QMessageBox.warning(self, 'password error', 'enter a strong password',
                                QMessageBox.Close, QMessageBox.Close)
            wrong_pass = True
            return wrong_pass

        wrong_pass = False
        return wrong_pass


class LoginUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 200, 400, 300)
        self.setWindowTitle('Login UI')
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.login_user_interface()
        self.show()

    def login_user_interface(self):
        login_label = QLabel(self)
        login_label.setText('Login')
        login_label.move(160, 10)
        login_label.setFont(QFont('Arial', 20))

        name_label = QLabel(self)
        name_label.setText('Username:')
        name_label.move(40, 70)

        self.name_entry = QLineEdit(self)
        self.name_entry.move(120, 65)
        self.name_entry.resize(200, 30)

        pass_label = QLabel(self)
        pass_label.setText('Password:')
        pass_label.move(40, 115)

        self.password_entry = QLineEdit(self)
        self.password_entry.move(120, 110)
        self.password_entry.resize(200, 30)
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.show_pwd_cb = QCheckBox(text="show password", parent=self)
        self.show_pwd_cb.move(180, 145)
        self.show_pwd_cb.toggle()
        self.show_pwd_cb.setChecked(False)
        self.show_pwd_cb.stateChanged.connect(self.show_password)

        sign_in_btn = QPushButton('Login', self)
        sign_in_btn.move(100, 190)
        sign_in_btn.clicked.connect(self.click_login)
        sign_in_btn.resize(90, 30)

        sign_up_btn = QPushButton('Sign up', self)
        sign_up_btn.move(210, 190)
        sign_up_btn.resize(90, 30)
        sign_up_btn.clicked.connect(self.signup_window)

    def signup_window(self):
        self.signup_window_object = SignUp()
        self.signup_window_object.show()

    def click_login(self):
        username = self.name_entry.text()
        password = self.password_entry.text()
        file = pd.read_csv('users.csv')

        if username in list(file['username']) and password in list(file['password'][file.username == username]):
            QMessageBox.information(self, 'Login successful', 'Login successful',
                                    QMessageBox.Ok, QMessageBox.Ok)
            self.close()

        else:
            QMessageBox.warning(self, 'Error Message', 'Username or Password incorrect',
                                QMessageBox.Close, QMessageBox.Close)

    def show_password(self, state):
        if state == Qt.Checked:
            self.password_entry.setEchoMode(QLineEdit.Normal)
        else:
            self.password_entry.setEchoMode(QLineEdit.Password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginUI()
    sys.exit(app.exec_())



