# Kirjoita ratkaisu tähän


def negatiivisesta_positiiviseen():

    value = int(input("Anna luku: "))
    for luku in range(-value, value+1):
        if luku != 0:
            print(luku)

negatiivisesta_positiiviseen()