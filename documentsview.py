class documentsview():

    def __init__(self,ID_DOCUMENTS, name_document, date_of_creation, document, ID_DISCIPLINE, ID_USER):
        self.__ID_DOCUMENTS = ID_DOCUMENTS
        self.__name_document = name_document
        self.__date_of_creation = date_of_creation
        self.__document = document
        self.__ID_DISCIPLINE = ID_DISCIPLINE
        self.__ID_USER = ID_USER

    # setters
    def setDocName(self, name_document):
        self.__name_document = name_document

    def setDocDate(self, date_of_creation):
        self.__date_of_creation = date_of_creation

    def setDocID(self, ID_DOCUMENTS):
        self.__ID_DOCUMENTS = ID_DOCUMENTS

    def setDoc(self, document):
        self.__document = document

    def setDiscID(self, ID_DISCIPLINE):
        self.__ID_DISCIPLINE = ID_DISCIPLINE

    def setUserID(self, ID_USER):
        self.__ID_USER = ID_USER

        # getters

    def getDocName(self):
        self.__name_document

    def getDocDate(self):
        self.__date_of_creation

    def getDocID(self):
        self.__ID_DOCUMENTS

    def getDoc(self):
        self.__document

    def getDiscID(self):
        self.__ID_DISCIPLINE

    def getUserID(self):
        self.__ID_USER