#for numero in range(1, 21):
#    print(numero)

#vocales=[ 'a', 'e', 'i', 'o', 'u']
#siempre se usan corchetes para hacer una lista
#print(vocales[0])
#print(vocales[1])
#print(vocales[2])

#for numero in range(0, 5):
#  print(vocales[numero])

#for vocal in vocales:
#    print(vocal)

#crear una lista de 5 colores,, recorrer la lista y cuando encuentre el color rojo, terminara el programa y nos mostrara un mensaje que diga que encontro el color rojo

#colores=['azul', 'naranja', 'verde', 'rojo', 'amarillo']
#for color in colores:
#    if color=='rojo':
#        print('encontrado')
#        break
#    print(color)

#agregar contenido o elementos al final de una lista, existe un metodo
#APPEND
#lista=[]
#print(lista)
#dato1=input('ingresa una fruta: ')
#lista.append(dato1) 
#print(lista)
#dato2=input('ingresa una segunda fruta: ')
#lista.append(dato2) 
#print(lista)

##EJERCICIO
#crear un programa que me deje ingresar datos en una lista vacia
#en caso de que el usuario ingrese la palabra'si' el programa dejara de pedir datosl


texto=[]
while True:
    dato1=input('ingresa un la palbra o letra: ')
    if dato1 =='si':
        break
    texto.append(dato1)
print(texto)
    
            
texto=[]
condicion=1
while True:
    dato1=input('ingresa un la palbra o letra: ')
    if dato1 =='si':
        condicion=0
    texto.append(dato1)
print(texto)




