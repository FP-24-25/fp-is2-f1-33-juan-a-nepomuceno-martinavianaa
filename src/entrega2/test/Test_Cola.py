'''
Created on 6 nov 2024

@author: User
'''

from entrega2.tipos.Cola import Cola

print('TEST DE COLA')
print('#############################')
print('Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5')
cola = Cola()
numeros_a_agregar = [23, 47, 1, 2, -3, 4, 5]
for numero in numeros_a_agregar:
    cola.add(numero)
print(f'Resultado de la cola: {cola}')
print('#############################')
print('Elementos eliminados utilizando remove_all:', cola.remove_all())