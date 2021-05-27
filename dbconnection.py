import pyodbc

class dbconnection():

    @staticmethod
    def getconn():
        try:
            conn= pyodbc.connect('DRIVER={SQL SERVER};'
                         'SERVER=DESKTOP-T8133DF;'
                         'DATABASE=DIPLOMDB;'
                         'Trusted_connection=yes;')
            return conn

        except Exception as e:
            print(e)