import math


while 1:
    x=  float(input ('Indica el valor de x: '))
    y=  float(input ('Indica el valor de y: '))

    print ('Selecciona la operación que desees operar')
    print ('1. Sumar')
    print ('2. Restar')
    print ('3. Multiplicar')
    print ('4. Dividir')
    print ('5. Potencia')
    print ('6. Logaritmo (logaritmo del primer numero [x]) ')

    n= int(input('¿Cuál opción deseas? '))

    if n==1: 
        Resultado= x+y
        print(Resultado)
    elif n==2:
        Resultado= x-y
        print(Resultado)
    elif n==3:
        Resultado= x+y
        print(Resultado)
    elif n==4 and y!=0:
        Resultado= x/y
        print(Resultado)
    elif n==5:
        Resultado= x**y
        print(Resultado)
    elif n==6 and x>0:
        Resultado= math.log10(x)
        print(Resultado)
    else:
        print ('NO se encuentra, prueba otra vez')

