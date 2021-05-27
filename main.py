import sys

import db_handler
from controllers import institutecontroller as ic
from controllers import disciplinecontroller as dc
from controllers import positioncontroller as pc
from check_db import *
from db_handler import *
from PyQt5.QtCore import QDir

import dbconnection as DB

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget,  QComboBox, QTextEdit, QMessageBox, QFileDialog, QPushButton
from PyQt5.uic import loadUi


class MainWindow(QDialog,QTextEdit):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("enter1.ui", self)

        self.pushButton.clicked.connect(self.Auth)
        self.pushButton_2.clicked.connect(self.gotoRegistration)
        self.base_line_edit = [self.login, self.password]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text())==0:
                    return
            funct(self)
        return wrapper

    @check_input
    def Auth(self):
        log = self.login.text()
        passw = self.password.text()
        self.check_db.thr_login(log,passw)


    def signal_handler(self,value):
        QtWidgets.QMessageBox.about(self,'Оповещение', value)

    def gotoRegistration(self):
        registr = Registration()
        widget.addWidget(registr)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoBase(self):
        base = Base()
        widget.addWidget(base)
        widget.setCurrentIndex(widget.currentIndex()+2)

    def gotoStart(self):
        mainwindow =MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex())

class Registration(QDialog, QTextEdit, QComboBox):
    def __init__(self):
        super(Registration, self).__init__()
        loadUi("registr.ui", self)
        self.next_button.clicked.connect(self.reg)
        self.initinst()
        self.initpos()

        self.base_line_edit = [self.login, self.oldpassword,self.surname, self.name]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

        self.inst_box.currentIndexChanged.connect(self.instselected)
        self.possition_box.currentIndexChanged.connect(self.posselected)

    def instselected(self):
        cbinstindex = self.inst_box.currentIndex()
        inst_selected = listofinstitutetype[cbinstindex]
        sel = inst_selected.getInstID()
        print(sel)

    def posselected(self):
        cbposindex = self.possition_box.currentIndex()
        pos_selected = listofpositiontype[cbposindex]
        sel2 = pos_selected.getPosID()
        print(sel2)

    def signal_handler(self,value):
        QtWidgets.QMessageBox.about(self,'Оповещение', value)

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    msg = QMessageBox()
                    msg.setWindowTitle("Ошибка")
                    msg.setText("Заполните обязательные поля")
                    msg.setIcon(QMessageBox.Warning)
                    msg.exec_()
                    return
            funct(self)
        return wrapper

    @check_input
    def reg(self):
        log_2 = self.login.text()
        passw_2 = self.oldpassword.text()
        sur = self.surname.text()
        na = self.name.text()
        id_ins = self.instselected()
        id_pos = self.posselected()
        self.check_db.thr_register(log_2, passw_2, sur, na, id_ins, id_pos)

    def initinst(self):
        global listofinstitutetype
        listofinstitutetype = ic.institutecontroller.gettypeinst()

        for x in listofinstitutetype:
            self.inst_box.addItem(x.getInstName())

    def initpos(self):
        global listofpositiontype
        listofpositiontype = pc.positioncontroller.gettypepos()

        for x in listofpositiontype:
            self.possition_box.addItem(x.getPosName())

    def gotoBase(self):
        base = Base()
        widget.addWidget(base)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Base(QDialog,QComboBox,QTableWidget,QPushButton):

    def __init__(self):
        super(Base, self).__init__()
        loadUi("base.ui", self)
        self.initdisc()
        self.initdoc()

        self.tableWidget_2.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('Название документа'))
        self.tableWidget_2.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('Дата создания'))
        self.tableWidget_2.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('Дисциплина'))

        self.chooseButton.clicked.connect(self.BF)

    def BF(self):
        fname= QFileDialog.getOpenFileName(self, 'Open file','C\\Users\\', 'EXCEL files (*.xlsx)')
        self.file.setText(fname[0])

    def initdoc(self):

        conn = DB.dbconnection.getconn()
        cursor = conn.cursor()
        cursor.execute('SELECT d.name_document, d.date_of_creation, di.name_discipline from DOCUMENTS d left join DISCIPLINE di  on d.ID_DISCIPLINE = di.ID_DISCIPLINE')

        self.tableWidget_2.setRowCount(1)
        tablerow=0
        for row in cursor.fetchall():
            self.tableWidget_2.setItem(tablerow,0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))

    def initdisc(self):
        global listofdisciplinetype
        listofdisciplinetype = dc.disciplinecontroller.gettypedisc()

        for x in listofdisciplinetype:
            self.discipline_box.addItem(x.getDiscName())

app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow=MainWindow()
base=Base()
registr=Registration()
widget.setFixedWidth(700)
widget.setFixedHeight(500)

widget.addWidget(mainwindow)
widget.addWidget(registr)
widget.addWidget(base)

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("some")