'''
Created on 6 nov 2024

@author: User
'''

from __future__ import annotations
from entrega2.tipos.Lista_ordenada import ListaOrdenada
from typing import TypeVar

E=TypeVar('E')
R=TypeVar('R')

class ListaOrdenadaSinRepeticion(ListaOrdenada[E, R]):
    def add(self, e: E) -> None:
        if e not in self._elements:
            super().add(e)

    
    def __repr__(self) -> str:
        return f"ListaOrdenadaSinRepeticion({self._elements})"