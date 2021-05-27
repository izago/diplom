class institutetype():

    def __init__(self, ID_INSTITUTE, name_institute):
        self.__ID_INSTITUTE = ID_INSTITUTE
        self.__name_institute = name_institute

    #setters
    def setInstName(self, name_institute):
        self.__name_institute = name_institute

    def setInstID(self, ID_INSTITUTE):
        self.__ID_INSTITUTE = ID_INSTITUTE

    #getters
    def getInstID(self):
        return self.__ID_INSTITUTE

    def getInstName(self):
        return self.__name_institute