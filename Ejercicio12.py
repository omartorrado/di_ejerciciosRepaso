def factorial(numeros):
    for x in numeros:
        factorial=1;
        for y in range(2,x+1):
            factorial=factorial*y
        print("el factorial de "+str(x)+" es "+str(factorial))

factorial((1,4,5,6,7,8))