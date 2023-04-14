## vamos a realizar un ejercicio que reciba una función que calcule el área de un polígono y la retorne 


## definimos la función
def areapoligono(poligono):
    #poligono = input('Por favor introduzca un polígono entre - cuadrado \n- triángulo\n- rectángulo')
    lado = 2
    basetri = 3
    alturatri = 4
    areatri = basetri * alturatri / 2
    baserec = 2
    alturarec = 5
    arearec = baserec * alturarec
    # utilizamos el condicional para saber que tipo de polígono selecciona el usuario
    if poligono == 'cuadrado':
        lado **= 2
        print(f'El área de este polígono es: {lado}')
    elif poligono == 'triángulo':
        print(f'El área de este polígono es: {areatri}')
    else:
        print(f'El área de este polígono es: {arearec}')

    return poligono

areapoligono(poligono= input('Por favor introduzca un polígono entre - cuadrado \n- triángulo\n- rectángulo \n')) #le pedimos por consola al usuario que ingrese alguno de los tres polígonos