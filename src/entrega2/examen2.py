'''
Created on 21 nov 2024

@author: User
'''

from __future__ import annotations
from entrega2.tipos.Agregado_lineal import AgregadoLineal
from typing import TypeVar

E=TypeVar('E')

class ColaConLimite (AgregadoLineal[E]):
    def __init__(self, capacidad:int):
        super().__init__()
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0.")
        self._capacidad = capacidad
    
    @staticmethod
    def of(capacidad: int) -> ColaConLimite[E]:
        return ColaConLimite(capacidad)
    
    def is_full(self) -> bool:
        return len(self._elements) == self._capacidad
    
    def add(self, e: E) -> None:
        if self.is_full(): #Compruebo que la lista está llena
            raise OverflowError("Overflow: La cola está llena.")
        self._elements.append(e)
    
    def __repr__(self) -> str:
        return f"{self._elements}" 
    
#Aquí comienzan las pruebas (ejercicio 3)
print('TESTS COLA CON LÍMITE')
print('Cuando la capacidad es 3 e introduzco "Tarea 1", "Tarea 2", "Tarea 3"')
cola= ColaConLimite.of(3)
cola.add('Tarea1')
cola.add('Tarea 2')
cola.add('Tarea 3')
print(f'El resultado de la cola es: {cola}')
print('########################')
print('Intento introducir un nuevo elemento: "Tarea 4". Supera la capacidad.')
try:
    cola.add('Tarea 4')
except OverflowError as e:
        print(e)



#Faltan las pruebas de Agregado_lineal, pretendía crear una nueva clase "cola" con la que realizar las pruebas.

