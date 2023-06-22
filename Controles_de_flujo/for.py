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

colores=['azul', 'naranja', 'verde', 'rojo', 'amarillo']
for color in colores:
    if color=='rojo':
        print('encontrado')
        break
    print(color)
