# Crea una funciones, encargada de detectar si una cadena de texto es un heterograma.
#heterograma ==> frase que no contiene letra repetida ejem:centrifugado.
# Function to Check whether a given string is Heterogram or not
 
def heterograma(lista):
    letras={}
    for a in lista:
        if a in letras:
            return False
        letras[a]=1
    return True
lista=input('ingresa una palabra: ')
if heterograma(lista):
    print(f"""{lista}', es una palabra heterograma.""")
else:
    print(f"""{lista}', no es una palabra heterograma.""")