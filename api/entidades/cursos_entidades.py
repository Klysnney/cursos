class CursoEntidades():
    def __init__(self, nome, area):
        self.__nome = nome
        self.__area = area

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area
