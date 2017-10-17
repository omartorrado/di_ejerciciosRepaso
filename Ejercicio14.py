import unicodedata

def numPalabra(frase):
    listaPalabras=[]
    fraseSinAcentos=""
    repeticionesPalabra={}
    for x in frase:
        fraseSinAcentos+=unicodedata.normalize('NFD',x)[0]
    fraseSinAcentos=fraseSinAcentos.lower()
    listaPalabras=fraseSinAcentos.split(" ")
    print(listaPalabras)
    for x in listaPalabras:
        vecesRepetida=0
        if x not in repeticionesPalabra:
            for y in listaPalabras:
                if x==y:
                    vecesRepetida+=1
                    print(x,"=",y,"vecesRepetida:",vecesRepetida)
                repeticionesPalabra[x] = vecesRepetida
    print(repeticionesPalabra)

numPalabra("En un lugar de la Mancha en la Mancha")