'''
Created on 6 nov 2024

@author: User
'''

from __future__ import annotations
from entrega2.tipos.Agregado_lineal import AgregadoLineal
from typing import TypeVar

E=TypeVar('E')

class Cola(AgregadoLineal[E]):
    @staticmethod
    def of() -> Cola[E]:
        return Cola()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def __repr__(self) -> str:
        return f"Cola({self._elements})"