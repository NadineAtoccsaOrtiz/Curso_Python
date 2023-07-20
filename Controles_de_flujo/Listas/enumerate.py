#lista=['a','e','i']

#for indice, valor in enumerate(lista):
    #if valor == 'i':
        #print(indice, valor)

#crear una lista que va contener los numeros del 1 al 10 
#crear una funcion que me permita recibir como parametro una lista
#la funcion tendra que retornar un nuevo array con todos los numeros pares que existen del 1 a 10

#lista=[1,2,3,4,5,6,7,8,9,10]
#def pares(lista):
#    nuevo=[]
#    for pares, valor in enumerate(lista):
#        if valor % 2 == 0:
#           nuevo.append(valor)
#    return nuevo
#print(pares(lista))

#texto='131 2543 7698'
#print(list(texto))
#print(texto.split(' '))

#hacer un programa que pida al usuario un texto
#y evaluar con una funcion la cantidad de vocales a que tiene el texto

texto=input('ingresa un texto: ')
def vocales(texto:str)->int:
    cantidad=0
    for valor in list(texto):
        if valor =='a':
            cantidad+=1
    return cantidad
print(f"El texto tiene: {vocales(texto)} vocales a")

#
#
#



