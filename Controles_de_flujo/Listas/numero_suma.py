lista=[2,5,8,4,1]

def sumanumeros(arraynumeros):
    totalsuma=0
    for numero in arraynumeros:
        totalsuma+=numero
    return totalsuma
print(sumanumeros(lista))

def numeromenor(arraynumeros):
    menor=arraynumeros[0]
    for numero in arraynumeros:
        if numero < menor:
            menor = numero
    return menor
print(numeromenor(lista))

def numeromayor(arraynumeros):
    mayor=arraynumeros[0]
    for numero in arraynumeros:
        if numero > mayor:
            mayor=numero
    return mayor
print(numeromayor(lista))

