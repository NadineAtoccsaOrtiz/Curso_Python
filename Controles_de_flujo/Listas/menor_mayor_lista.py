#como ordenar una lista con los metodos de ordenamiento en python
lista=[4,7,9,2,4,1,6,3,5,8,9,10]
band = False
while band==False:
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            aux=lista[i]
            lista[i]=lista[i+1]
            lista[i+1]=aux
            band=False
print(lista)
