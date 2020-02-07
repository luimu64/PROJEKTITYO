from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Isekai.py")
ulkofraami = LabelFrame(root, pady=5)
ulkofraami.grid(row=0,column=0,columnspan=3)
nappifraami = LabelFrame(ulkofraami, padx=50, pady=5)
nappifraami.grid(row=2,column=0,columnspan=3)

def update(path,tekstinro):
    teksti.configure(text="tekstilista[tekstinro]")

intro = "Pimeänä ja kosteana tammikuun perjantai iltana olet menossa \nostamaan kaljaa k-marketista rankan amispäivän jälkeen. Matkalla \nkuitenkin virolainen raksamies ajaa kännissä päältäsi saabilla. "
kuva = ImageTk.PhotoImage(Image.open("kuvat/joki.jpg"))
kuval = Label(ulkofraami, image=kuva)
kuval.grid(row=0,column=0)

teksti = Label(ulkofraami, text=intro)
teksti.grid(row=1, column=0)

tekstilista[0] = intro


seuraava = Button(nappifraami, text="Seuraava", padx=10)
seuraava.grid(row=0, column=0)
stats = Button(nappifraami, text="Tiedot", padx=10)
stats.grid(row=0, column=1)
valinta1 = Button(nappifraami, text="valinta 1", padx=10)
valinta1.grid(row=0, column=2)
valinta2 = Button(nappifraami, text="valinta 2", padx=10)
valinta2.grid(row=0, column=3)
valinta3 = Button(nappifraami, text="valinta 3", padx=10)
valinta3.grid(row=0, column=4)

root.mainloop()