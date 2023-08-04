# Crea un programa que analice texto y obtenga:
#=>Número total de palabras (no espacios).
#=>Número de oraciones del texto (cada vez que aparecen una coma).
#=>Encuentre la palabra más larga. Todo esto utilizando un único bucle.

#Entrada=>"soy un texto escrito por pc, y hoy hace mucho frio"

#palabras= 11
#oraciones= 2
#texto largo= escrito

texto=input('ingresa un texto: ')
palabras=0
longitud= len(texto.split())
oraciones=len(texto.split(","))

palabra_mas_largo=" "
    
for b in texto.split():
    palabras+=1
    if len(b)>len(palabra_mas_largo):
            palabra_mas_largo=b

  

print(f"""  cantidad de palabras:{longitud}
    cantidad de oraciones:{oraciones}
    palabra mas larga:{palabra_mas_largo}""")

    
