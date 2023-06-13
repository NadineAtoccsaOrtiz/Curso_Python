print("Hola, Bienvenid@ a la calculadora ♦")
print(f"""
1.suma + 
2.resta -
3.multiplicacion ×
4.division ÷
""")
op=input('Indique la operacion que desea ejecutar: ')
n1=int(input('ingrese n1: '))
n2=int(input('ingrese el n2: '))
if op=='+':
	print(f"""
	====================
	procesando operacion.....
	suma: {n1+n2}
	====================
	""")
	print(f"""
	Felicitaciones, la operacion fue un 
	exito")
	""")
elif op=='-':
	print(f"""
	====================
	Procesando operacion.....
	resta:", {n1-n2}
	====================
	""")
	print(f"""
	Felicitaciones, la operacion fue un 
	exito")
	""")
elif op=='×':
	print(f"""
	====================
	Procesando operacion.....
	resta:", {n1*n2}
	====================
	""")
	print(f"""
	Felicitaciones, la operacion fue un 
	exito")
	""")
elif op=='÷':
	print(f"""
	====================
	Procesando operacion.....
	resta:", {n1//n2}
	====================
	""")
	print(f"""
	Felicitaciones, la operacion fue un 
	exito")
	""")
else:
	print(f"""
	•••••••••••••••••••••••••••••••••••••••••••
	Error al seleccionar la operacion
	vuelva a seleccionar.
	•••••••••••••••••••••••••••••••••••••••••••
	""")