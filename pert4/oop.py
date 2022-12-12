class Segitiga:
  def __init__(self, alas, tinggi):
    self.alas = alas
    self.tinggi = tinggi

  def get_luas(self):
    return 0.5 * self.alas * self.tinggi

segitiga1 = Segitiga(5, 10)


print('luas segitiga1:', segitiga1.get_luas())


class Kotak:
    def input1(self):
        self.p = int(input("masukan panjang\t: "))
        self.l = int(input("masukan lebar\t: "))

    def luas(self):
        self.luas1 = self.p*self.l

kotak1 = Kotak()
kotak1.input1()
kotak1.luas()

print ("luas kotak\t:",kotak1.luas1)