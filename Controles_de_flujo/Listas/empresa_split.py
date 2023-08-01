nombre=input('ingresa el nombre de la empresa: ')
ruc=int(input('ingresa el ruc de la empresa: '))
direccion=input('ingresa la direccion: ')
sucursales=input('ingresa las sucursales en comas: ').split(' , ')
horario_dia=input('ingresa el horario del dia: ')
horario_tarde=input('ingresa el horario de la tarde')
empresa={'nombre': nombre ,
					'ruc':ruc,
					'direccion':direccion,
					'sucursales':sucursales,
					'horario':{
							'dia':horario_dia,
							'tarde':horario_tarde
					}	}
print(empresa)
