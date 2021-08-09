# tee ratkaisu tänne


import datetime

def onko_validi(hetu: str):

    synt_vuosi = int(hetu[4:6])
    synt_kk = int(hetu[2:4])
    synt_paiva = int(hetu[:2]) 

    jakojaannos = int(hetu[7:10]) % 31
    jakojaannos_indeksi = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    tarkastusmerkki = jakojaannos_indeksi[jakojaannos]

    syntyma_aika = datetime.datetime(synt_vuosi,synt_kk,synt_paiva)
    nykyhetki = datetime.datetime.now()

    if syntyma_aika > nykyhetki:
        return False

    elif hetu[4] in range(1,9) and hetu[6] != "-":
        return False
    
    elif hetu[4] == "0" and hetu[6] != "A":
        return False
    
    elif hetu[-1] != tarkastusmerkki:
        return False

    else:
        return True

print(onko_validi("270897-605D"))

peepee = "270897-605D"

print(peepee[4])
numero = int(peepee[0:3])
print(numero - 10)