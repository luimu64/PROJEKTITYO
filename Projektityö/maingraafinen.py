from tkinter import Tk, Frame, Label, Button, Toplevel, LabelFrame
from PIL import Image, ImageTk
import os
import pygame

dir_path = os.path.dirname(os.path.realpath(__file__))

pygame.mixer.init()
pygame.mixer.music.load(str(dir_path) + "\\resurssit\\bg.ogg")
pygame.mixer.music.play(-1) 

t1 = "Pimeänä ja kosteana tammikuun perjantai iltana olet menossa ostamaan kaljaa k-marketista rankan amispäivän jälkeen. \nMatkalla kuitenkin epäonnekkaan autoilijan jarrut pettää hänen yrittäessään pysähtyä ja hän ajaa päältäsi. \n "
t12 = "Heräät aamulla joesta, mutta tuntuu että jotain on pielessä. Vesi on liian lämmintä ja on liian kirkasta ollakseen \ntammikuu saati sitten suomi ollenkaan. Sillä missä olet ja mikä aika on ei ole suurta merkitystä nyt huomattuasi sinun HIRMUISEN nälän\n"
kysymys1 = "1. vaihtoehto: Jää ojaan kalastamaan käyttäen käsiä. \n2. vaihtoehto: Tutki olisiko lähiympäristössä ruokaa. \n3. vaihtoehto: Seuraa joen viereistä polkua siviilisaatioon."
t1_1 = "Yrität kalastaa mutta se on ilman kynsiä yllättävän hankalaa. Kalat ovat limaisia ja liukuvat käsistäsi. \nNukahdat ojaan  nälästä, väsymyksestä ja hämmennyksestä rankan päivän jälkeen. \nHeräät tuntemattomassa huoneesa sängyltä ja huomaat että sinua tarkkaillaan."
t1_12 = "Tarkkalilija on nuorehko tyttö sängyn vieressä. Nimekseen hän kertoo Nita. Hän kysyy miksi olit ojassa ja vastaat \nettä yritit kalastaa ilman onkea ja nukahdit väsymyksestä. Nitan ilme muuttuu iloiseksi huomatessaan että olet kylläinen,\n ja kysyy \"Minulta meni juuri viimeinen leipä ja meinasin mennä kirkolta kysymään, haluatko tulla mukaan?\""
t1_13 = "Päätät mennä Nitan kanssa kirkolle. Kirkolle päästyänne papilta näyttävä henkilö tulee saarnaaman kyseisen kirkon \nuskonnosta. Päätät kuunneella mitä hänellä on sanottavaa ja päädyt johonkin kummalliseen rituaaliin. \n Nukahdat oudosti ja heräät nitan luota jossa hän kertoo kuinka tuuperruit rituaalin aikana."

t1_2 = "Lähdet tutkimaan läheistä metsää löytämättä mitään muuta kuin tuntemattomia sieniä joita et uskalla syödä. \nIhmeen kaupalla löydät puskan vierestä kimpaleen grillattua lihaa ja kun menet lähelle. \nHuomaat lihanpullia puun alla ja jäät ansaan. Seuraavana aamuna setämiehen näköinen mies joka"
t1_21 = "ei näytä tyytyväiseltä napattuun riistaan vie sinut pienen kylän kirkolta näyttävään \nrakennukseen. Heräät tuntemattomassa huoneesa sängyltä ja huomaat että sinua tarkkaillaan. \nTarkkailija on nuorehko tyttö sängyn vieressä. Hän kertoo nimekseen Nita ja ja kysyy miksi olit jalkapuussa."
t1_22 = "Vastaat \"En tiedä, jäin ansaaan ja menetin tajuntani\". \nHän vaikuttaa huojentuneelta että et ole rikollinen ja tarjoaa sienisoppaa syötäväksi.\n"

