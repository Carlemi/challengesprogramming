## vamos a realizar un programa que reciba un número por parte del usuario y lo convierta a binario

bits_table = [128, 64, 32, 16, 8, 4, 2, 1]

numerocliente = int(input('Sr. Usuario por favor ingrese un número: '))


if numerocliente >= bits_table[0]:
    print(1)
else:
    print(0)
if numerocliente >= bits_table[1]:
    print(0)
else:
    print(0)
if numerocliente >= bits_table[2]:
    print(1)
else:
    print(0)
if numerocliente >= bits_table[3]:
    print(1)
else:
    print(0)
if numerocliente >= bits_table[4]:
    print(1)
else: 
    print(0)
if numerocliente >= bits_table[5]:
    print(1)
else:
    print(0)
if numerocliente >= bits_table[6]:
    print(1)
else:
    print(0)
if numerocliente >= bits_table[7]:
    print(1)
else:
    print(0)
print(bits_table)    


