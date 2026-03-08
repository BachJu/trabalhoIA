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