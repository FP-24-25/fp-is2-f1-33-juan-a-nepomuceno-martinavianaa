'''
Created on 6 nov 2024

@author: User
'''

from entrega2.tipos.Lista_ordenada import ListaOrdenada

print('TEST DE LISTA ORDENADA')
print('#############################')
print('Creación de una lista con criterio de orden lambda x: x')
lista=ListaOrdenada(lambda x:x)
print('Se añade en este orden: 3, 1, 2')
lista.add_all([3, 1, 2])
print(f'Resultado de la lista: {lista}')
print('#############################')
print(f'El elemento eliminado al utilizar remove(): {lista.remove()}')
print('#############################')
lista.add(1)
print(f'Elementos eliminados utilizando remove_all(): {lista.remove_all()}')
print('#############################')
print('Comprobando si se añaden los números en la posición correcta...')
lista.add_all([3, 1, 2])
lista.add(0)
print(f'Lista después de añadirle el 0: {lista}')
lista.add(10)
print(f'Lista después de añadirle el 10: {lista}')
lista.add(7)
print(f'Lista después de añadirle el 7: {lista}')