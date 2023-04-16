## vamos a realizar un programa que reciba un número por parte del usuario y lo convierta a binario


def conver_to_binary():
    bits_table = [128, 64, 32, 16, 8, 4, 2, 1]
    numerocliente = int(input('Sr. Usuario por favor ingrese un número: '))
    for numero in bits_table:
        if numero >= numerocliente:
            print(1)    
        else:
            print(0)
conver_to_binary()



