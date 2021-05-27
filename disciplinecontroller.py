import dbconnection as DB
import disciplinetype as dt

class disciplinecontroller():

    @staticmethod
    def gettypedisc():
        try:
            listofdisciplinetype = []

            conn=DB.dbconnection.getconn()
            cursor = conn.cursor()
            cursor.execute('select * from discipline')

            for row in cursor:
                disciplinetype =dt.disciplinetype(row[0],row[1]) #id, name
                listofdisciplinetype.append(disciplinetype)
            return listofdisciplinetype

        except Exception as e:
            print(e)
        finally:
            conn.close()
