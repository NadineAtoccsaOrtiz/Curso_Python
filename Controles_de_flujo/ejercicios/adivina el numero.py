intentos=0
minumero=5
while intentos<3:
    print('intenta adivinar en que numero estoy pensando: ')
    numero=int(input('ingresa un numero: '))

    intentos=intentos+1

    if numero<minumero:
        print('tu estimacion es baja, sigue intentndo. ')
    if numero>minumero:
        print('tu estimacion es alta, sigue intentando. ')
    if numero==minumero:
        break
if numero==minumero:
    intentos=str(intenos)
    print('felicidades, aivinaste el numero en, {intentos}, intentos.')
if numero!=minumero:
    minumero=str(minumero)
    print('fallaste, el numero que estaba pensando era:+minumero')