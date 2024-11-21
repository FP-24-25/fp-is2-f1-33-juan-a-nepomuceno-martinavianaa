'''
Created on 6 nov 2024

@author: User
'''
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

E=TypeVar('E')



class AgregadoLineal(ABC, Generic[E]): #clase agregadolineal que hereda abc (la convierte en clase abstracta) y generic e(acepta cualquier tipo)
    
    def __init__(self): #constructor, como la instrucción inicial, Esto significa que puedes crear una nueva instancia de la clase simplemente llamando a AgregadoLineal() sin tener que darle información adicional en el momento de crearla.
        self._elements: List[E] = [] #crea una lista vacía _elements que puede tener cualquier tipo
    
#métodos comunes    
    def size(self) -> int:
        return len(self._elements)
    
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    def elements(self) -> List[E]:
        return self._elements.copy()
    
#método abstracto, debe ser implemetnado en cualquier subclase    
    @abstractmethod
    def add(self, e: E) -> None:
        pass
    
    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)
    
    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0) #elimina el primer elemento y lo devuelve
    
    def remove_all(self) -> List[E]:
        elementos_eliminados=[]
        while not self.is_empty():
            elementos_eliminados.append(self.remove())
        return elementos_eliminados
    
     
    