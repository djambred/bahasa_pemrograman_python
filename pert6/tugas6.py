class Waktu:

    def __init__(self, jam, menit, detik):
        self.jam = jam
        self.menit = menit
        self.detik = detik
    
    def info(self):
        if self.jam >= 24 or self.menit >= 60 or self.detik >= 60:
            print("wrong value")
        else:
            print(self.jam,':',self.menit,':',self.detik)

waktu = Waktu(int(input("masukkan jam: ")), int(input("masukkan menit: ")), int(input("masukkan detik: ")))
waktu.info()
