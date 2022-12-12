class Mahasiswa:

    # class attribute
    matkul = "PBO"

    # instance attribute
    def __init__(self, name, nim):
        self.name = name
        self.nim = nim

# instantiate Mahasiswa class
a = Mahasiswa("Budi", 123456789)
b = Mahasiswa("Ani", 1234567890)

# access the class attributes
print("A tergabung dalam {}".format(a.__class__.matkul))
print("B juga tergabung dalam {}".format(b.__class__.matkul))

# access the instance attributes
print("{} punya nim {}".format( a.name, a.nim))
print("{} punya nim {}".format( b.name, b.nim))

