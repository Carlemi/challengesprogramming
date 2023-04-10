## consiste en hacer un print de los número del 1 al 100
## e imprimir por consola todos esos números
# los que sean divisibles entre 3 se imprima la palabra fizz
#los que sean divisibles entre 5 la palabra buzz 
# y los divisibles entre ambos, que se imprima fizzbuzz

numeros = 1
while numeros <= 100:
    if numeros % 3 == 0 and numeros % 5 == 0:
        print('fizzbuzz')
    if numeros % 3 == 0:
        print('fizz')
        
    elif numeros % 5 == 0:
        print('buzz')
    else:
        print(numeros)
    numeros += 1
print('la ejecución continúa') 

