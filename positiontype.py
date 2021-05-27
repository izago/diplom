class positiontype():

    def __init__(self, ID_POSITION, name_position):
        self.__ID_POSITION = ID_POSITION
        self.__name_position = name_position

    #setters
    def setPosName(self, name_position):
        self.__name_position = name_position

    def setPosID(self, ID_POSITION):
        self.__ID_POSITION = ID_POSITION

    #getters
    def getPosID(self):
        return self.__ID_POSITION

    def getPosName(self):
        return self.__name_position