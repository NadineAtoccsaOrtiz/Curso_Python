#pedir a un usuario una lista de 5 elemntos , si en la lista contiene la palabra disco 
#mostar la palabra y la ubicacion de sun iondice positivo


lista=[]
indice=0
palabra=' '
while len (lista)<5:
    dato=input('Ingresa un dato: ')
    lista.append(dato)
for texto in range(0, len(lista)):
    if lista[texto]== 'disco':
        palabra=lista[texto]
        indice=texto
print(f"""
el texto disco se encuentra en el indice, {indice}
y el texto es {palabra}
""")