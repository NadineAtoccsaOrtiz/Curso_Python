#crear una funcion que me permita agregar dos objetos en una lista, de un perro y un gato.

#lista=[{'animal':'Perro','nombre':'Taff','raza':'Pitbul','sexo'}]

lista=[]
while len(lista)<=2:
	objeto={}
	objeto['Animal']=input('ingresa que animal es tu mascota: ')
	objeto['Nombre']=input('ingresa el nombre de la mascota')
	objeto['Edad']=int(input('ingresa la edad de la mascota'))
	
	lista.append(objeto)
print(lista)