##entrada
frutas=[]
while len(frutas)<5:
    nuevafruta=input('ingresa una fruta: ')
    for fruta in frutas:
        if len(nuevafruta)==len(fruta):
            print('misma longitud ')
    if nuevafruta in frutas:
        print('esta fruta ya existe huevonaso; ingfresa otra fruta pendejo: ')
    else:
        frutas.append(nuevafruta)
#proceso
def textolargo(array):
    longitudtexto=0
    mostrarfruta=''
    for index in range(0,len(array)):
        if len(array[index])>longitudtexto:
            longitudtexto=len(array[index])
            mostrarfruta=array[index]
    return mostrarfruta
#salida
print(textolargo(frutas))
