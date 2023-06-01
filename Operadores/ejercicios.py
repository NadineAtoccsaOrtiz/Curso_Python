#EJERCICIO 1
radiocirculo=int(input('ingrese el radio del circulo'))
area=3.14*(radiocirculo**2)
#print(area)
#print (f'El area el circulo es{area}')
print (f"""
===============================
El area el circulo es {area}
==============================
""")

#EJERCICIO 2
radio=int(input('ingrese el radio de la esfera'))
volumen=4/3*3.14*(radio**3)
print (f"""
===============================
El volumen de la esfera es {volumen}
==============================
""")

#EJERCICIO 3
base=int(input('ingrese la base del trtiangulo'))
altura=int(input('ingrese la altura del triangulo'))
area=base*altura/2
print (f"""
===============================
El area el triangulo es {area}
==============================
""")


#obtenercadena='hola'
#print(obtenercadena[-3])

#trocear='hola a todos'
#print(trocear[3:5])
#print(trocear[:-3])

#ultimostring='texto largo'
#print(len(ultimostring))
#longitud=(len(ultimostring))
#print(ultimostring[longitud-1])

#pertenencia
#pertenencia='hola' in 'hola mundo'
#print(pertenencia)

#con='a'<'A' ##codigo ascci
#print(con)

#EJERCICIOS DE CONVERSIONES
nombre=input("Ingresa tu nombre")
apellido=input("Ingresa tu apellido")
print(f"""
===========================================
"Hola {nombre}, {apellido}
Bienvenid@ al programa👾"
===========================================
""")

#EJERCICIO 2
TEXTO=input("Ingrese un texto")
CantidadTexto=len(TEXTO)
print(CantidadTexto)

#EJRCICIO 3
comparacion=int(input('Ingresa un numero para comparar'))
if comparacion!=20:
    print("afuera")
else:
    print("adentro")

#EJERCICIO 4
edad=int(input('ingresa tu edad'))
if edad<18:
    print("Eres menor de edad")
if edad>18:
    print("Eres mayor de edad")

#TAREA 1:
DNI=input('Ingresa tu DNI')
LongDNI=(len(DNI))
if LongDNI==8:	
    nombre=input('Ingresa tu nombre')	
    print(f"""	
    Bienvenid@, {nombre}	
    """)
else:	
    print('Error, vuelva a ingresar el DNI')

#TAREA 2:
apellido=input("Ingresa tu primer apellido")
comparacion=apellido[-2:]
if comparacion=='ez':
    print("Eres casi español")
if comparacion=='es':
    print("Eres casi peruano")

#TAREA 3: SUMA DE DIGITOS
DNI=input('Ingresa tu DNI')
longitud=len(DNI)
if longitud==8:
	sumadigitos=int(DNI[-1:])+int(DNI[:1])
	print(f"""
	El primer digito de su DNI es:
		{int(DNI[-1:])}
	El ltimo digito de su DNI es:
		{int(DNI[:1])}
	La suma de ambos digitos es:
    		{sumadigitos}
	""")
else:
	print("Error, vuelva a ingresar su DNI")

#TAREA 4:AÑO BICIESTO
año =int(input('Ingresa el año que deseas evaluar'))
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print(f"""
    Estamos evaluando su respuesta
    ..............................
    Respuesta:

            --> El año que ingreso es bisiesto😎
    """)
else:
	print(f"""
    Estamos evaluando su respuesta
    ..............................
    Respuesta:

            ---> El año que ingreso no es bisiesto🙁
    """)