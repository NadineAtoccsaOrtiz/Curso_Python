#averiguar convenciones para nombrar una variable
#constantes y comos se declara en python

#CONVENCIONES
#Convenciones al Nombrar Elementos: CamelCase y snake_case
#A la hora de escribir código, todo tiene nombres: variables, clases, funciones, paquetes, módulos, etc. Es por lo tanto muy importante seguir unas 
# directrices determinadas para que nuestro código sea lo más legible posible. No se nombra igual a una clase que a una función, y tampoco suele ser 
# recomendable usar nombres como a o x ya que aporta poca información. A continuación lo vemos en detalle.

#Eligiendo Nombres
#Antes de nada debemos debemos pensar el nombre que le vamos dar a nuestra variable clase o función. Es importante tener en cuenta lo siguiente:
#Evitar usar palabras reservadas. Si es necesario usar una palabra reservada como class, usar class_ como alternativa.
#Evitar usar l O y I, ya que pueden ser confundidas.
#Usar _variable para especificar uso interno. Por ejemplo from m import * no importaría lo que empieza con _.
#Se puede usar __variable para invocar el name mangling y hacer privadas determinadas variables o métodos.
#Para métodos mágicos usar siempre __init__, pero no son nombres que debemos crear sino reutilizar los que Python nos ofrece.
#Estilos: Camel Case y snake_case
#Supongamos que ya sabemos como vamos a nombrar a nuestra clase, función o variable. Pongamos que queremos llamar 
# a nuestra función “mi función de prueba”. Dado que no podemos utilizar espacios para nombrar variables, hay diferentes alternativas:

#EJEMPLO
#mi_funcion_de_prueba
#MiFuncionDePrueba
#MIFUNCIONDEPRUEBA
#MI_FUNCION_DE_PRUEBA
#mifunciondeprueba

#Algunas de estas alternativas son conocidas como Camel Case o snake_case en 
# el mundo de la programación. Pues bien, Python define cómo nombrar a cada tipo 
# de la siguiente manera:

#Funciones: Letras en minúscula separadas por barra baja: funcion, mi_funcion_de_prueba.
#Variables: Al igual que las funciones: variable, mi_variable.
#Clases: Uso de CamelCase, usando mayúscula y sin barra baja: MiClase, ClaseDePrueba.
#Métodos: Al igual que las funciones, usar snake case: metodo, mi_metodo.
#Constantes: Nombrarlas usando mayúsculas y separadas por barra bajas: UNA_CONSTANTE, OTRA_CONSTANTE.
#Módulos: Igual que las funciones: modulo.py, mi_modulo.py.
#Paquetes: En minúsculas pero sin separar por barra bajas: packete, mipaquete



#Los siguientes estilos de nomenclatura se distinguen comúnmente:
#b (letra minúscula única)
#B (letra mayúscula única)
#minúscula
#lower_case_with_underscores
#MAYÚSCULA
#UPPER_CASE_WITH_UNDERSCORES
#CapitalizedWords (o CapWords, o CamelCase – llamado así por el aspecto irregular de sus letras [4]). Esto también se conoce a veces como StudlyCaps.
#Nota: Cuando utilice acrónimos en CapWords, escriba en mayúscula todas las letras del acrónimo. Por lo tanto, HTTPServerError es mejor que HttpServerError.

#CONSTANTES
#Las constantes son valores que permanecen intactos a través de la ejecución de un programa y que nadie puede modificar después de la primera asignación.
#Recordemos que por regla general (para indicar que es una constante) las constantes se indican con mayúsculas, y si tienen espacios se sustituyen por guiones bajos. Por ejemplo:
VERSION_DE_MI_PROGRAMA = "1.2.1.3"
#La convención para nombrar constantes es hacerlo con el nombre todo en mayúsculas, de esta forma, aunque en realidad estemos trabajando con variables,
#  quien esté trabajando con el programa, sabrá a simple vista que se trata de una constante y que no hay que reasignarle ningún valor.

CONSTANTE = "Valor cualquiera."
CONSTANTE = "Otro valor."

print(CONSTANTE)


