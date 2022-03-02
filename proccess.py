class Proccess:
    def __init__(self, id, n_proccess):
        self.__clock = [0 for i in range(n_proccess)]
        self.__id = id

    def set_clock(self, id, value):
        self.__clock[id] = value

    def get_proccess_id(self):
        return self.__id

    def get_clock(self):
        return self.__clock
