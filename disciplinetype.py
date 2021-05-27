class disciplinetype():

    def __init__(self, ID_DISCIPLINE, name_discipline):
        self.__ID_DISCIPLINE = ID_DISCIPLINE
        self.__name_discipline = name_discipline

    #setters
    def setDiscName(self, name_discipline):
        self.__name_discipline = name_discipline

    def setDiscID(self, ID_DISCIPLINE):
        self.__ID_DISCIPLINE = ID_DISCIPLINE

    #getters
    def getDiscId(self):
        return self.__ID_DISCIPLINE

    def getDiscName(self):
        return self.__name_discipline