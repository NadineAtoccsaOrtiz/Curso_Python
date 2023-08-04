# Escribe un programa que reciba un texto y transforme lenguaje natural a "lenguaje hacker" 
# (conocido realmente como "leet" o "1337"). Este lenguaje se caracteriza por sustituir caracteres
#  alfanuméricos. Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)  
# con el alfabeto y los números en "leet". (Usa la primera opción de cada transformación solo para reemplazar 
# vocales: Por ejemplo "4" para la "a")
#ejemplo
#entrada==>eucalipto
#salida==>3(_)c4l1pt0

def lenguaje_hacker(texto):
    vocales={
        'a'='4',
        'e'='3',
        'i'='1',
        'o'='0',
        't'='7'
    }
    fusion=""
    for letras in texto:
        letras_min=letras.lower()
        fusion+=vocales.get(letras_min,letras)
    return fusion

    texto=input('ingresa un palabra para convertirlo: ')
    texto_fusion=lenguaje_hacker(texto)
    print(f"""texto_fusion:{texto_fusion} """)