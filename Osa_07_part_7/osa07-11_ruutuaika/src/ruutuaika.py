# tee ratkaisu tänne,



from datetime import datetime, timedelta

def ruutuaika():

    datat = {}
    kokonaisminuutit = 0
    KAminuutit = 0

    tiedosto_nimi = input("Tiedosto: ")
    aloituspaiva = input("Aloituspäivä: ")
    montakoPv = int(input("Moneltako päivältä: "))

    print("Anna ruutuajat kunakin päivänä minuutteina (TV/Tietokone/Mobiililaite")

    aloituspaiva = datetime.strptime(aloituspaiva, "%d.%m.%y")

    paivienmaara = timedelta(days=montakoPv)

    lopetuspaiva = aloituspaiva + paivienmaara

    lopetuspaiva = datetime.strptime(lopetuspaiva, "%d.%m.%y")

    with open(tiedosto_nimi,"a") as tiedosto:
        tiedosto.write(f"Ajanjakso: {aloituspaiva}-{lopetuspaiva}\n")
    
    e = 0

    for paiva in range(aloituspaiva,lopetuspaiva):

        paiva = datetime.strptime(paiva, "%d.%m.%y")

        ruutuaika = input(f"Ruutuaika {paiva}:")

        ruutuaika = ruutuaika.replace(" ","/")
        minuutit = ruutuaika.split("/")

        i = 0
        for minat in minuutit:
            i += int(minat)

        kokonaisminuutit += i
        
        for määrä in minuutit:
            e += 1
        
        datat[f"{paiva}"] = ruutuaika
    
    KAminuutit += float(kokonaisminuutit/e)
    
    with open(tiedosto_nimi,"a") as tiedosto:

        tiedosto.write(f"Yht. minuutteja: {kokonaisminuutit}\n")
        tiedosto.write(f"Keskim. minuutteja {KAminuutit}\n")

        for avain,arvo in datat.items():
            tiedosto.write(f"{avain}: {arvo}\n")

ruutuaika()

       