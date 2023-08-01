#objeto={'nombre':'Nadine','Apellidos':'Atoccsa Ortiz','edad':18,'fecha de nacimiento':'06/04/2005','DNI':73787356,'correo':'nadineatoccsaortiz@gmail.com','ocupacion':'Estudiante'}

objeto={}
objeto['nombre']=input('ingresa tu nombre: ')
objeto['Apellidos']=input('ingresa tus apellidos: ')
objeto['Edad']=int(input('ingresa tu edad: '))
objeto['DNI']=int(input('ingresa tu DNI: '))
objeto['Ocupacion']=input('ingresa tu ocupacion: ')
objeto['Sexo']=input('ingresa M si es masculino o F si es femenino: ')
if 'sexo' in objeto == 'M':
	print('Tu sexo es masculino')
else:
	print('Tu sexo es Femenino')
print(objeto)
	
print 

