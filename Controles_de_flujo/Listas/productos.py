print('Elige un producto deseado: ')
print(f"""
1 CAMISA------------------------100
2 CINTURON----------------------50
3 ZAPATOS-----------------------80
4 PANTALON----------------------60
5 CALCETINES--------------------10
6 FALDAS------------------------150
7 GORRAS------------------------80
8 SUETER------------------------160
9 CORBATA-----------------------20
10 CHAQUETA---------------------100
""")

cuenta = []
precios = [100, 50, 80, 60, 10, 150, 80, 160, 20, 100]

comprando = 0
while comprando == 0:

	codigo = int(input("Introduzca el código del articulo: "))
	cantidad = int(input("Introduzca la cantidad de articulos: "))
	cuenta.append((precios[codigo-1])*cantidad)
	comprando = int(input("Para agregar otro articulo 0 para salir 1: "))

precio_total = 0

for precios in cuenta:
	precio_total = precio_total + int(precios)


print("El precio total a pagar es de " + str(precio_total))