import dbconnection as DB
import institutetype as it

class institutecontroller():

    @staticmethod
    def gettypeinst():
        try:
            listofinstitutetype = []

            conn=DB.dbconnection.getconn()
            cursor = conn.cursor()
            cursor.execute('select * from institute')

            for row in cursor:
                institutetype=it.institutetype(row[0],row[1]) #id, name
                listofinstitutetype.append(institutetype)
            return listofinstitutetype

        except Exception as e:
            print(e)
