#como ordenar una lista con los metodos de ordenamiento en python

#band = False
#while band==False:
#    for i in range(len(lista)-1):
#        if lista[i]>lista[i+1]:
#            aux=lista[i]
#            lista[i]=lista[i+1]
#            lista[i+1]=aux
#            band=False
#print(lista)


def menor_a_mayor( lista ):
    n = len( lista )

    for i in range( n - 1 ) :
        valor= 0

        for j in range(n - 1) :
            
            if lista[j] > lista[j + 1] : 
                tmp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = tmp
                valor = 1

        if valor== 0:
            break

    return lista

lista=[4,7,9,2,4,1,6,3,5,8,9,10]

resultado= menor_a_mayor(lista)

print (resultado)