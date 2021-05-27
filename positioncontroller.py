import dbconnection as DB
import positiontype as pt

class positioncontroller():

    @staticmethod
    def gettypepos():
        try:
            listofpositiontype = []

            conn=DB.dbconnection.getconn()
            cursor = conn.cursor()
            cursor.execute('select * from position')

            for row in cursor:
                positiontype=pt.positiontype(row[0],row[1]) #id, name
                listofpositiontype.append(positiontype)
            return listofpositiontype

        except Exception as e:
            print(e)
