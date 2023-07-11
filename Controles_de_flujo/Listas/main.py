## CONTROLES DE FLUJO

#CONDICIONALES
###se realiza algo si se cumple cierta condicion
### bloques
#### cuando nosotros utilicemos cualquier control de flujo o funciones  el codigo que se debe ejecutar depues debera nestar definida por bloques o identificaciones


#ejercicio
#evaluar si es menor de 17 monstrar com mensaje cana si es mayor a 18 monstara come y si es mayor a 40 monstrar ya esta usado

#entrada de datos
#dead= input ('ingrese un edad: ')
#if edad < 17 :
#  print('cana')
#f edad > 40 :
#  print('ya esta usado')
    
    
# hacer  un programa que pida al usuario su dni si la longuitud del dni es 8  que pida Su nombre  y lo muestre por consola si la longuitud del dni es mayor o menor a 8 que le  mjestre un mensaje de erorr
#datos de entrada
dniUsuario= input(" Ingrese si DNI: ")
longitudDni=len(dniUsuario)
#proceso
if longitudDni== 8 :
    #entrada
    nombre=input("Ingresa tu nombre: ")
    #proceso
    mensaje=f"""hola bienvenido , {nombre}"""
    #salida de dato
    print(mensaje)
else:
    print("El dni ingresado es incorrecto ")



# hacer un programa que pida al usuario ingresar el primer apellido si su apellido tiene en como ultimos caractereslas letras--ez-- mostrar un mensaje que diga casi eres español si los carcteres finales  son --es--  que diga eres casi peruano

# datos de entrada 
Apellido= input ("Ingrese su apellido Paterno:  ")
comparacion=Apellido[-2:]
if comparacion=='ez' :
  print("eres casi español")
if comparacion=='es':
  print('eres casi peruano')

## hacer un programa que le pida aun usuario su dni y compruebe que sea de 8 digitos, si es correcto que sume el primer numero del dni, mostrarpor la pantalla la suma y el resultado
# ejemplo:
## ingresa=12345678
## "1+8=9"


# hacer un programa que permita que el usuario ingrese un año  y me de com respuesta si es bisiesto o no




 #if 
vocal= input('ingrese  un a vocal minuscula: ' )
match vocal:
  case'a' :
    print('es una vocal')
  case'e' :
    print('es una vocal')
  case'i' :
    print('es una vocal')
  case'o' :
    print('es una vocal')
  case'u' :
    print('es una vocal')
    
    
#2
vocales='aeiou'
vocalmayus='AEIOU'
ingresevocal=input('Ingrese una vocal minuscula: ')
if ingresevocal in vocales:
  print('es una vocal minuscula')
elif ingresevocal in vocalmayus:
  print('es una vocal mayuscula')
else:
  print('no es una vocal ni minuscula ni mayuscula')
  


## 3 FOR
#PARA ENLISTAR COSAS USAR LAS COMAS (, )
vocales=[ 'a', 'e', 'i', 'o', 'u']
#siempre se usan corchetes para hacer una lista
print(vocales[0])
print(vocales[1])
print(vocales[2])

for numero in range(0,5):
  print(vocales[numero])

#Las funciones Lower, Upper y Proper convierten las letras de una cadena en mayúsculas o minúsculas.

# -> Lower convierte las letras mayúsculas en minúsculas.
# -> Upper convierte las letras minúsculas en mayúsculas.
# -> Proper convierte la primera letra de cada palabra en mayúscula si está en minúscula o en minúscula si está en mayúscula.
# Las tres funciones omiten los caracteres que no son letras.

# Si se pasa una cadena única, el valor devuelto es la versión convertida de dicha cadena. Si se pasa una tabla de una columna que contiene cadenas, el valor devuelto es 
# una tabla de una columna de cadenas convertidas. Si tiene una tabla con varias columnas, puede convertirla en una tabla de una sola columna, como se describe en cómo trabajar con tablas.

# Sintaxis
# Lower( String )
# Upper( String )
# Proper( String )

# String: requerido. La cadena que se va a convertir.
# Lower( SingleColumnTable )
# Upper( SingleColumnTable )
# Proper( SingleColumnTable )

# SingleColumnTable: requerido. Una tabla de una columna de cadenas para convertir.