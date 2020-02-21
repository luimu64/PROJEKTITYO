from tkinter import Tk, Frame, Label, Button, Toplevel, LabelFrame
from PIL import Image, ImageTk
import os
import pygame

pygame.mixer.init()
pygame.mixer.music.load("resurssit/bg.ogg")
pygame.mixer.music.play(-1) 

root = Tk()
root.title("Isekai.py")

ulkofraami = Frame(root, pady=5)
ulkofraami.grid(row=0,column=0,columnspan=3)
nappifraami = Frame(ulkofraami, padx=50, pady=5)
nappifraami.grid(row=2,column=0,columnspan=3)
tekstifraami = Frame(ulkofraami)
tekstifraami.grid(row=1, column=0)
tekstinro = 0
valintanro = 0
kuvanro = 0
i = 0
vastattu = 0


def tietoja():
    tietoja = Toplevel()
    tietoja.geometry("800x400")
    tietoja.title("Infoa")
    nappibox = LabelFrame(tietoja, text="Aiheet", padx=10)
    nappibox.grid(row=0, column=0)
    tekstibox = LabelFrame(tietoja, text="Sisältö", padx=10)
    tekstibox.grid(row=0, column=1)
    tieto1 = Button(nappibox, text="Uuden maailman uskonto", padx=10)
    tieto1.grid(row=0, column=0)
    tieto2 = Button(nappibox, text="Nita", padx=76)
    tieto2.grid(row=1, column=0)
    tietojal = Label(tekstibox, text="Paina nappeja katsoaksesi informaatiota", padx=10, pady=10)
    tietojal.pack()


def update():
    global tekstinro
    global kuvalista
    global valintanro
    if valintanro == 1:
        global i
        if valinta1l[i] == "loppu":
            valintanro = 0
            teksti.configure(text=tekstilista[tekstinro])
            tekstinro += 1
            return
        elif valinta1l[i] == "kuva1":
            kuval.config(image=kuvalista[1])
            i += 1
        teksti.configure(text=valinta1l[i])
        i += 1

    elif valintanro == 2:
        if valinta2l[i] == "loppu":
            valintanro = 0
            teksti.configure(text=tekstilista[tekstinro])
            tekstinro += 1
            return
        elif valinta2l[i] == "kuva1":
            kuval.config(image=kuvalista[1])
            i += 1
        teksti.configure(text=valinta2l[i])
        i += 1

    elif valintanro == 3:
        if valinta3l[i] == "loppu":
            valintanro = 0
            teksti.configure(text=tekstilista[tekstinro])
            tekstinro += 1
            return
        elif valinta3l[i] == "kuva1":
            kuval.configure(image=kuvalista[1])
            i += 1
        teksti.configure(text=valinta3l[i])
        i += 1
    elif valintanro == 0 and tekstinro == 0:
        tekstinro += 1
        teksti.configure(text=tekstilista[tekstinro])
        tekstinro += 1

    else:
        valintanro == 0
        teksti.configure(text=tekstilista[tekstinro])
        tekstinro += 1

def valinta1():
    global valintanro
    if vastattu == 0:
        valintanro = 1

def valinta2():
    global valintanro
    if vastattu == 0:
        valintanro = 2

def valinta3():
    global valintanro
    if vastattu == 0:
        valintanro = 3


intro = "Pimeänä ja kosteana tammikuun perjantai iltana olet menossa ostamaan kaljaa k-marketista rankan amispäivän jälkeen. \nMatkalla kuitenkin sattumanvaraisen rekkamiehen huomio herpaantuu ja hän ajaa päältäsi saabilla. \n "
kysymys1 = "1. vaihtoehto: Jää ojaan kalastamaan käyttäen käsiä. \n2. vaihtoehto: Tutki olisiko lähiympäristössä ruokaa. \n3. vaihtoehto: Seuraa joen viereistä polkua siviilisaatioon."
t1_1 = "Yrität kalastaa mutta se on ilman kynsiä yllättävän hankalaa. Kalat ovat limaisia ja liukuvat käsistäsi. \nNukahdat ojaan  nälästä, väsymyksestä ja hämmennyksestä rankan päivän jälkeen. \nHeräät tuntemattomassa huoneesa sängyltä ja huomaat että sinua tarkkaillaan."
t1_12 = "Tarkkalilija on nuorehko tyttö sängyn vieressä. Nimekseen hän kertoo Nita. Hän kysyy miksi olit ojassa ja vastaat \nettä yritit kalastaa ilman onkea ja nukahdit väsymyksestä. Nitan ilme muuttuu iloiseksi huomatessaan että olet kylläinen,\n ja kysyy \"Minulta meni juuri viimeinen leipä ja meinasin mennä kirkolta kysymään, haluatko tulla mukaan?\""
t1_13 = "Päätät mennä Nitan kanssa kirkolle. Kirkolle päästyänne papilta näyttävä henkilö tulee saarnaaman kyseisen kirkon \nuskonnosta. Päätät kuunneella mitä hänellä on sanottavaa ja päädyt johonkin kummalliseen rituaaliin. \nJossain vaiheessa rituaalia sinua alkaa yhtäkkiä nukuttamaan ja nukahdat."
t1_14 = "Heräät Nitan makuuhuoneesta ja hän kertoo kuinka tuuperruit rituaalin aikana, \njoten hän kantoi sinut kotiinsa lepäämään.\n "

