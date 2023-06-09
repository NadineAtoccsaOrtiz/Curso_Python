print("Bienvenid@s al juego Piedra, papel o tijeras")
print('opciones\n1.piedra\n2.papel\n3.tijeras')
while True:
	jugador1=int(input('Jugador 1, elije tu movimiento: '))
	jugador2= input('Jugador 2, elije tu movimiento: ')

	if jugador1=='piedra' and jugador2=='tijeras':
		print('Jugador 1 gana, piedra chanca a tijeras')
	elif jugador1=='papel' and jugador2=='piedra':
		print('Jugador 1 gana, papel tapa a piedra')
	elif jugador1=='tijeras' and jugador2=='papel':
		print('Jugador 1 gana, tijeras cortan a papel')
	elif jugador2=='piedra' and jugador1=='tijeras':
		print('Jugador 2 gana, piedra chanca a tijeras') 
	elif jugador2=='papel' and jugador1=='piedra':
		print('Jugador 2 gana, papel tapa a piedra')
	elif jugador2=='tijeras' and jugador1=='papel':
		print('Jugador 2 gana, tijeras cortan a papel')
	elif jugador1==jugador2:
		print('Empate, vuelvan a escojer su movimiento')
	else:
		print('Movimiento no valido, vuelva a elejir')