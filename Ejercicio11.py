def encajan(ficha1,ficha2):
    encajan=False
    for x in ficha1:
        for y in ficha2:
            if x==y:
                print("Encaja el "+str(x))
                encajan=True
    if encajan==False:
        print("No encaja ninguna ficha")
encajan((2,3),(4,6))
encajan((4,3),(4,6))
