import datos
while len(datos.lista)<5:
    dato=input('Ingresa un dato: ')
    datos.lista.append(dato)
for texto in range(0, len(datos.lista)):
    if datos.lista[texto]== 'disco':
        datos.palabra=datos.lista[texto]
        datos.indice=texto



