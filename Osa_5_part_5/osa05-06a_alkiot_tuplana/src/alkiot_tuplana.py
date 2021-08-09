# tee ratkaisu tänne



# def tuplaa_alkiot(lista: list):

#     tuplatut = []

#     for alkio in lista:
#         tuplatut.append(alkio*2)
    
#     return tuplatut


a = [1, 3, 5]
b = a
a[:] = [x + 2 for x in a]
print(b)

