import time
import sys
import keyboard

t1 = """
    Pimeänä ja kosteana tammikuun perjantai iltana olet menossa 
    ostamaan kaljaa k-marketista rankan amis päivän jälkeen. Matkalla 
    kuitenkin virolainen raksamies ajaa kännissä päältäsi saabilla. 
    Heräät aamulla joesta mutta tuntuu että jotain on pielessä. 
    Vesi on liian lämmintä ja on liian kirkasta ollakseen tammikuu
    saati sitten suomi ollenkaan. Huomaaat että sinulla on kova nälkä.\n"""


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

    \u2588\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580
    \u258C  Kontrollit:
    \u258C  1, 2, 3     =   vaihtoehtojen valitsemis 
    \u258C                  näppäimet jos ei muuta sanota
    \u258C  välilyönti  =   skippaa tekstin loppuun
    \u258C  pohjassa
    \u2588     
""")
time.sleep(5)
animoija(t1)
kysymys = input("""
    1. vaihtoehto
    Jää ojaan kalastamaan. Sinulla ei ole onkea mutta kyllähän 
    karhutkin voivat kalaa napata käsillä.\n
    2. vaihtoehto
    Lähde etsimään ruokaa luonnosta.\n
    3. vaihtoehto
    Seuraa joen viereistä polkua toivoes löytäväsi siviilisaatiota.\n   

""")
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
time.sleep(5)