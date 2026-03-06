from dataclasses import dataclass
from typing import Iterator

from Quadrado import *

#Classe para representar a matriz escolhida pelo usuário
class Matriz:
    quadrados: list[Quadrado, ...]

    def __init__(self, quadrados=None):
        self.quadrados = [] if quadrados == None else quadrados

    #função para que a classe se torne iterável
    def __iter__(self) -> Iterator[Quadrado]:
        return iter(self.quadrados)
    
    def __getitem__(self, index: int) -> Quadrado:
        return self.quadrados[index]

    #pegando a largura e a altura da nossa matriz
    def largura(self) -> int:
        return max(Quadrado.coluna for Quadrado in self) + 1
    
    def altura(self) -> int:
        return max(Quadrado.linha for Quadrado in self) + 1
    
    #descobrindo qual é a entrada
    def entrada(self) -> Quadrado:
        for quad in self.quadrados:
            if quad.terreno is Terrenos.INICIO:
                return quad

    #funções para validar se há somente um inicio e somente um destino
    def validar_inicio(self):
        soma = 0
        for quadrado in self.quadrados:
            print(quadrado.terreno)
            if quadrado.terreno == Terrenos.INICIO:  
                soma +=1
        if soma > 1:
            raise ValueError("Não é possível ter mais do que um inicio.")
    
    def validar_destino(self):
        soma = 0
        for quadrado in self.quadrados:
            print(quadrado.terreno)
            if quadrado.terreno == Terrenos.DESTINO:  
                soma +=1
        if soma > 1:
            raise ValueError("Não é possível ter mais do que um destino.")
        
matriz = Matriz(
    quadrados=(
        Quadrado(0, 0, 0, Terrenos.NENHUM),
        Quadrado(1, 0, 1, Terrenos.PLANO),
        Quadrado(2, 0, 2, Terrenos.INICIO),
        Quadrado(3, 0, 3, Terrenos.PLANO),
        Quadrado(4, 1, 0, Terrenos.MONTANHA),
        Quadrado(5, 1, 1, Terrenos.PLANO),
        Quadrado(6, 1, 2, Terrenos.DESTINO),
        Quadrado(7, 1, 3, Terrenos.DESTINO)
    )
)

print(matriz.validar_destino())