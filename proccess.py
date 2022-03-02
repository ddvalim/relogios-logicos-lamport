class Proccess:
    def __init__(self, id, n_proccess):
        self.__clock = [0 for i in range(n_proccess)]
        self.__id = id

    def set_clock(self, id, value):
        self.__clock.insert(id, value)

    @property
    def get_proccess_id(self):
        return self.__id

    @property
    def get_clock(self):
        return self.__clock