t1_3 = "Matkaat polkua pitkin kunnes päädyt pieneen kylään. Kylässä on pieniä kivitaloja ja rakennus joka näyttää kirkolta.\n Päätät mennä katsooman jos kirkolta saisi jotain syötävää. Siellä tapaat papilta vaikuttavan henkilön \njoka kertoo alueen uskonnosta [lisätietoa uskonnosta \"Tiedot\" napista]."
t1_31 = "Pappi vain selittää ja selittää eikä sinua voisi kiinnostaa vähempää. Mietit vain \"Jos olen mukava ja ymmärtäväinen\n saan ehkä häneltä jotain syötävää\". Jatkat kuuntelua kunnes pappi alkaakin yhtäkkiä kertomaan STAND:eistä.\n Olet lukenut JOJO'ssin joten ymmärrät kaikki papin piilotetut viittaukset"
t1_32 = "Päätät kuunneella tarkasti mitä hänellä on sanottavaa ja lopulta päädyt outoon rituaaliin. \nJossain vaiheessa rituaalia sinua alkaa yhtäkkiä nukuttamaan ja nukahdat. Heräät sängyltä ja huomaat että sinua \ntarkkaillaan. Tarkkailija on nuori tyttö joka kertoo nimekseen Nita. Kerrot olevasi nälkäinen ja hän tarjoaa sienisoppaa."

t2 = "Kuulet Nitalta paikallisesta örkki-ongelmasta. Örkit ovat ryöstäneet kaiken kullan mitä löytävät joka on epätavallistä\n käytöstä örkeille sillä örkit ovat liian tyhmiä ymmärtääkseen kullan arvoa. Kylän kykenevien olisi illalla suunnitelma\n käydä tuhoamassa eräs läheinen luola jonka uskotaan olevan örkkien pesä. Sinua kutsutaan mukaan operaatioon."
t21 = "Saat illalla miekan kylän sepältä puolustaaksesi itseäsi vaikka örkkejä ei kuuluisi olla koloissansa öisin. \nLähdet koloa kohti ryhmän mukana. Päätätte jakautua kahteen ryhmään yhteen joka sukeltaa koloon\n dynamiitin kanssa jättää sen sinne ja tulee takaisin ja toiseen joka estää örkkien paluun luolaan ja varmistaa pakoreitin."

kysymys2 = "1. Vaihtoehto: Mene koloon sukeltavan ryhmän kanssa\n 2. Vaihtoehto: Jää turvaamaan kolon suuta \n3. Vaihtoehto: Koeta karata tilanteesta metsään"

t2_1 =  "Otat mukaan dynamiitiä eddessäsi luolaan menee kaksi kylän miestä toisella kädessään kirves ja toisella soihtu.\n Luolassa on kosteaa ja haisee mädältä. päästyänne luolan syvinpiin syvyyksiin löydätte kasoittain kultaa,\n eläimien jäännöksiä ja ISON nukkuvan örkin yli kaksi metriä korkea ja näyttää siltä että saattaisi mennä herättyään"
t2_12 = "egyptiin hakkaamaan kaksisataa vuotta vanhan englantilais vamppyyrin eli toisin sanottuna sitä ei pitäisi herättää.\n Onneksi se on syvässä unessa ja saatte herättämättä örkkiä asetettua dynamiitit paikoilleen jolloin\n ne räjähdyttyään tukkisivat tunnelin kokonaan kivillä. Asetatte kaikki dynamiitit pitkään sytytyslankaan jonka voitte"
t2_13 = "sytyttää turvallisesti luolan suulta. Lähteässänne hiljaa uloskäyntiä päin mies kirveen kanssa kompastuu lepakkosoppakulhoon\n joka herättää örkin. Se nousee raivoissaan ylös ja salaman nopeasti juoksee soihtumiehen luokse\n jonka se läpsäyttää sinun viereiseen seinää päin kuin kärpäsen."

t2_2 = "Jäät luolan suulle miekka kädessä odottaen kylän miehiä jotka menivät luolaan dynamiitin kanssa. Odotat luolan suulla kunnes \nkuulet luolasta kovan kolauksen ja huudon jonka jälkeen luolasta juoksee ulos jääkaapin kokoinen \nörkki joka juoksee sinua päin heittäen sinut ilmaan ja ennen kuin huomaatkaan olet jo laskeutumassa ja osut maahan."

