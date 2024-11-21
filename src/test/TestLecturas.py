'''
Created on 18 oct 2024

@author: User
'''
 
from lecturas.lecturas import contador_palabras, lineas_con_palabra,\
    palabras_unicas, longitud_promedio_lineas

def test6():
    print('TEST DE LA FUNCIÓN 6:')
    prueba6=contador_palabras('../resources/lin_quijote.txt', 'quijote') #probar con variaciones del texto
    print(f'El número de veces que aparece la palabra quijote en el fichero resources/lin_quijote.txt es: {prueba6}')

def test7():
    print('TEST DE LA FUNCIÓN 7:')
    prueba7=lineas_con_palabra('../resources/lin_quijote.txt', 'quijote')
    print(f'Las líneas en las que aparece la palabra quijote son: {prueba7}')

def test8():
    print('TEST DE LA FUNCIÓN 8:')
    prueba8=palabras_unicas('../resources/archivo_palabras.txt')
    print(f'Las palabras únicas en el fichero archivo_palabras.txt son: {prueba8}')

def test9_1():
    print('TEST 1 DE LA FUNCIÓN 9:')
    prueba9=longitud_promedio_lineas('../resources/palabras_random.csv', ',')
    print(f'La longitud promedio de las líneas del fichero palabras_random.csv es: {prueba9}')
    
def test9_2():
    print('TEST 2 DE LA FUNCIÓN 9:')
    prueba10=longitud_promedio_lineas('../resources/vacio.csv', ',')
    print(f'La longitud promedio de las líneas del fichero vacio.csv es: {prueba10}')
    
if __name__ == '__main__':
    test9_1()