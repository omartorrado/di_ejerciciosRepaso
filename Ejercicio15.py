import random

def tiradaMediaDados(dados,caras,numTirada):
    resultados=0
    for x in range(1,dados+1):
        numero=random.randrange(1,caras+1)
        print("tirada:"+str(numTirada),numero)
        resultados+=numero
    print("Total "+str(resultados))
    return resultados

def tirarXVeces(veces):
    tiradas=[]
    for x in range (0,veces):
        tiradas.append(tiradaMediaDados(2,6,x+1))
    tiradas.sort()
    for x in range (2,13):
        print("Ha salido",tiradas.count(x)," veces el",x)

tirarXVeces(50)