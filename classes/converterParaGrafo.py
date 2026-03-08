from typing import TypeAlias

from Quadrado import Quadrado
from Matriz import Matriz
from Terrenos import Terrenos


#Para que possamos nos referir a um quadrado como um nó
No: TypeAlias = Quadrado

class Aresta:
    no1: No
    no2: No

#conjunto de nós
def construir_nos(matriz: Matriz) -> set[No]:
    nos: set[No] = set()
    for quadrado in matriz:
        if quadrado.terreno is not Terrenos.NENHUM:
            nos.add(quadrado)
    
    return nos

#conjunto de arestas
def construir_arestas(matriz: Matriz, nos: set[No]) -> set[Aresta]:
    arestas: set[Aresta] = set()
    
    #verificando as ligações de cada nó no conjunto
    for no_raiz in nos:
        #seguindo para a direita
        no = no_raiz
        for x in range(no.coluna + 1, matriz.largura):
            no = matriz.quadrados[no.linha * matriz.largura + x]
            #serve para não acrescentar nos cujos quadrados são vazios
            if no in nos:
                arestas.add(Aresta(no_raiz, no))
                break
        
        #seguindo para baixo
        no = no_raiz
        for y in range(no.linha + 1, matriz.altura):
            no = matriz.quadrados[y * matriz.largura + no.coluna]
            if no in nos:
                arestas.add(Aresta(no_raiz, no))
                break
    
    return arestas



matriz = Matriz(
    quadrados=(
        Quadrado(0, 0, 0, Terrenos.PLANO),
        Quadrado(1, 0, 1, Terrenos.PLANO),
        Quadrado(2, 0, 2, Terrenos.ROCHOSO),
        Quadrado(3, 0, 3, Terrenos.PLANO),
        Quadrado(4, 1, 0, Terrenos.MONTANHA),
        Quadrado(5, 1, 1, Terrenos.PLANO),
        Quadrado(6, 1, 2, Terrenos.INICIO),
        Quadrado(7, 1, 3, Terrenos.DESTINO)
    )
)

conjunto = construir_nos(matriz)
print(conjunto)

arestas = construir_arestas(matriz, conjunto)
print(arestas)