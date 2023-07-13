print("Bienvenid@s al juego Piedra👊, papel🖐 o tijeras✌")
print('opciones\n1.piedra\n2.papel\n3.tijeras\n')
while True:
	jugador1=int(input('Jugador 1, elije tu movimiento: '))
	jugador2=int(input('Jugador 2, elije tu movimiento: '))

	if jugador1==1 and jugador2==3:
		print('\nJugador 1 gana, piedra chanca a tijeras\n')
	elif jugador1==2 and jugador2==1:
		print('\nJugador 1 gana, papel tapa a piedra\n')
	elif jugador1==3 and jugador2==2:
		print('\nJugador 1 gana, tijeras cortan a papel\n')
	elif jugador2==1 and jugador1==3:
		print('\nJugador 2 gana, piedra chanca a tijeras\n') 
	elif jugador2==2 and jugador1==1:
		print('\nJugador 2 gana, papel tapa a piedra\n')
	elif jugador2==3 and jugador1==2:
		print('\nJugador 2 gana, tijeras cortan a papel\n')
	elif jugador1==jugador2:
		print('\nEmpate, vuelvan a escojer su movimiento\n')
	else:
		print('\nMovimiento no valido, vuelva a elejir\n')