t2_3 = "Lähdet heti tilaisuuden tullessa juoksemaan mahdollisimman nopeasti pimeään metsään kunnes törmäät johonkin. Se ei ole puu \nvaan erittäin vihainen örkki joka vihaisena mosauttaa kallosi kasaan nuijalla.\n"

info_uskonto = "Pelin uskonnon mukaan kuka tahansa voi saada voimia joita kutsutaan 『STAND』eiksi. Tarinan päähenkilö sai oman voimansa nukahdettuaan kirkolla, mutta ei koskaan saanut käyttää sitä."
info_tekniset = "Peli on tehty käyttämällä Pythonin sisäänrakennettua Tkinter kirjastoa. Tkinter on tarkoitettu ohjemien käyttöliittymien tekemiseen ei pelien."
info_musiikki = "Music provided by No Copyright Music, Music used: Traveler by Alexander Nakarada @ SerpentSound Studios, Licensed under Creative Commons Attribution 4.0"
info_meista = "Roni teki tarinan ja haki kuvat, Leimu(minä) teki kaiken muun. Kummallakaan ei ollut kokemusta eikä motivaatiota lähes yhtään."

root = Tk()
root.title("Farssi.exe")
root.iconbitmap("resurssit\\icon.ico")

kuva_kmarket = ImageTk.PhotoImage(Image.open(str(dir_path) + "\\resurssit\\K-Market.jpg"))
kuva_kirkko = ImageTk.PhotoImage(Image.open(str(dir_path) + "\\resurssit\\kirkko.jpg"))
kuva_kylantalo = ImageTk.PhotoImage(Image.open(str(dir_path) + "\\resurssit\\kylantalo.jpg"))
kuva_luola = ImageTk.PhotoImage(Image.open(str(dir_path) + "\\resurssit\\toinenluola.jpg"))
kuva_kala = ImageTk.PhotoImage(Image.open(str(dir_path) + "\\resurssit\\kala.jpg"))
kuva_metsa = ImageTk.PhotoImage(Image.open(str(dir_path) + "\\resurssit\\pimeametsa.jpg"))

ulkofraami = Frame(root, pady=5, bg="black")
ulkofraami.grid(row=0,column=0,columnspan=3)
nappifraami = Frame(ulkofraami, padx=50, pady=5, bg="black")
nappifraami.grid(row=2,column=0,columnspan=2)
tekstifraami = Frame(ulkofraami, bg="black")
tekstifraami.grid(row=1, column=0)

valintanro = 0
tekstinro = 1



def tietoja():
    def tieto1():
        tietojal.config(text=info_uskonto)
    def tieto2():
        tietojal.config(text=info_musiikki)
    def tieto():
        tietojal.config(text=info_tekniset)
    def tieto3():
        tietojal.config(text=info_meista)

    tietoja = Toplevel(bg="black")
    tietoja.geometry("722x200")
    tietoja.title("Infoa")
    tietoja.iconbitmap("resurssit\\icon.ico")
    nappibox = LabelFrame(tietoja, text="Aiheet", padx=8, pady=10, bg="black", fg="white")
    nappibox.grid(row=0, column=0, padx=5)
    tekstibox = LabelFrame(tietoja, text="Sisältö", padx=10, bg="black", fg="white")
    tekstibox.grid(row=0, column=1, sticky="w n e", padx=5)
    tieto1 = Button(nappibox, text="Pelin maailman uskonto", command=tieto1, font=("Roboto", "14"))
    tieto1.grid(row=0, column=0, sticky="w e")
    tieto = Button(nappibox, text="Tekniset tiedot", command=tieto, font=("Roboto", "14"))
    tieto.grid(row=1, column=0, sticky="w e")
    tieto2 = Button(nappibox, text="Musiikki", padx=76, command=tieto2, font=("Roboto", "14"))
    tieto2.grid(row=3, column=0, sticky="w e")
    tieto3 = Button(nappibox, text="Tietoja meistä", padx=76, command=tieto3, font=("Roboto", "14"))
    tieto3.grid(row=2, column=0, sticky="w e")
    tietojal = Label(tekstibox, text="Paina nappeja katsoaksesi informaatiota", padx=10, pady=10, wraplength=350, bg="black", fg="white", font=("Roboto", "14"))
    tietojal.grid(row=0, column=1)

