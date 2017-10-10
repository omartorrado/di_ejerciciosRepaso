def bisiesto(año):
    if (año%4)==0 and (año%100)!=0:
        return True
    elif (año%4)==0 and (año%400)==0:
        return True
    else:
        return False

def fechaValida(dia,mes,año):
    if mes==2:
        if(bisiesto(año)==True):
            if dia<=29:
                print("Fecha valida")
            else:
                print("Fecha no valida")
        else:
            if dia<=28:
                print("Fecha valida")
            else:
                print("Fecha no valida")
    elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        if dia<=31:
            print("Fecha valida")
        else:
            print("Fecha no valida")
    elif mes==4 or mes==6 or mes==9 or mes==11:
        if dia<=30:
            print("Fecha valida")
        else:
            print("Fecha no valida")

fechaValida(31,1,1986)
fechaValida(29,2,2017)
