from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Isekai.py")
ulkofraami = Frame(root, pady=5)
ulkofraami.grid(row=0,column=0,columnspan=3)
nappifraami = Frame(ulkofraami, padx=50, pady=5)
nappifraami.grid(row=2,column=0,columnspan=3)
tekstifraami = LabelFrame(ulkofraami, padx=100)
tekstifraami.grid(row=1, column=0)
tekstinro = 0
valintanro = 0

def update():
    global tekstinro
    tekstinro += 1
    teksti.configure(text=tekstilista[tekstinro])

def valinta1():
    global tekstinro
    tekstinro = 100

def valinta2():
    global tekstinro
    tekstinro = 200

def valinta3():
    global tekstinro
    tekstinro = 300

intro = "Pimeänä ja kosteana tammikuun perjantai iltana olet menossa \nostamaan kaljaa k-marketista rankan amispäivän jälkeen. Matkalla \nkuitenkin virolainen raksamies ajaa kännissä päältäsi saabilla. "
t1_1 = "Yrität kalastaa mutta se on ilman kynsiä yllättävän hankalaa.  kalat ovat limaisia ja liukuvat käsistäsi. Nukahdat ojaan  nälästä, väsymyksestä ja hämmennyksestä rankan päivän jälkeen.Heräät tuntemattomassa huoneesa sängyltä ja huomaat että sinua "
kysymys1 = "1. vaihtoehto: Jää ojaan kalastamaan käyttäen käsiä. \n2. vaihtoehto: Tutki olisiko lähiympäristössä ruokaa. \n3. vaihtoehto: Seuraa joen viereistä polkua siviilisaatioon."

t1_2 = "Lähdet tutkimaan läheistä metsää löytämättä mitään muuta kuin \ntuntemattomia sieniä joita et uskalla syödä. Ihmeen kaupalla löy-\ndät puskan vierestä kimpaleen grillattua lihaa ja kun menet lähelle,"
t1_21 = "Huomaat lihanpullia puun alla ja jäät ansaan. Seuraavana aamuna\n setämiehen näköinen mies joka ei näytä tyytyväiseltä napattuun \nriistaan vie sinut pienen kylän kirkolta näyttävään rakennukseen."
t1_22 = "Heräät tuntemattomassa huoneesa sängyltä ja huomaat että sinua tarkkaillaan. Huomaat nuorehkon tytönsängyn vieressä. Hän kertoo nimekseen Nita ja ja kysyy miksi olit jalkapuussa."
t1_3 = "Matkaat polkua pitkin kunnes päädyt pieneen kylään. Kylässä on"



kuva = ImageTk.PhotoImage(Image.open("kuvat/joki.jpg"))
kuval = Label(ulkofraami, image=kuva)
kuval.grid(row=0,column=0)

teksti = Label(tekstifraami, text=intro, bd=12)
teksti.grid(row=0, column=0)

tekstilista = [" "]
tekstilista[0] = intro
tekstilista[1]

seuraava = Button(nappifraami, text="Seuraava", padx=10, command=update)
seuraava.grid(row=0, column=0)
stats = Button(nappifraami, text="Tiedot", padx=10)
stats.grid(row=0, column=1)
valinta1 = Button(nappifraami, text="valinta 1", padx=10, command=valinta1)
valinta1.grid(row=0, column=2)
valinta2 = Button(nappifraami, text="valinta 2", padx=10, command=valinta2)
valinta2.grid(row=0, column=3)
valinta3 = Button(nappifraami, text="valinta 3", padx=10, command=valinta3)
valinta3.grid(row=0, column=4)

root.mainloop()