def update():
    global valintanro
    global tekstinro
    if tekstilista[tekstinro] == "kala":
        kuval.config(image=kuva_kala)
        tekstinro += 1


    if valintanro == 0 and tekstilista[tekstinro] != " ":
        teksti.config(text=tekstilista[tekstinro])
        tekstinro += 1
    elif valintanro == 1 and valinta1l[tekstinro] != " ":
        teksti.config(text=valinta1l[tekstinro])
        tekstinro += 1
    elif valintanro == 2 and valinta2l[tekstinro] != " ":
        teksti.config(text=valinta2l[tekstinro])
        tekstinro += 1
    elif valintanro == 3 and valinta3l[tekstinro] != " ":
        teksti.config(text=valinta3l[tekstinro])
        tekstinro += 1

    elif valintanro == 1 and valinta1l[tekstinro] == " ":
        teksti.config(text=tekstilista[tekstinro])
        tekstinro += 1
        valintanro = 0

    elif valintanro == 2 and valinta2l[tekstinro] == " ":
        teksti.config(text=tekstilista[tekstinro])
        tekstinro += 1
        valintanro = 0

    elif valintanro == 3 and valinta3l[tekstinro] == " ":
        teksti.config(text=tekstilista[tekstinro])
        tekstinro += 1
        valintanro = 0

    

def valinta1():
    global valintanro
    if tekstinro == 4:
        kuval.config(image=kuva_kylantalo)
    elif tekstinro == 10:
        kuval.config(image=kuva_luola)
    valintanro = 1

def valinta2():
    global valintanro
    if tekstinro == 4:
        kuval.config(image=kuva_metsa)
    elif tekstinro == 10:
        kuval.config(image=kuva_luola)
    valintanro = 2

def valinta3():
    global valintanro
    if tekstinro == 4:
        kuval.config(image=kuva_kirkko)
    elif tekstinro == 10:
        kuval.config(image=kuva_metsa)
    valintanro = 3





kuval = Label(ulkofraami, image=kuva_kmarket)
kuval.grid(row=0,column=0)

teksti = Label(tekstifraami, text=t1, bd=12, bg="black", foreground="white", font=("Roboto", "14"))
teksti.grid(row=0, column=0)

tekstilista = [t1, "kala", t12, kysymys1, " ", " ", " ", t2, t21, kysymys2, " ", " ", " "]

valinta1l = [" ", " ", " ", " ", t1_1, t1_12, t1_13, " ", " ", " ", t2_1, t2_12, t2_13, "KUOLIT\n\n"]
valinta2l = [" ", " ", " ", " ", t1_2, t1_21, t1_22, " ", " ", " ", t2_2, "KUOLIT\n\n"]
valinta3l = [" ", " ", " ", " ", t1_3, t1_31, t1_32, " ", " ", " ", t2_3, "KUOLIT\n\n"]

seuraava = Button(nappifraami, text="Seuraava", padx=10, command=update, font=("Roboto", "14"))
seuraava.grid(row=0, column=0)
stats = Button(nappifraami, text="Tiedot", padx=10, command=tietoja, font=("Roboto", "14"))
stats.grid(row=0, column=1)
valinta1 = Button(nappifraami, text="valinta 1", padx=10, command=valinta1, font=("Roboto", "14"))
valinta1.grid(row=0, column=2)
valinta2 = Button(nappifraami, text="valinta 2", padx=10, command=valinta2, font=("Roboto", "14"))
valinta2.grid(row=0, column=3)
valinta3 = Button(nappifraami, text="valinta 3", padx=10, command=valinta3, font=("Roboto", "14"))
valinta3.grid(row=0, column=4)

root.mainloop()
