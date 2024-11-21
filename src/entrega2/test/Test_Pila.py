'''
Created on 11 nov 2024

@author: User
'''

from entrega2.tipos.Pila import Pila

print('TEST DE PILA')
print('#############################')
print('Creación de una pila vacía')
pila = Pila.of()
print(f'Pila inicial: {pila}')
print('Se añade en este orden: 1, 2, 3')
pila.add_all([1, 2, 3])
print(f'Resultado de la pila: {pila}')
print('#############################')
print(f'El elemento eliminado al utilizar remove(): {pila.remove()}')
print(f'Pila tras usar remove(): {pila}')
print(f'Elementos eliminados utilizando remove_all(): {pila.remove_all()}')
print(f'Pila tras usar remove_all(): {pila}')
print('#############################')
print('Se comprueba que se mantenga el orden correcto al añadir elementos:')
pila.add_all([1, 2, 3])
pila.add(8)
print(f'Resultado de la pila tras añadir un 8: {pila}')
pila.add(3)
print(f'Resultado de la pila tras añadir un 3: {pila}')