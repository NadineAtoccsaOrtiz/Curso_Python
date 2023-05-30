#Operadores de comparación
#     mayor 15<13 -> TRUE
#     menor 12>15 -> TRUE
#      igual 12==12 -> TRUE
#      distinto 12!=10 -> TRUE
#   - True o false
#   - 12==10 false
#    - 12<13 true
#    - Almacenar variable
#    - Com=12<13
#   - Print(com)

# Operadores aritméticos

#   - Suma
#   - Resta
#   - División 12/2
#   - Residuo
#   - Potencia **
#   - Raíz
#   - División en Entero 12//2

#Print (12+45+12)

#Print (12+(45+12))

#Print (45/23*5+2)

#Print(45/23/5*2)

# Almacenar operación

#   Op=45/23/5*2 -> de derecha a izquierda

#   Print(op)

# Operadores lógicos

#   - True
#   - False

#   Var = true & true

#   Print (var) 

#   Opera = true | true 

#   Print (opera)

# Asignación aumentada

#   a=10

#   a= a+10 

#    a+=10 → ## a=a+10

# Ejercicios 

#   Entrada de datos

#   NumeroUno=int(input(’numero uno’))

#    NumeroDos=int(input(’numero dos’))

# Proceso

#   Suma=numeroUno+numeroDos

#  Salida de datos

#    Print(suma)

# Tarea

#Escriba un programa que acepte el radio de un círculo y compute su área

#   F= Dentro de un string concatenar la variable 

#   En vez de poner comillas y el +

#Ejercicio dos 

#Escriba un programa que acepte el radio de una esfera y obtenga el volumen

#Ejercicio  tres

#Escriba un programa que acepte la base y la altura de un triángulo

#   Codewars

#   Letcode
# OPERACIONES CON STRING
## observacioj
# true se considera como 1 internamente y false seria 0
#suma=false*20 -> 0
#suma=true+20 -> 21

#convinacion de cadenas (concatenar)
#   letra='hola'+'a todos'
#no solo las letras son string tambien los espacios
#letra='hola'+' '+'a todos'
### repetir cadenas
# cadena='hola '*5
#print(cadena)
#print (cadena, end)
#obtener una cadena especifica
        #obtenercadena='hola'
        #print(obtenercadena)
        #python asigna a una cadena dos tipos de indices
        #indice positivo de izquierda a derecha, empeiza de 0
        #indice negativo derecha a izquierda, empeiza en -1
#quiero imprimir la letra l de mi variable obtenercadena
#print=(obtenercadena[2]) -> l
#print=(obtenercadena[-3]) -> o
# bracket -> []
#### la ultima letra siempre es n-1
#la comilla debe ser diferente a las que guardan el mensaje para evitar error
#ya que al poner comillas estamos guardando datos de string 

#trocear cadenas
#trocear='un mensaje'
# print=(trocear[2:]) #### es igual a print(ultimostring[-1])
#[star o inicio:final+1] -> estructura
#[inicio:inicionegativo] -> otra manera
#solo funciona con string, con las comillas
#length en java gallina tiene huevo

### PERTENENCIAS
#EJEMPLO
#con tal de que haya un caracter igual al mensaje nos da true
#debe ser igual, si esta en mayusculas o minusculas
#sirve para comparar

#con= comparar letras se pueden pero conel codigo ascci
#las comparaciones solo se hacen con numero pero al colocar letras 
#internamente lo compara basandose en el codigo ascci de las letras


#CONVERSACIONES string número

#Número=”10”
#Input() nos devuelve string
#Convertir a número
#Print(type(int(numero))
#o
#Número=”10”
#Número invertido=int(número)
#Print(type(número))
#Print(type(numeroconvertido))
# →<class ‘str’>
# →<class ‘int’>

#FlotanteString=’10’
#Flotantenúmero=float(FlotanteString)
#Print(FlotanteString)
#Print(flotantenúmero)
# →10
# →10.0

#Print(type(flotantenúmero))
#→<class ‘float’>

#Int-entero
#Input-captura datos
# float → coma o punto flotante, sirve en casos por ejemplo cuando se trabaja con dinero, 
# encuestas, en peso, talla, etc


#CONVERSIÓN INVERSA
#Númeroentero=20
#Númerostring=(str(Númeroentero))

#Ejercicios
#Haga un programa que pida al usuario su nombre y luego su apellido y como salida que concatene 
# ambos datos 

#Ejercicio
#Hacer un programa que pida un texto y me de cómo salida la cantidad de letras que tiene

#NOTA:
#Algoritmos de ordenamiento
#Controles de flujo- cortar la secuencia normal de un programa 
#Los programas se manejan de forma secuencial 
#ejem
#Nombre=’Jory’
#Mensaje=’hola bichota’
#Print(mensaje)
#Print(nombre)
# →hola
# →jory

#bloques en python
#Cuando nosotros utilicemos cualquier control de flujo o funciones, el código que se debe
#  ejecutar deberá estar definida por bloques o identaciones.

#       1).- condicionales:

#       Se realiza algo si se cumple cierta condición

#       Cuando tenemos un capítulo

#Ejemplo:

#I.Introduccion

#   1.1. concepto 

#   1.2.

#Estructura

#Si tenemos un control de flujo por ejemplo una condición, se va ejecutar si se cumple la condición 

#Si es verdad:

#      Print(’es verdad’)

#Print(’otra cosa’)
#=================================================================
#If true: o → if false: 
#      Print(’es verdad’)

#Print(’otra cosa’)

#Si es falso no ejecuta, ahí se rompe el flujo, al pasar eso el programa se pasa a la siguiente línea y 
# así sucesivamente hasta imprimir otra cosa

#Omite lo demás al no cumplir la condición

#Todo lo que hay dentro de if si la condición es verdad, caso contrario se imprime lo que está fuera de if

#TAREA: hacer un programa que pida al usuario su DNI si la longitud del DNI es 8 que pida su nombre y lo muestre 
# en consola si la longitud del DNI es mayor o menor a 8 que muestre un mensaje de error.