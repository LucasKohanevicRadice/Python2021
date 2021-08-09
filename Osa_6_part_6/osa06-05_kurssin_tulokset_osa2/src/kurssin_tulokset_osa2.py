# tee ratkaisu tänne



from os import popen, remove



if True:
    # tänne ei tulla
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
    koepisteet = input("Koepisteet: ")
else:
    # kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"
    koepisteet = "koepisteet1.csv"

op_tiedot = []
teht_tiedot = []
koe_p = []

with open(opiskelijatiedot) as tiedosto:

    for rivi in tiedosto:
        rivi = rivi.replace("\n", "")

        rivi = rivi.split(";")
        op_tiedot.append(rivi)


with open(tehtavatiedot) as tiedosto:

    for rivi in tiedosto:
        rivi = rivi.replace("\n", "")

        rivi = rivi.split(";")
        teht_tiedot.append(rivi)


with open(koepisteet) as tiedosto:

    for rivi in tiedosto:

        rivi = rivi.replace("\n", "")

        rivi = rivi.split(";")
        koe_p.append(rivi)


op_tiedot.pop(0)
teht_tiedot.pop(0)
koe_p.pop(0)


kurssitulokset = {}
koepiste_kirja = {}

for kaikki_tiedot in op_tiedot:

    kurssitulokset[kaikki_tiedot[0]] = f"{kaikki_tiedot[1]} {kaikki_tiedot[2]}"



for rivi in teht_tiedot:

    for indeksi, arvo in enumerate(rivi):

        if indeksi == 0:
            continue

        rivi[indeksi] = int(arvo)
    
    teht_summa = sum(rivi[1:])

    if teht_summa in range(4,8):

        koepiste_kirja[rivi[0]] = 1
    
    elif teht_summa in range(8,12):

        koepiste_kirja[rivi[0]] = 2
    
    elif teht_summa in range(12,16):

        koepiste_kirja[rivi[0]] = 3
    
    elif teht_summa in range(16,20):

        koepiste_kirja[rivi[0]] = 4
    
    elif teht_summa in range(20,24):

        koepiste_kirja[rivi[0]] = 5
    
    elif teht_summa in range(24,28):

        koepiste_kirja[rivi[0]] = 6
    
    elif teht_summa in range(28,32):

        koepiste_kirja[rivi[0]] = 7
    
    elif teht_summa in range(32,36):

        koepiste_kirja[rivi[0]] = 8
    
    elif teht_summa in range(36,40):

        koepiste_kirja[rivi[0]] = 9
    
    elif teht_summa >= 40:

        koepiste_kirja[rivi[0]] = 10
    
    else:

        koepiste_kirja[rivi[0]] = 0
    






sallitut = ["1","2","3","4","5","6","7","8","9","10"]

for rivi in koe_p:

    for indeksi, arvo in enumerate(rivi):

        if indeksi == 0:
            continue

        rivi[indeksi] = int(arvo)
    
    koepiste_kirja[rivi[0]] += sum(rivi[1:])
        

for avain, arvo in kurssitulokset.items():

    if koepiste_kirja[avain] in range(0,15):

        kurssitulokset[avain] += " 0"
    
    elif koepiste_kirja[avain] in range(15,18):

        kurssitulokset[avain] += " 1"
    
    elif koepiste_kirja[avain] in range(18,21):

        kurssitulokset[avain] += " 2"
    
    elif koepiste_kirja[avain] in range(21,24):

        kurssitulokset[avain] += " 3"
    
    elif koepiste_kirja[avain] in range(24,28):

        kurssitulokset[avain] += " 4"
    
    elif koepiste_kirja[avain] >= 28:

        kurssitulokset[avain] += " 5"



for oppilasnumero, op_ja_tehtavat in kurssitulokset.items():

    print(kurssitulokset[oppilasnumero])



