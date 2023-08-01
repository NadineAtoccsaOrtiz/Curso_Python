print("Categoria Precio Codigo Reacargo/dia de atraso")
print(f"""
1 Favoritos/ s/2.50 / s/0.50
2 Nuevos/ s/3.00 2 / s/0.75
3 Estrenos/ s/3.50 / s/1.00
4 Super estrenos/ s/4.00 / s/1.50
""")

codigo = int(input("Introduce el codigo de la categoria de la pelicula: "))
dias = int(input("Introduce el numero de dias de atraso en la devolucion: "))
codigo in range(1,4)
print("")
if(codigo > 4):
    print("Porfavor, introduce un codigo correcto, del 1 al 4")
else:
    if(codigo==1):
        retraso = (2.50 + (dias * 0.5))
        print("El total a pagar es: s/",retraso," dolares")
    elif(codigo==2):
        retraso = (3 + (dias * 0.75))
        print("El total a pagar es: s/",retraso," dolares")
    elif(codigo==3):
        retraso = (3.50 + (dias))
        print("El total a pagar es: s/",retraso," dolares")
    else:
        retraso = (4 + (dias * 1.5))
        print("El total a pagar es: s/",retraso," dolares")