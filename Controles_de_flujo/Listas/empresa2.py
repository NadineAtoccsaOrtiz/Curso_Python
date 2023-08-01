## otro metodo

objeto={}
objeto['nombre']=input('ingresa el nombre de tu empresa: ')
objeto['Ruc']=int(input('ingresa el ruc de tu empresa: '))
objeto['Direccion']=input('ingresa tu direccion: ')

while len(objeto['sucursales'])<2:
	sucursal=input('ingresa el nombre de tu 	sucursal: ')
	objeto['sucursales'].append(sucursal)
	
objeto['Horario']={}
objeto['Horario']['dia']=input('ingresa el horario de atencion del dia: ')
objeto['Horario']['tarde']=input('ingresa el horario de atencion de la tarde: ')


print(objeto)