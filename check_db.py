from PyQt5 import QtCore, QtGui, QtWidgets
from db_handler import *


class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def thr_login(self, log, passw):
        log_in(log, passw, self.mysignal)

    def thr_register(self, log_2, passw_2, sur, na, id_ins, id_pos):
        register(log_2, passw_2, sur, na, id_ins, id_pos, self.mysignal)