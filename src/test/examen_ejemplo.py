'''
Created on 23 oct 2024

@author: User
'''
import math
def P3(n:int, k:int, i:int = 1) -> int:
    assert n>0
    assert k>0
    assert i>0
    assert k>i
    producto=1
    for j in range(i,k+1):
        producto *= n + j
    return producto

print(P3(3,5,1))

def C3(n: int, k: int) -> int:
    resultado=(math.factorial(n+1)//((math.factorial(k))*(math.factorial(n-k+1))))
    return resultado
    assert n>0
    assert k>0
    assert n>=k-1

def S3 (n:int, k:int) -> float:
    suma=0
    for i in range(0, k+1):
        suma+= ((-1)**i) * math.comb(k, i) * ((math.factorial(n+i)/math.factorial(k-i)))
    return suma
    assert n>0
    assert k>0
    assert n>=k

def palabrasMenosComunes(fichero: str, n: int = 5):
    lista_palabras= []
    try:
        with open(fichero, mode='r', encoding='utf-8') as f:
            contenido=f.read().lower()
            palabras=contenido.split()
            for palabra in palabras:
                lista_palabras+=[[palabra, palabras.count(palabra)]]
            for i in range(0, n+1):
                indices_lista=[]
                indices_lista+= -i
        return lista_palabras[indices_lista]
                
    