t1_2 = "Lähdet tutkimaan läheistä metsää löytämättä mitään muuta kuin tuntemattomia sieniä joita et uskalla syödä. \nIhmeen kaupalla löydät puskan vierestä kimpaleen grillattua lihaa ja kun menet lähelle. \nHuomaat lihanpullia puun alla ja jäät ansaan. Seuraavana aamuna setämiehen näköinen mies joka"
t1_21 = " ei näytä tyytyväiseltä napattuun riistaan vie sinut pienen kylän kirkolta näyttävään \nrakennukseen. Heräät tuntemattomassa huoneesa sängyltä ja huomaat että sinua tarkkaillaan. \nTarkkailija on nuorehko tyttö sängyn vieressä. Hän kertoo nimekseen Nita ja ja kysyy miksi olit jalkapuussa."
t1_22 = "Vastaat \"En tiedä, jäin ansaaan ja menetin tajuntani\". \nHän vaikuttaa huojentuneelta että et ole rikollinen ja tarjoaa sienisoppaa syötäväksi."

t1_3 = "Matkaat polkua pitkin kunnes päädyt pieneen kylään. Kylässä on pieniä kivitaloja ja rakennus joka näyttää kirkolta.\n Päätät mennä katsooman jos kirkolta saisi jotain syötävää. Siellä tapaat papilta vaikuttavan henkilön \njoka kertoo alueen uskonnosta [lisätietoa uskonnosta \"Tiedot\" napista]."
t1_31 = "Päätät kuunneella mitä hänellä on sanottavaa ja päädyt johonkin kummalliseen rituaaliin. \nJossain vaiheessa rituaalia sinua alkaa yhtäkkiä nukuttamaan ja nukahdat. Heräät sängyltä ja huomaat että sinua \ntarkkaillaan. Tarkkailija on nuori tyttö joka kertoo nimekseen Nita. Kerrot olevasi nälkäinen ja hän tarjoaa sienisoppaa."

kuva_joki = ImageTk.PhotoImage(Image.open("/home/luimu/PROJEKTITYO/Projektityö/resurssit/joki.jpg"))
kuva_kmarket = ImageTk.PhotoImage(Image.open("/home/luimu/PROJEKTITYO/Projektityö/resurssit/Kmarket.jpg"))
kuva_kuva2 = ImageTk.PhotoImage(Image.open("/home/luimu/PROJEKTITYO/Projektityö/resurssit/kuva2.png"))

kuvalista = [kuva_joki, kuva_kmarket, kuva_kuva2]


kuval = Label(ulkofraami, image=kuvalista[0])
kuval.grid(row=0,column=0)

teksti = Label(tekstifraami, text=intro, bd=12)
teksti.grid(row=0, column=0)

tekstilista = [" "]
tekstilista = [intro, kysymys1, "teksti 3", "kysymys 2"]

valinta1l = ["kuva1", t1_1, t1_12, t1_13, t1_14, "loppu", "2_1", "2_2","loppu"]
valinta2l = [t1_2, t1_21, t1_22, " ", "loppu", "seuraava valinta teksti 2"]
valinta3l = [t1_3, t1_31, " ", " ", "loppu", "seuraava valinta teksti 3"]

seuraava = Button(nappifraami, text="Seuraava", padx=10, command=update)
seuraava.grid(row=0, column=0)
stats = Button(nappifraami, text="Tiedot", padx=10, command=tietoja)
stats.grid(row=0, column=1)
valinta1 = Button(nappifraami, text="valinta 1", padx=10, command=valinta1)
valinta1.grid(row=0, column=2)
valinta2 = Button(nappifraami, text="valinta 2", padx=10, command=valinta2)
valinta2.grid(row=0, column=3)
valinta3 = Button(nappifraami, text="valinta 3", padx=10, command=valinta3)
valinta3.grid(row=0, column=4)

root.mainloop()