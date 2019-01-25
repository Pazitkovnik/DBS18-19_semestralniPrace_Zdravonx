from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
import mysql.connector

import user_gui
import sql_functions

class Window(QWidget):
    def __init__(self, cursor, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Zdravonx")
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.resize(600, 400)
        self.cursor = cursor

        self.initUI()
 
    def initUI(self):
        self.machine_list = QListWidget()
        self.refresh_machine_list()

        self.button_remove = QPushButton(self.tr('Remove'))
        self.button_remove.clicked.connect(self.action_remove_machine)

        self.button_add = QPushButton(self.tr('Add'))
        self.button_add.clicked.connect(self.action_add_machine)
        
        self.button_edit = QPushButton(self.tr('Edit'))
        self.button_edit.clicked.connect(self.action_edit_machine)

        self.button_find = QPushButton(self.tr('Find'))
        self.button_find.clicked.connect(self.action_add_machine)

        self.button_export = QPushButton(self.tr('Export to PDF'))
        self.button_export.clicked.connect(self.action_edit_machine)

        self.button_users = QPushButton(self.tr('Users'))
        self.button_users.clicked.connect(self.action_edit_machine)

        self.button_servis = QPushButton(self.tr('Servis ZP'))
        self.button_servis.clicked.connect(self.action_edit_machine)

        self.button_kontrola = QPushButton(self.tr('Kontrola ZP'))
        self.button_kontrola.clicked.connect(self.action_edit_machine)
        
        b4=QPushButton("Button4")

        vlay = QVBoxLayout()
        vlay.addWidget(self.button_remove)
        vlay.addWidget(self.button_add)
        vlay.addWidget(self.button_edit)
        vlay.addWidget(self.button_find)
        vlay.addWidget(self.button_export)
        vlay.addWidget(self.button_users)
        vlay.addWidget(self.button_servis)
        vlay.addWidget(self.button_kontrola)

        hlay = QHBoxLayout(self)
        hlay.addWidget(self.machine_list)
        hlay.addLayout(vlay)

        
 
        self.setLayout(hlay)
        self.setWindowTitle("ZDRAVONX")

    def refresh_machine_list(self):
        self.machine_list.clear()
        machines = sql_functions.get_all_machines(self.cursor)
        for m in machines:
            self.machine_list.addItem(m[0])

    def get_active_machine_name(self):
        item = self.machine_list.currentItem()
        return item.data(Qt.DisplayRole)
          
    def action_remove_machine(self):
        name = self.get_active_machine_name()
        #delete the item from gui list
        row = self.machine_list.currentRow()
        self.machine_list.takeItem(row)
        sql_functions.remove_machine(self.cursor, name)
        print(name)

    def action_add_machine(self):
        self.adder = user_gui.Add_Machine(self.cursor, self)

    def action_edit_machine(self):
        self.editer = user_gui.Edit_Machine(self.cursor, self, self.get_active_machine_name())
        

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    #change the gui style
    QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))

    mysql_connection = mysql.connector.MySQLConnection()
    login = user_gui.Login(mysql_connection, 'admin', 'adminoslav666')
    
    if login.exec_() == QtWidgets.QDialog.Accepted:
        cursor = mysql_connection.cursor()

        #check if the user is admin or just technician
        is_admin = sql_functions.is_user_admin(cursor)
        if is_admin:
            print('prihlasen jako admin')
        else:
            print('prihlasen jako prach sprosty technik')
        
        window = Window(cursor)
        window.show()
        sys.exit(app.exec_())
