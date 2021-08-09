# TEE RATKAISUSI TÄHÄN:
import re


def on_viikonpaiva(merkkijono: str):

    viikonpaivat = ["ma","ti","ke","to","pe","la","su"]

    for paiva in viikonpaivat:
        if re.match(paiva, merkkijono):
            return True
    
    else:
        return False



def kaikki_vokaaleja(merkkijono: str,):

    vokaalit = "^[a|e|i|u|o|y|ä|ö|å]*$"
    # vokaalit = "^[aeiuoyäöå]*$"

    if re.match(vokaalit, merkkijono):
        return True
    else:
        return False

def kellonaika(merkkijono: str):

    tunnit = []
    minuutit = []
    sekunnit = []

    for i in range(0,25):
        tunnit.append(str(i))

    
    for i in range(0,61):
        minuutit.append(str(i))
        sekunnit.append(str(i))

    
    if merkkijono[0:1] not in tunnit:
        return False
    
    elif merkkijono[2] != ":":
        return False
    
    elif merkkijono[3:4] not in minuutit:
        return False
    
    elif merkkijono[5] != ":":
        return False
    
    elif merkkijono[6:7] not in sekunnit:
        return False
    
    else:
        return True



    # tunnit = "[00-24]"
    # minuutit = "[00-60]"
    # sekunnit = "[00-60]"

    # if merkkijono[2] and merkkijono[5] != ":":
    #     return False
    

    # if merkkijono[0:1] in tunnit and merkkijono[2] == ":" and merkkijono[3:4] in minuutit and merkkijono[5] == ":" and merkkijono[6:7] in sekunnit:
    #     return True
    
    # else:
    #     return False
    
    
    

if __name__ == "__main__":
    print(on_viikonpaiva("ma"))
    print(on_viikonpaiva("pe"))
    print(on_viikonpaiva("tu"))

    print("")
    print("")

    print(kaikki_vokaaleja("eioueioieoieouyyyy"))
    print(kaikki_vokaaleja("saaaa"))

    print("")
    print("")
    
    print(kellonaika("25:01:01"))
            
        
