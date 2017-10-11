def esMayorMenosOIgual(listaNum,numeroAComparar):
    menores=[]
    mayores=[]
    iguales=[]
    for x in listaNum:
        if x<numeroAComparar:
            menores.append(x)
        elif x>numeroAComparar:
            mayores.append(x)
        else:
            iguales.append(x)
    print("Numeros menores que "+str(numeroAComparar)+": "+str(menores))
    print("Numeros mayores que " + str(numeroAComparar) + ": " + str(mayores))
    print("Numeros iguales que " + str(numeroAComparar) + ": " + str(iguales))

esMayorMenosOIgual((-99,1,2,3,4,4,4,6,7,8,10,78538567,345),4)