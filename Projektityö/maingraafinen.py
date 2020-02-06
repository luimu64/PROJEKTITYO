from tkinter import *

root = Tk()
root.title("Isekai.py")
root.geometry("1000x400")
fraami = LabelFrame(root, text="Kontrollit", padx=50, pady=5)
fraami.pack()

kontrollit = "1, 2, 3...  =  vaihtoehtojen valitsemisnäppäimet jos ei toisin sanota\nvälilyönti pohjassa  =  skippaa tekstin loppuun"

teksti = Label(fraami, text=kontrollit)
teksti.pack()
def pohjateksti(teksti):
    teksti = Label(fraami, text=" Pimeänä ja kosteana tammikuun perjantai iltana olet menossa ostamaan kaljaa k-marketista rankan amispäivän jälkeen. Matkalla kuitenkin virolainen raksamies ajaa kännissä päältäsi saabilla. Heräät aamulla joesta mutta tuntuu että jotain on pielessä. Vesi on liian lämmintä ja on liian kirkasta ollakseen tammikuusaati sitten suomi ollenkaan. Huomaaat että sinulla on kova nälkä")
    teksti.pack()
    

strnappi = Button(root, text="Aloita!", padx=50, command=pohjateksti("s"))
strnappi.pack()



root.mainloop()