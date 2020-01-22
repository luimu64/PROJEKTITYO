import time
import sys
import keyboard

t1 = """Pimeänä ja kosteana tammikuun perjantai iltana olet menossa 
ostamaan kaljaa k-marketista rankan amis päivän jälkeen. Matkalla 
kuitenkin virolainen raksamies ajaa Kännissä päältäsi saabilla. 
Heräät aamulla joesta mutta tuntuu että jotain on pielessä. 
Vesi on liian lämmintä ja on liian kirkasta ollakseen tammikuu
saati sitten suomi ollenkaan. Huomaaat että sinulla on kova nälkä.\n"""

t1_1 = """Teksti kaksi"""

#https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
def animoija(s):
    for a in s:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.07)
        if keyboard.is_pressed('space'):
            refreshi()
            print(s)
            break
        

def refreshi():
    i = 0
    while i < 100:
        print("\n")
        i += 1

refreshi()
animoija(t1)
input("""
1.  Jää ojaan kalastamaan sinulla ei ole onkea mutta kyllähän 
    karhutkin voivat kalaa napata käsillä\n
2.  Lähde etsimään ruokaa luonnosta\n
3.  Seuraa joen viereistä polkua toivoes löytäväsi siviilisaatiota\n

""")
time.sleep(5)