# tee ratkaisu tänne


import datetime

def kuinka_vanha():

    päivä = int(input("Päivä: "))
    kuukausi = int(input("Kuukausi: "))
    vuosi = int(input("Vuosi: "))

    syntyma_aika = datetime.datetime(vuosi,kuukausi, päivä)

    millenium = datetime.datetime(1999,12,31)

    erotus = millenium - syntyma_aika

    if syntyma_aika > millenium:
        print("Et ollut syntynyt kun vuosituhat vaihtui")
    
    else:
        print(f"Olit {erotus.days} päivää vanha kun vuosituhat vaihtui.")

kuinka_vanha()

