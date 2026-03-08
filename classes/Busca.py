from Matriz import *
from Quadrado import *
from Terrenos import *

#custo maximo em minutos que o exercício pede
CUSTO_MAX = 720

#Função para retornar vizinhos de uma determinada posição
#Tuple = [ESQ, DIR, CIMA, BAIXO]
def listar_vizinhos(matriz: Matriz, quadrado: Quadrado) -> list[Quadrado]:
        vizinhos = []
        esq = quadrado.index - 1
        dir = quadrado.index + 1
        cima = quadrado.index - matriz.largura()
        baixo = quadrado.index + matriz.largura()

        #verifica se o quadrado de indice anterior está na mesma linha que o quadrado atual
        if (not matriz.quadrados[esq].visitado and matriz.quadrados[esq].linha == quadrado.linha):
            vizinhos.append(matriz.quadrados[esq])

        #verifica se o quadrado de indice posterior está na mesma linha que o quadrado atual
        if (not matriz.quadrados[dir].visitado and matriz.quadrados[dir].linha == quadrado.linha):
            vizinhos.append(matriz.quadrados[dir])
        
        #verifica se o quadrado de indice acima está na mesma coluna que o quadrado atual
        if (cima > 0 and not matriz.quadrados[cima].visitado and matriz.quadrados[cima].coluna == quadrado.coluna):
            vizinhos.append(matriz.quadrados[cima])

        if (baixo <= matriz.max_index() and not matriz.quadrados[baixo].visitado  and matriz.quadrados[baixo].coluna == quadrado.coluna):
            vizinhos.append(matriz.quadrados[baixo])
        
        return vizinhos

#calcula o custo da posição relativa
def calcular_heuristica(col_atual, lin_atual, col_dest, lin_dest):
    return ((col_atual - col_dest) ** 2 + (lin_atual - lin_dest) ** 2) * 0.5

#Define qual será o próximo quadrado escolhido
def prox_quadrado(vizinhos: list[Quadrado], destino: Quadrado) -> Quadrado:
    menor_custo = 999
    for quadrado in vizinhos:
        custo = quadrado.terreno + calcular_heuristica(quadrado.coluna, quadrado.linha, destino.coluna, destino.linha)
        if custo < menor_custo: 
            menor_custo = custo
            quad = quadrado
    
    return quad

#função para imprimir o caminho no terminal
def printar_caminho(lista_visitados: list[Quadrado]):
    print(f'Quadrados visitados')
    for quadrado in lista_visitados:
        if quadrado.terreno == Terrenos.DESTINO: print(f'({quadrado.linha}, {quadrado.coluna})')
        else: print(f'({quadrado.linha}, {quadrado.coluna}) ->', end=' ')

#verifica se o agente chegou ao destino
def chegou(atual: Quadrado, destino: Quadrado):
    return atual.index == destino.index

def busca_aEstrela(matriz: Matriz):
    #minutos gastos até então
    min_gasto = 0
    #o agente inicia-se na entrada da matriz
    agente = matriz.entrada()

    destino = matriz.destino()
    
    #marcamos o agente como visitado e o adicionamos a lista de quadrados visitados
    agente.visitado = True
    lista_visitados = [agente]

   
    #verificamos se já iniciamos no destino
    if chegou(agente, destino):
        print(f'O agente já está no destino e gastou {min_gasto} minutos')

    while(True):
        agente = prox_quadrado(listar_vizinhos(matriz, agente), destino)
        lista_visitados.append(agente)
        agente.visitado = True
        if chegou(agente, destino):
            break

    printar_caminho(lista_visitados)

matriz = Matriz(
    quadrados=(
        Quadrado(0, 0, 0, Terrenos.INICIO),
        Quadrado(1, 0, 1, Terrenos.PLANO),
        Quadrado(2, 0, 2, Terrenos.MONTANHA),
        Quadrado(3, 0, 3, Terrenos.ROCHOSO),
        Quadrado(4, 0, 4, Terrenos.PLANO),
        Quadrado(5, 0, 5, Terrenos.MONTANHA),
        Quadrado(6, 1, 0, Terrenos.MONTANHA),
        Quadrado(7, 1, 1, Terrenos.ROCHOSO),
        Quadrado(8, 1, 2, Terrenos.ROCHOSO),
        Quadrado(9, 1, 3, Terrenos.PLANO),
        Quadrado(10, 1, 4, Terrenos.ROCHOSO),
        Quadrado(11, 1, 5, Terrenos.MONTANHA),
        Quadrado(12, 2, 0, Terrenos.ROCHOSO),
        Quadrado(13, 2, 1, Terrenos.ROCHOSO),
        Quadrado(14, 2, 2, Terrenos.MONTANHA),
        Quadrado(15, 2, 3, Terrenos.MONTANHA),
        Quadrado(16, 2, 4, Terrenos.PLANO),
        Quadrado(17, 2, 5, Terrenos.MONTANHA),
        Quadrado(18, 3, 0, Terrenos.PLANO),
        Quadrado(19, 3, 1, Terrenos.MONTANHA),
        Quadrado(20, 3, 2, Terrenos.MONTANHA),
        Quadrado(21, 3, 3, Terrenos.ROCHOSO),
        Quadrado(22, 3, 4, Terrenos.PLANO),
        Quadrado(23, 3, 5, Terrenos.ROCHOSO),
        Quadrado(24, 4, 0, Terrenos.PLANO),
        Quadrado(25, 4, 1, Terrenos.MONTANHA),
        Quadrado(26, 4, 2, Terrenos.MONTANHA),
        Quadrado(27, 4, 3, Terrenos.ROCHOSO),
        Quadrado(28, 4, 4, Terrenos.PLANO),
        Quadrado(29, 4, 5, Terrenos.PLANO),
        Quadrado(30, 5, 0, Terrenos.PLANO),
        Quadrado(31, 5, 1, Terrenos.PLANO),
        Quadrado(32, 5, 2, Terrenos.MONTANHA),
        Quadrado(33, 5, 3, Terrenos.PLANO),
        Quadrado(34, 5, 4, Terrenos.PLANO),
        Quadrado(35, 5, 5, Terrenos.DESTINO)
    )
)

busca_aEstrela(matriz)