'''
Created on 17 oct 2024

@author: User
'''

from funciones.funciones import producto, producto_secuencia,\
    numero_combinatorio, sumatorio, metodo_newton

def test1():
    print('TEST DE LA FUNCIÓN 1:')
    n=4
    k=2
    prueba1 = producto(n, k)
    print(f'El producto de {n} y {k} es: {prueba1}')

def test2():
    print('TEST DE LA FUNCIÓN 2:')
    a1=3
    r=5
    k=2 
    prueba2 = producto_secuencia(a1, r, k)
    print(f'El producto de la secuencia geométrica con a1={a1}, r={r} y k={k} es: {prueba2}')

def test3():
    print('TEST DE LA FUNCIÓN 3:')
    n=4
    k=2
    prueba3 = numero_combinatorio(n, k)
    print(f'El número combinatorio de {n} y {k} es: {prueba3}')

def test4():
    print('TEST DE LA FUNCIÓN 4:')
    n=4
    k=2
    prueba4 = sumatorio(n, k)
    print(f'El número S(n, k) siendo n={n} y k={k} es: {prueba4}')

def test5():
    print('TEST DE LA FUNCIÓN 5:')
    a=3
    e=0.001
    f= lambda x: 2*(x**2)
    fd= lambda x: 4*x
    prueba5 = metodo_newton(a, e, f, fd)
    print(f'Resultado de la función 5 con a={a} y e={e}, f(x)=2·x^2 y f´(x)=4·x: {prueba5}')
    
if __name__ == '__main__':
    test1()
