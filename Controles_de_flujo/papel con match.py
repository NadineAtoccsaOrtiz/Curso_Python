print(f"""
====================================================
Bienvenid@s al juego: Piedra👊, Papel🖐  o Tijeras✌
====================================================
""")
import nombres
print(f'\nHola {nombres.persona1} y {nombres.persona2}✨🎉')
import mensajes
print(mensajes.movimientos)

while True:
    jugador1 = int(input(f'{nombres.persona1} elige tu movimiento: '))
    jugador2 = int(input(f'{nombres.persona2} elige tu movimiento: '))

    match jugador1:
        case 1 if jugador2 == 3: 
            print(f"""
            -----------------------------------------------
            Gana {nombres.persona2} ya que  {mensajes.m1}🤩
            """)
        case 2 if jugador2 == 1: 
            print(f"""
            ----------------------------------------------
            Gana {nombres.persona1} ya que {mensajes.m2}🤩
            """)
        case 3 if jugador2 == 2: 
            print(f"""
            ---------------------------------------------
            Gana {nombres.persona1} ya que {mensajes.m3}🤩
            """)
        case 3 if jugador2 == 1: 
            print(f"""
            ---------------------------------------------
            Gana {nombres.persona2} ya que {mensajes.m1}🤩
            """)
        case 1 if jugador2 == 2: 
            print(f"""
            ----------------------------------------------
            Gana {nombres.persona2} ya que {mensajes.m2}🤩
            """)
        case 2 if jugador2 == 3: 
            print(f"""
            ----------------------------------------------
            Gana {nombres.persona2} ya que {mensajes.m3}🤩
            """)
        case 1 if jugador2 == 1: 
            print(f'\nVaya, quedaron empate😂\n')
        case 2 if jugador2 == 2: 
            print(f'\nVaya, quedaron empate😂\n')
        case 3 if jugador2 == 3: 
            print(f'\nVaya, quedaron empate😂\n')
        case _: print(mensajes.m4)
else:
    print('\nmovimiento no valido😬\n')

