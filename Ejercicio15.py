import random

def tiradaMediaDados(dados,caras):
    resultados=0
    for x in range(1,dados+1):
        numero=random.randrange(1,caras+1)
        print("tirada:",numero)
        resultados+=numero
        print("Total "+str(resultados))
        return resultados

tiradas=[]
for x in range (0,20):
    tiradas.append(tiradaMediaDados(2,6))
tiradas.sort()
for x in range (1,7):
    print("Ha salido",tiradas.count(x)," veces el",x)