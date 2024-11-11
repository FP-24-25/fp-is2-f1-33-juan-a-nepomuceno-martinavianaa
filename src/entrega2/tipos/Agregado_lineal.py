'''
Created on 6 nov 2024

@author: User
'''
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

E=TypeVar('E')



class AgregadoLineal(ABC, Generic[E]):
    
    def __init__(self):
        self._elements: List[E] = []
    
    def size(self) -> int:
        return len(self._elements)
    
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    def elements(self) -> List[E]:
        return self._elements.copy()
    
    @abstractmethod
    def add(self, e: E) -> None:
        pass
    
    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)
    
    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)
    
    def remove_all(self) -> List[E]:
        elementos_eliminados=[]
        while not self.is_empty():
            elementos_eliminados.append(self.remove())
        return elementos_eliminados
    
     
    