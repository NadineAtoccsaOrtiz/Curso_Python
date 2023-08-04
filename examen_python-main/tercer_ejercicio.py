# Crea una función que reciba dos cadenas de texto casi iguales, a excepción de uno o varios caracteres. 
# La función debe encontrarlos y retornarlos en formato lista/array.
#  Ambas cadenas de texto deben ser iguales en longitud.
#Las cadenas de texto son iguales elemento a elemento.
#No se pueden utilizar operaciones propias del lenguaje que lo resuelvan directamente. Ejemplos:
# Me llamo jose / Me llemo jese -> ["e", "o"]
#hola como estas / holi come estus -> ["i", "e", "u"]

def diferencias(texto1,texto2):
    diferent=[]
    for a in range(len(texto1)):
        if texto1[a] !=texto2[a]:
            diferent.append(texto1[a])
    return diferent
texto1=input('ingresa el primer texto: ')
texto2=input('ingresa el segundo texto: ')
result=diferencias(texto1,texto2)
print("las diferencias son :", result)
