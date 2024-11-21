'''
Created on 6 nov 2024

@author: User
'''

from __future__ import annotations
from typing import Callable, TypeVar, Generic
from entrega2.tipos.Agregado_lineal import AgregadoLineal


E=TypeVar('E')
R=TypeVar('R')

class ListaOrdenada(AgregadoLineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]): # El constructor de la clase recibe un argumento order, que es una función que se usará para ordenar los elementos. Esta función acepta un elemento E y devuelve un valor de tipo R
        super().__init__() # llama al constructor de AgregadoLineal para inicializar la lista _elements
        self._order = order #guarda la función order en un atributo privado _order.
    
    @staticmethod
    def of(order: Callable[[E], R]) -> ListaOrdenada[E, R]: #Este método permite crear una nueva instancia de ListaOrdenada de forma estática. Recibe una función order como parámetro y la usa para crear una instancia de ListaOrdenada inicializada con ese criterio de orden.
        return ListaOrdenada(order)

    def __index_order(self, e: E) -> int: # Este es un método privado que busca el índice donde se debe insertar un nuevo elemento e para mantener el orden.
        for index, current in enumerate(self._elements):
            if self._order(e) < self._order(current): #Si el valor de self._order(e) (el valor del nuevo elemento según la función de orden) es menor que el valor de self._order(current), entonces devuelve el índice actual, donde el nuevo elemento debe insertarse.
                return index
        return len(self._elements) #Si no se encuentra un elemento mayor, devuelve el tamaño actual de la lista (len(self._elements)), indicando que el nuevo elemento debería agregarse al final.
    
    def add(self, e: E) -> None:
        index = self.__index_order(e)
        self._elements.insert(index, e)
        
    def __repr__(self) -> str:
        return f'ListaOrdenada({self._elements})'
