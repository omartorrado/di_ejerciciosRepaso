import unicodedata

def numPalabra(frase):
    listaPalabras=[]
    fraseSinAcentos=""
    repeticionesPalabra={}
    for x in frase:
        fraseSinAcentos+=unicodedata.normalize('NFD',x)[0]
        print(x)
    fraseSinAcentos=fraseSinAcentos.lower()
    listaPalabras=fraseSinAcentos.split(" ")



    print(listaPalabras)

numPalabra("En un lugar de la Mancha en la Mancha")