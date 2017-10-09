def farCel(n):
    return (n-32)*(5/9)

for n in range(10,121,10):
    print(str(n)+"ªF son",farCel(n),"ªC")