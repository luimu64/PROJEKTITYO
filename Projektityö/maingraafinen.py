from tkinter import *

root = Tk()
root.title("Isekai.py")
root.geometry("1200x600")
fraami = LabelFrame(root, text="Kontrollit:", padx=50, pady=5)
fraami.pack()

intro = "1, 2, 3...  =  vaihtoehtojen valitsemisnäppäimet jos ei toisin sanota\nvälilyönti pohjassa  =  skippaa tekstin loppuun"

teksti = Label(fraami, text=intro)
teksti.pack()

strnappi = Button(root, text="Aloita!", padx=50)
strnappi.pack()

root.mainloop()