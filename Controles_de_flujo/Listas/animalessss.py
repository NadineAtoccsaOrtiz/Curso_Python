lista=[]
while True:
    objeto={}
    objeto["animal"]=input("ingrese que animal es: ")
    objeto["nombre"]=input("ingresa en nombre como llamas a tu animal: ")
    objeto["edad"]=int(input("ingresa el tiempo que esta contigo: "))
    objeto["sexo"]=input("ingresa M si es macho y H si es hembra: ")
    lista.append(objeto)
    condicion=input("si desea salir escriba:salir, si desea continuar escriba:continuar: ")
    if condicion == 'salir':
        break
print(lista)