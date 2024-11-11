'''
Created on 6 nov 2024

@author: User
'''

from __future__ import annotations
from entrega2.tipos.Agregado_lineal import AgregadoLineal
from typing import TypeVar

E=TypeVar('E')

class Pila(AgregadoLineal[E]):
    @staticmethod
    def of() -> Pila[E]:
        return Pila()

    def add(self, e: E) -> None:
        self._elements.insert(0, e)

    def __repr__(self) -> str:
        return f"Pila({self._elements})"