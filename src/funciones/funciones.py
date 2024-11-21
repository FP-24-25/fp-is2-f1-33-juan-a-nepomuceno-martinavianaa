'''
Created on 17 oct 2024

@author: User
'''
import math

def producto(n:int, k:int) -> int:
    producto = 1  
    for i in range(0, k+1):
        producto *= (n - i + 1)
    return producto

def producto_secuencia (a1, r, k):
    producto=a1
    for n in range(2, k+1):
        producto*= (a1 * r**(n-1))
    return producto

def numero_combinatorio (n, k):
    resultado = math.comb(n, k)
    return resultado

def sumatorio (n, k):
    suma=0
    for i in range(0, k):
        suma+= ((-1)**i) * math.comb(k+1, i+1) * ((k-i)**n)
    suma*= 1/math.factorial(k)
    return suma

def metodo_newton (a, e, f, fd):
    x_n = a
    while abs(f(x_n))> e:
        x_n = x_n - f(x_n)/ fd(x_n)
    return x_n