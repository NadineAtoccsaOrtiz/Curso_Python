print("Categoria Precio Codigo Reacargo/dia de atraso")
print("Favoritos 2.50 1 $0.50")
print("Nuevos 3.00 2 $0.75")
print("Estrenos 3.50 3 $1.00")
print("Super estrenos 4.00 4 $1.50")
print("")
codigo = int(input("Introduce el codigo de la categoria de la pelicula: "))
dias = int(input("Introduce el numero de dias de atraso en la devolucion: "))
codigo in range(1,4)
print("")
if(codigo > 4):
    print("Porfavor, introduce un codigo correcto, del 1 al 4")
else:
    if(codigo==1):
        retraso = (2.50 + (dias * 0.5))
        print("El total a pagar es: $",retraso," dolares")
    elif(codigo==2):
        retraso = (3 + (dias * 0.75))
        print("El total a pagar es: $",retraso," dolares")
    elif(codigo==3):
        retraso = (3.50 + (dias))
        print("El total a pagar es: $",retraso," dolares")
    else:
        retraso = (4 + (dias * 1.5))
        print("El total a pagar es: $",retraso," dolares")