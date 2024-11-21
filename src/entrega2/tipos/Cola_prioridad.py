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
        self._elements: List[Tuple[E, P]] = [] #El constructor inicializa _elements, una lista vacía de tuplas en la forma (elemento, prioridad)
    
    def add(self, e: E, priority: P) -> None: # agregar un nuevo elemento e con una prioridad priority
        index = self.index_order(priority) #Llama a index_order(priority) para encontrar la posición donde el elemento debe ser insertado (según su prioridad).
        self._elements.insert(index, (e, priority)) #Usa self._elements.insert(index, (e, priority)) para insertar el elemento en el índice correcto, manteniendo la lista ordenada por prioridad.
    
    def index_order(self, priority: P) -> int: #Este método encuentra la posición en la que debe insertarse un nuevo elemento basado en su prioridad.
        for index, (_, p) in enumerate(self._elements): #Recorre self._elements y, por cada elemento (element, p), compara priority con p.
            if priority < p: #Si priority es menor que p (es decir, tiene mayor prioridad), devuelve el índice actual, ya que debe insertarse antes.
                return index
        return len(self._elements) #Si ningún elemento tiene menor prioridad, devuelve len(self._elements), indicando que el nuevo elemento debe agregarse al final.
    
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