#TAREA, LIMITE 5
#animales=[]
#for numero in range(0,5):
#    datos =input('ingresa un  animal: ')
#    animales.append(datos)
#print(animales)

#METODO 2
#lista =[]

#while len(lista)<5:
#    dato=input('ingresa un dato: ')
#    lista.append(dato)
#
#print(f"""
#===================================
#los datos ingresados son:  {lista}
#===================================
#""")

#EJERCICIO 2
#Pedir al usuario un numero luego generar la tabla de multiplicar de dicho numero del 1 hasta el 12
#dato=int(input('INGRESA EL NUMERO QUE DESEAS MULTIPLICAR: '))
#for numero in range (1,13):
#    resultado=numero*dato
#    print(f"{numero}*{dato}={resultado}")

#EJERCICIO 3
#  2=2*1=2=2
#  3=3*2*1=6
#  4=4*3*2*1=24
#  5=5**4*3*2*1=120

#Hacer un programa que me pida un numero y me calcule su factorial:
#ejemplo 5 factorial igual a 120

dato=int(input('ingresa un numero: '))
factorial=1
if dato == 0:
    print('el factorial de 0 es 0')
else:
    for numero in range(1, dato+1):
        factorial=factorial*numero
    print(f"""
    --------------------------------------
    El factorial de {dato} es {factorial}
    -------------------------------------
    """)




