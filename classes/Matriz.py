from typing import Iterator

from Terrenos import *
from Quadrado import *

#Classe para representar a matriz escolhida pelo usuário
class Matriz:
    quadrados: list[Quadrado]

    #inicializando a lista de Quadrados
    def __init__(self, quadrados=None):
        self.quadrados = [] if quadrados == None else quadrados
        
        #inicializa e verifica se há somente um destino ou inicio
        self.validar_destino()
        self.validar_inicio()

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
    
    #descobrindo qual objeto Quadrado é a entrada
    #utilizamos a função next da classe Iterator para auxiliar
    def entrada(self) -> Quadrado:
        return next(quad for quad in self if quad.terreno is Terrenos.INICIO)

    #descobrindo qual objeto Quadrado é o destino
    #utilizamos a função next da classe Iterator para auxiliar
    def destino(self) -> Quadrado:
        return next(quad for quad in self if quad.terreno is Terrenos.DESTINO)

    #funções para validar se há somente um inicio e somente um destino
    def validar_inicio(self):
        soma = 0
        for quadrado in self.quadrados:
            if quadrado.terreno == Terrenos.INICIO:  
                soma +=1
        if soma != 1:
            raise ValueError("É preciso uma única entrada!")
    
    def validar_destino(self):
        soma = 0
        for quadrado in self.quadrados:
            if quadrado.terreno == Terrenos.DESTINO:  
                soma +=1
        if soma != 1:
            raise ValueError("É preciso um único destino!")

#objeto matriz para testes das funções e da classe em geral  
matriz = Matriz(
    quadrados=(
        Quadrado(0, 0, 0, Terrenos.NENHUM),
        Quadrado(1, 0, 1, Terrenos.PLANO),
        Quadrado(2, 0, 2, Terrenos.ROCHOSO),
        Quadrado(3, 0, 3, Terrenos.PLANO),
        Quadrado(4, 1, 0, Terrenos.MONTANHA),
        Quadrado(5, 1, 1, Terrenos.PLANO),
        Quadrado(6, 1, 2, Terrenos.INICIO),
        Quadrado(7, 1, 3, Terrenos.DESTINO)
    )
)

quadrado = matriz.entrada()
print(quadrado.index)