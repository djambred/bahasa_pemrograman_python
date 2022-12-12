class Induk:
    def __init__(self):
        self.satu = "Satu"
        self.dua = "Dua"

class Anak:
    def __init__(self):
        Induk.__init__(self)
        print(self.__dua)
        print("call class anak")

#call induk
obj = Induk()
print(obj.satu)