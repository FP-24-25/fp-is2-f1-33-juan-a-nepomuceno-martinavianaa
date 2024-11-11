'''
Created on 6 nov 2024

@author: User
'''

from __future__ import annotations
from typing import TypeVar, Generic, List, Tuple

E = TypeVar('E')
P = TypeVar('P')

class ColaPrioridad(Generic[E, P]):
    def __init__(self):
        # Lista de tuplas (elemento, prioridad)
        self._elements: List[Tuple[E, P]] = []
    
    def add(self, e: E, priority: P) -> None:
        # Agregar un elemento respetando el orden de prioridad
        index = self.index_order(priority)
        self._elements.insert(index, (e, priority))
    
    def index_order(self, priority: P) -> int:
        # Encontrar el índice en el que insertar el nuevo elemento según la prioridad
        for index, (_, p) in enumerate(self._elements):
            if priority < p:
                return index
        return len(self._elements)
    
    def remove(self) -> E:
        # Elimina y devuelve el elemento con la mayor prioridad
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)[0]
    
    def remove_all(self) -> List[E]:
        # Elimina todos los elementos y devuelve la lista de elementos eliminados
        elementos_eliminados = []
        while not self.is_empty():
            elementos_eliminados.append(self.remove())
        return elementos_eliminados
    
    def is_empty(self) -> bool:
        # Verifica si la cola está vacía
        return len(self._elements) == 0
    
    def decrease_priority(self, e: E, new_priority: P) -> None:
        # Disminuye la prioridad de un elemento
        for i, (element, priority) in enumerate(self._elements):
            if element == e:
                # Si la nueva prioridad es menor, eliminamos y agregamos de nuevo
                if new_priority < priority:
                    self._elements.pop(i)
                    self.add(e, new_priority)
                return
    
    def __repr__(self) -> str:
        # Representación de la cola con elementos y sus prioridades
        return f'ColaPrioridad{[(e, p) for e, p in self._elements]}'
    
    def elements(self) -> List[E]:
        # Devuelve una lista de los elementos (sin las prioridades)
        return [e for e, _ in self._elements]