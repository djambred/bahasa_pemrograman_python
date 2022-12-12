# parent class
class Person(object):
    def __init__(self, id, nama):
        self.id = id
        self.nama = nama
    def display(self):
        print(self.id,"-", self.nama)
        
# child class
class Employee(Person):
    def __init__(self, id, nama, gaji, posisi):
        self.gaji = gaji
        self.posisi = posisi
        Person.__init__(self, id, nama)
    def empDisp(self):
        print(self.id,"-", self.nama,"-", self.gaji,"-", self.posisi)

# creation of an object variable or an instance
test = Employee(1,'John',4000000, 'Magang')
 
# calling a function of the class Person using its instance
test.display(), 
test.empDisp()

        