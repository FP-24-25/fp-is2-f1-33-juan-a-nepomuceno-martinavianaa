'''
Created on 24 oct 2024

@author: User
'''

import math

def P2(n:int, k:int, i:int=1):
    assert n>k
    assert i< (k+1)
    producto=1
    for i in range(i, k-1):
        producto*= (n-i+1)
    return producto

def C2(n:int, k:int):
    assert n>k
    assert n>0
    assert k>0
    resultado=math.comb(n, k+1)
    return resultado
    

def S2(n:int, k:int):
    assert n>k
    assert n>0
    assert k>0
    suma=0
    for i in range(0, k+1):
        suma+= ((-1)**i)*math.comb(k,i)*(k,i)**(n+1)
    suma+=math.factorial(k)/(n*math.factorial(k+2))
    return suma

def palabrasMasComunes (fichero:str, n=int):
    assert n>1
    lista=[]
    try:
        with open(fichero, mode='r', encoding='utf-8') as f:
            contenido=f.read().lower()
            palabras=contenido.split()
            for palabra in palabras:
                res=palabras.count(palabra)
                lista+=[palabra,res]
        return lista
    except IOError as e:
        print(f'Error al intentar leeer el archivo: {e}')
    except Exception as e:
        print(f'Ocurrió un error al crear el fichero: {e}')
    
def test1():
    print('TEST P2:')
    try:
        print(P2(5, 4, 6))
    except AssertionError:
        print(f'Los parámetros no cumplen con los criterios correctos')
    try:
        print(P2(8, 5, 2))
    except AssertionError:
        print(f'Los parámetros no cumplen con los criterios correctos')
    
def test2():
    print('TEST C2:')
    try:
        print(C2(7,4))
    except AssertionError:
        print(f'Los parámetros no cumplen con los criterios correctos')
    try:
        print(C2(3,8))
    except AssertionError:
        print(f'Los parámetros no cumplen con los criterios correctos')

if __name__ == '__main__':
    test1()

if __name__ == '__main__':
    test2()



        
        
