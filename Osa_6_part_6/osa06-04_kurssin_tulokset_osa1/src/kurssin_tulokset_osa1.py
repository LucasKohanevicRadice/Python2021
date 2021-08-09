# tee ratkaisu tänne


from os import popen, remove



if True:
    # tänne ei tulla
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
else:
    # kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"

op_tiedot = []
teht_tiedot = []

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

op_tiedot.pop(0)
teht_tiedot.pop(0)

kurssitulokset = {}

for kaikki_tiedot in op_tiedot:

    kurssitulokset[kaikki_tiedot[0]] = f"{kaikki_tiedot[1]} {kaikki_tiedot[2]}"



for rivi in teht_tiedot:

    for indeksi, arvo in enumerate(rivi):

        if indeksi == 0:
            continue

        rivi[indeksi] = int(arvo)


for avain, arvo in kurssitulokset.items():

    for kaikki_tiedot in teht_tiedot:

        if kaikki_tiedot[0] == avain:

            kurssitulokset[avain] += f" {sum(kaikki_tiedot[1:])}"



for oppilasnumero, op_ja_tehtavat in kurssitulokset.items():

    print(kurssitulokset[oppilasnumero])



