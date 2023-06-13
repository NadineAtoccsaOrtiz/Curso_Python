print('Bienvenid@ a la Calculadora de indice de masa corporal IMC')
peso=float(input('Ingresa tu peso en Kg'))
talla=float(input('Ingresa tu talla en Cm'))
imc=talla*talla
imc1=peso/imc
print(imc)
if imc1>=18:
	print('Estas en el peso normal')
elif imc<18:
	print('Estas bajo de peso')