#crear un programa que almacene datos de una empresa con el siguiente formato
#

objeto={}
objeto['nombre']=input('ingresa el nombre de tu empresa: ')
objeto['Ruc']=int(input('ingresa el ruc de tu empresa: '))
objeto['Direccion']=input('ingresa tu direccion: ')
objeto['Sucursales']=input('ingresa las sucursales de tu empresa: ')
objeto['Ocupacion']=input('ingresa tu ocupacion: ')
objeto['Horario de dia']=input('ingresa el horario de atencion del dia: ')
objeto['Horario de tarde']=input('ingresa el horario de atencion de la tarde: ')


print(objeto)