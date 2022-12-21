import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
import os

root = Tk()
root.title = ("sample app")
root.geometry = ('400x580')

def beriair():
    showinfo(title='info', message='sudah di beri air')

def beripupuk():
    showinfo(title='info', message='sudah di beri pupuk')

#button air
air = PhotoImage(file="./img/seed.png")
button_air = Button(root, image=air,borderwidth=0, cursor="hand2", command=beriair)
button_air.place(x=10, y=10)

#button pupuk
pupuk = PhotoImage(file="./img/small.png")
button_pupuk = Button(root, image=pupuk,borderwidth=0, cursor="hand2", command=beripupuk)
button_pupuk.place(x=200, y=10)

#button pupuk
keluar = PhotoImage(file="./img/iconair.png")
button_keluar = Button(root, image=keluar,borderwidth=0, cursor="hand2",command=root.destroy)
button_keluar.place(x=25, y=200)



root.mainloop()