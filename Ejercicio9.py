def alfabeticamente(frase1, frase2, posicion):
    frase1=frase1.lower()
    frase2=frase2.lower()
    posicion=posicion;
    if frase1[posicion]<frase2[posicion]:
        print(frase1,frase2)
    elif frase1[posicion]>frase2[posicion]:
        print(frase2,frase1)
    else:
        posicion+=1
        alfabeticamente(frase1, frase2, posicion)

alfabeticamente("pedro","Juan",0)