# Kirjoita ratkaisu tähän

oikea = "Visual studio code"


while True:

    kysy = input("Editori: ")


    if kysy.lower() == oikea.lower():
        print("loistava valinta!")
        break
    
    elif kysy.lower() == "word" or  kysy.lower() == "notepad":
        print("surkea")
    
    else:
        print("ei ole hyvä")

