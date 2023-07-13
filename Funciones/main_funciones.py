#hacemos uso de la palabra reservada def
#segundo le ponemos un nombre a nuestra funcion, describe lo qie hace la funcion
#establemos los parametros que resivira nuestra funcion

#def saludo( ):
#	print(f"""
#	Hola, este es un mensaje de bienvenida.#...
#	cargando....
#	""")
#saludo( )

#int edad='15 '

#error por que estoy indicando un dato entero y estoy poniendo un dato texto por que el 15 lleva comilas y las conillas indican un dato texto

#RETURN
#el dato de retorno Sirve para retornar

#def saludo( ):
#	mensaje="""
#	Hola, este es un mensaje de #bienvenida....
#	cargando....
#	"""
#	return mensaje
	
#print(saludo( ))

def mensaje(resultado):
 	newmensaje=f"""el resultado es 		{resultado}
 	"""
 	return newmensaje 
def mensajebienvenida(nombre):
	nuevomensaje1=f"""hola, bienvenido al programa, {nombre}
	"""
	return nuevomensaje1
def suma(numero1, numero2):
 	operacion=numero1+numero2
 	return mensaje(operacion)
def resta(numero1, numero2):
	operacion=numero1-numero2return

ingresanombre=input('ingresa su nombre: ')
print(mensajebienvenida(ingresanombre))
primerdato=int(input('ingresa el primer numero: '))
segundodato=int(input('ingrese el segundo numero'))
print(suma(primerdato, segundodato))
 
