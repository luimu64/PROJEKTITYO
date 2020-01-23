import time
import sys
import keyboard

intro = """
    Pimeänä ja kosteana tammikuun perjantai iltana olet menossa 
    ostamaan kaljaa k-marketista rankan amispäivän jälkeen. Matkalla 
    kuitenkin virolainen raksamies ajaa kännissä päältäsi saabilla. 
    Heräät aamulla joesta mutta tuntuu että jotain on pielessä. 
    Vesi on liian lämmintä ja on liian kirkasta ollakseen tammikuu
    saati sitten suomi ollenkaan. Huomaaat että sinulla on kova nälkä.\n"""


#https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
def animoija(s):
    for a in s:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(delay)
        if keyboard.is_pressed('space'):
            refreshi()
            print(s)
            break
        

def refreshi():
    i = 0
    while i < 100:
        print("\n")
        i += 1


#ohjelman alku
refreshi()
print("""
     ______                      __                  __                                   
    /      |                    /  |                /  |                                  
    $$$$$$/   _______   ______  $$ |   __   ______  $$/       ______   __    __   ______  
      $$ |   /       | /      \\ $$ |  /  | /      \\ /  |     /      \\ / \\  /  | /      \\ 
      $$ |  /$$$$$$$/ /$$$$$$  |$$ |_/$$/  $$$$$$  |$$ |    /$$$$$$  |$$  \\/$$/ /$$$$$$  |
      $$ |  $$      \\ $$    $$ |$$   $$<   /    $$ |$$ |    $$    $$ | $$  $$<  $$    $$ |
     _$$ |_  $$$$$$  |$$$$$$$$/ $$$$$$  \\ /$$$$$$$ |$$ | __ $$$$$$$$/  /$$$$  \\ $$$$$$$$/ 
    / $$   |/     $$/ $$       |$$ | $$  |$$    $$ |$$ |/  |$$       |/$$/ $$  |$$       |
    $$$$$$/ $$$$$$$/   $$$$$$$/ $$/   $$/  $$$$$$$/ $$/ $$/  $$$$$$$/ $$/   $$/  $$$$$$$/ 

    \u2588\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2588
    \u258C  Kontrollit:                                                                       \u2590
    \u258C  1, 2, 3...  =   vaihtoehtojen valitsemis-                                         \u2590
    \u258C                  näppäimet jos ei toisin sanota                                    \u2590
    \u258C  välilyönti  =   skippaa tekstin loppuun                                           \u2590
    \u258C  pohjassa                                                                          \u2590
    \u2588\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2588
""")
delay = float(input("    Anna tekstin nopeus, 0.5 - 0 (0.05 suositeltava):\n\u2002\u2002\u2002\u2002\u2591"))
animoija(intro)
kysymys = input("""
    1. vaihtoehto
    Jää ojaan kalastamaan. Sinulla ei ole onkea mutta kyllähän 
    karhutkin voivat kalaa napata käsillä.\n
    2. vaihtoehto
    Lähde etsimään ruokaa luonnosta.\n
    3. vaihtoehto
    Seuraa joen viereistä polkua toivoen löytäväsi siviilisaatiota.\n\u2002\u2002\u2002\u2002\u2591""")
kysymys = kysymys.replace(" ", "")
if kysymys == "1":
    t1_1 = """
    Yrität kalastaa mutta se on ilman kynsiä yllättävän hankalaa. 
    kalat ovat limaisia ja liukuvat käsistäsi. Nukahdat ojaan 
    nälästä, väsymyksestä ja hämmennyksestä rankan päivän jälkeen.
    Heräät tuntemattomassa huoneesa sängyltä ja huomaat että sinua 
    tarkkaillaan. Tarkkalilija on nuorehko tyttö sängyn vieressä. 
    Hän kertoo nimekseen Nita ja 
    """
    animoija(t1_1)
elif kysymys == "2":
    t1_2 = """
    Lähdet tutkimaan läheistä metsää löytämättä mitään muuta kuin 
    tuntemattomia sieniä joita et uskalla syödä. Ihmeen kaupalla 
    löydät puskan vierestä kimpaleen grillattua lihaa ja kun menet 
    lähelle, "WHOOSH" lennähdät ilmaan ja jäät roikkumaan puustä 
    köyden varassa. Lihan ympärillä oli simppeli silmukka jota et 
    huomannut. Seuraavana aamuna setämiehen näköinen mies joka ei 
    näytä tyytyväiseltä napattuun riistaan vie sinut pienen kylän 
    kirkkoon jalkapuuhun.
    """
    animoija(t1_2)
time.sleep(5)