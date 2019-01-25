from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import mysql.connector
import sql_functions
# from mainwindow import Ui_MainWindow

class Login(QtWidgets.QDialog):
    def __init__(self, mysql_connection, username='', password='', parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle("Zdravonx")
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.username = username
        self.password = password
        
        self.mysql_connection = mysql_connection
        self.name_label = QtWidgets.QLabel("Username:")
        self.pass_label = QtWidgets.QLabel("Password:")
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        self.setFixedSize(225, 150)
        self.setStyleSheet('background-image: url(images/logo.png);')
        layout.addWidget(self.name_label)
        layout.addWidget(self.textName)
        layout.addWidget(self.pass_label)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        

    def handleLogin(self):
##        if (self.textName.text() == 'foo' and
##            self.textPass.text() == 'bar'):
##            a = 5
        try:
            if self.username or self.password:
                self.mysql_connection.connect(
                    host="localhost",
                    user=self.username,
                    passwd=self.password,
                    database="Zdravonx_database"
                )
            else:
                self.mysql_connection.connect(
                    host="localhost",
                    user=self.textName.text(),
                    passwd=self.textPass.text(),
                    database="Zdravonx_database"
                )
            self.accept()
        except mysql.connector.Error as err:
            print(err.errno)
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Cannot connect to the database!')
            else:
                QtWidgets.QMessageBox.warning(
                self, 'Error', 'Wrong username or password!')

            
class Add_Machine(QtWidgets.QWidget):
    
    def __init__(self, cursor, window):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.cursor = cursor
        self.window = window
        
        self.initUI()
        
        
    def initUI(self):
        
        idTyp = QLabel('ID typ')
        idOddel = QLabel('ID oddeleni')
        idDodav = QLabel('ID dodavatel')
        idStupen = QLabel('ID stupen')
        idStatus = QLabel('ID status')
        nazev = QLabel('Nazev')
        inv_cislo = QLabel('Inventarni cislo')
        vyr_cislo = QLabel('Vyrobni cislo')
        stupen_ochrany = QLabel('Stupen ochrany')
        typ = QLabel('Typ')
        umdns = QLabel('Kod UMNDS')
        umisteni = QLabel('Umisteni')
        datum = QLabel('Datum porizeni')

        self.edit_idTyp = QLineEdit()

        self.edit_idOddel = QLineEdit()

        self.edit_idDodav = QLineEdit()

        self.edit_nazev = QLineEdit()
        
        self.edit_inv_cislo = QLineEdit()
        
        self.edit_vyr_cislo = QLineEdit()

        self.edit_umdns = QLineEdit()
        
        self.edit_idStupen = QLineEdit()

        self.edit_idStatus = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(idTyp, 1, 0)
        grid.addWidget(self.edit_idTyp, 1, 1)

        grid.addWidget(idOddel, 2, 0)
        grid.addWidget(self.edit_idOddel, 2, 1)

        grid.addWidget(idDodav, 3, 0)
        grid.addWidget(self.edit_idDodav, 3, 1)

        grid.addWidget(nazev, 4, 0)
        grid.addWidget(self.edit_nazev, 4, 1)

        grid.addWidget(inv_cislo, 5, 0)
        grid.addWidget(self.edit_inv_cislo, 5, 1)

        grid.addWidget(vyr_cislo, 6, 0)
        grid.addWidget(self.edit_vyr_cislo, 6, 1)

        grid.addWidget(umdns, 7, 0)
        grid.addWidget(self.edit_umdns, 7, 1)

        grid.addWidget(idStupen, 8, 0)
        grid.addWidget(self.edit_idStupen, 8, 1)

        grid.addWidget(idStatus, 9, 0)
        grid.addWidget(self.edit_idStatus, 9, 1)

        self.button_add = QPushButton(self.tr('Add'))
        self.button_add.clicked.connect(self.action_add_machine)
        grid.addWidget(self.button_add)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Novy pristroj')    
        self.show()
        
    def action_add_machine(self):
        machine = []
        machine.append( int(self.edit_idTyp.text()) )
        machine.append( int(self.edit_idOddel.text()) )
        machine.append( int(self.edit_idDodav.text()) )
        machine.append(self.edit_nazev.text())
        machine.append(self.edit_inv_cislo.text())
        machine.append(self.edit_vyr_cislo.text())
        machine.append(self.edit_umdns.text())
        machine.append( int(self.edit_idStupen.text()) )
        machine.append( int(self.edit_idStatus.text()) )
        
        sql_functions.add_machine(self.cursor, machine)
        self.window.refresh_machine_list()
        #self.adder = user_gui.Add_Machine(self.cursor)
        self.close()
        
class Edit_Machine(QtWidgets.QWidget):   
    def __init__(self, cursor, window, name):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.cursor = cursor
        self.original_name = name
        self.window = window
        
        self.initUI()

    def initUI(self):
        machine = sql_functions.get_machine_info(self.cursor, self.original_name)
        idTyp = QLabel('ID typ')
        idOddel = QLabel('ID oddeleni')
        idDodav = QLabel('ID dodavatel')
        idStupen = QLabel('ID stupen')
        idStatus = QLabel('ID status')
        nazev = QLabel('Nazev')
        inv_cislo = QLabel('Inventarni cislo')
        vyr_cislo = QLabel('Vyrobni cislo')
        stupen_ochrany = QLabel('Stupen ochrany')
        typ = QLabel('Typ')
        umdns = QLabel('Kod UMNDS')
        umisteni = QLabel('Umisteni')
        datum = QLabel('Datum porizeni')

        self.edit_idTyp = QLineEdit()
        self.edit_idTyp.setText(str(machine[0][1]))

        self.edit_idOddel = QLineEdit()
        self.edit_idOddel.setText(str(machine[0][2]))

        self.edit_idDodav = QLineEdit()
        self.edit_idDodav.setText(str(machine[0][3]))

        self.edit_nazev = QLineEdit()
        self.edit_nazev.setText(machine[0][4])
        
        self.edit_inv_cislo = QLineEdit()
        self.edit_inv_cislo.setText(machine[0][5])
        
        self.edit_vyr_cislo = QLineEdit()
        self.edit_vyr_cislo.setText(machine[0][6])

        self.edit_umdns = QLineEdit()
        self.edit_umdns.setText(machine[0][7])
        
        self.edit_idStupen = QLineEdit()
        self.edit_idStupen.setText(str(machine[0][8]))

        self.edit_idStatus = QLineEdit()
        self.edit_idStatus.setText(str(machine[0][9]))

        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(idTyp, 1, 0)
        grid.addWidget(self.edit_idTyp, 1, 1)

        grid.addWidget(idOddel, 2, 0)
        grid.addWidget(self.edit_idOddel, 2, 1)

        grid.addWidget(idDodav, 3, 0)
        grid.addWidget(self.edit_idDodav, 3, 1)

        grid.addWidget(nazev, 4, 0)
        grid.addWidget(self.edit_nazev, 4, 1)

        grid.addWidget(inv_cislo, 5, 0)
        grid.addWidget(self.edit_inv_cislo, 5, 1)

        grid.addWidget(vyr_cislo, 6, 0)
        grid.addWidget(self.edit_vyr_cislo, 6, 1)

        grid.addWidget(umdns, 7, 0)
        grid.addWidget(self.edit_umdns, 7, 1)

        grid.addWidget(idStupen, 8, 0)
        grid.addWidget(self.edit_idStupen, 8, 1)

        grid.addWidget(idStatus, 9, 0)
        grid.addWidget(self.edit_idStatus, 9, 1)

        self.button_edit = QPushButton(self.tr('Edit'))
        self.button_edit.clicked.connect(self.action_edit_machine)
        grid.addWidget(self.button_edit)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Zmena pristroje')    
        self.show()

    def action_edit_machine(self):
        machine = []
        machine.append(self.edit_nazev.text())
        machine.append(self.edit_inv_cislo.text())
        machine.append(self.edit_vyr_cislo.text())
        #mozna chyba s ID!!! Neni jiste, takze mozna pohodicka jahodova
        
        sql_functions.remove_machine(self.cursor, self.original_name)
        sql_functions.add_machine(self.cursor, machine)
        self.window.refresh_machine_list()
        #self.adder = user_gui.Add_Machine(self.cursor)
        self.close()
