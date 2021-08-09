# tee ratkaisu tänne


from string import ascii_letters, punctuation


def jaa_merkkeihin(merkkijono: str):
    import string

    engkirjaimet = ""
    välimerkit = ""
    laiminlyödyt = ""

    for merkit in merkkijono:

        if merkit in ascii_letters:

            engkirjaimet += merkit
        
        elif merkit in punctuation:

            välimerkit += merkit
        
        else:
            laiminlyödyt += merkit

    return engkirjaimet, välimerkit, laiminlyödyt

if __name__ == "__main__":
    merkit = jaa_merkkeihin("JOO TÄÄ ON VITUN SAIRAAN SÄÄTÄNÄN FÄNTSYY ÖÖÖÖ SAISKO VAIK RÖÖÖÖKIN")