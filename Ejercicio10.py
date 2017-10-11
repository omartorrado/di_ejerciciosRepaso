def tuplaAlfa(x):
    tupla=x
    pos=1
    ordenado=True
    for y in tupla:
        if ordenado==True:
            if len(tupla)>pos:
                if y<=tupla[pos]:
                    #print("ok")
                    pos=pos+1
                else:
                    #print("No")
                    ordenado=False
            else:
                print(str(tupla)+"Esta ordenada")
        else:
            print(str(tupla)+"Esta desordenada")
            break
tuplaAlfa((1,2,3,4,5))
tuplaAlfa((10,4,4,4,4,5,10,100))
