import dbconnection as DB
import documentsview as dv

class documentscontroller():

    @staticmethod
    def getviewidoc():
        try:
            listofdocumentsview = []

            conn=DB.dbconnection.getconn()
            cursor = conn.cursor()
            cursor.execute('SELECT d.name_document, d.date_of_creation, di.name_discipline from DOCUMENTS d left join DISCIPLINE '
                       'di  on d.ID_DISCIPLINE = di.ID_DISCIPLINE')

            for row in cursor.fetchall():

                documentsview=dv.documentsview(row[0],row[1],row[2],row[3],row[4],row[5])
                listofdocumentsview.append(documentsview)
            return listofdocumentsview

        except Exception as e:
            print(e)
        finally:
            conn.close()