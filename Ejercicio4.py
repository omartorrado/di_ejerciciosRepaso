def bisiesto(año):
    if (año%4)==0 and (año%100)!=0:
        print("Bisiesto")
    elif (año%4)==0 and (año%400)==0:
        print("Bisiesto")
    else:
        print("No bisiesto")

bisiesto(2000)
bisiesto(2100)
bisiesto(2200)
bisiesto(2400)
bisiesto(100)
bisiesto(2017)