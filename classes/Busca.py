from Matriz import *
from Quadrado import *
from Terrenos import *

CUSTO_MAX = 720

#FUNÇÃO VERIFICAR DEPOIS
#Função para retornar vizinhos de uma determinada posição
#Tuple = [ESQ, DIR, CIMA, BAIXO]
def listar_vizinhos(matriz: Matriz, quadrado: Quadrado) -> list[Quadrado]:
        vizinhos = []
        esq = quadrado.index - 1
        #verifica se o quadrado de indice anterior não foi visitado e está na mesma linha que o quadrado atual
        if (not matriz.quadrados[esq].visitado and matriz.quadrados[esq].linha == quadrado.linha):
            vizinhos.append(matriz.quadrados[esq])

        #verifica se o quadrado de indice posterior está na mesma linha que o quadrado atual
        if (matriz.quadrados[quadrado.index + 1].linha == quadrado.linha):
            vizinhos.append(matriz.quadrados[quadrado.index + 1])
        
        #verifica se o quadrado de indice acima está na mesma coluna que o quadrado atual
        if (matriz.quadrados[quadrado.index - matriz.largura()].coluna == quadrado.coluna):
            vizinhos.append(matriz.quadrados[quadrado.index - matriz.largura()])
        
        if (matriz.quadrados[quadrado.index + matriz.largura()].coluna == quadrado.coluna):
            vizinhos.append(matriz.quadrados[quadrado.index + matriz.largura()])

        
        return vizinhos

#calcula o custo da posição relativa
def calcular_heuristica(col_atual, lin_atual, col_dest, lin_dest):
    return ((col_atual - col_dest) ** 2 + (lin_atual - lin_dest) ** 2) * 0.5

def prox_quadrado(vizinhos: list[Quadrado], destino: Quadrado) -> Quadrado:
    menor_custo = 999
    for quadrado in vizinhos:
        custo = quadrado.terreno + calcular_heuristica(quadrado.coluna, quadrado.linha, destino.coluna, destino.linha)
        if custo < menor_custo: 
            menor_custo = custo
            quad = quadrado
    
    return quad

#def printar_caminho(quadrado: Quadrado):

def chegou(col_atual, lin_atual, col_dest, lin_dest):
    return col_atual == col_dest and lin_atual == lin_dest

def busca_gulosa(matriz: Matriz):
    #minutos gastos até então
    min_gasto = 0
    #o agente inicia-se na entrada da matriz
    agente = matriz.entrada()
    destino = matriz.destino()

    #verificamos se o inicio e o destino estão na mesma posição

    if chegou(agente.coluna, agente.linha, destino.coluna, destino.linha):
        print(f'O agente já está no destino e gastou {min_gasto} minutos')

    agente.visitado = True
    lista_visitados = [agente]
    print(f'Visitados\n({agente.linha}, {agente.coluna}) ->')

    while(True):
        agente = prox_quadrado(listar_vizinhos(matriz, agente), destino)
        lista_visitados.append(agente)
        agente.visitado = True
        print(f'({agente.linha}, {agente.coluna}) ->')
        if chegou(agente.coluna, agente.linha, destino.coluna, destino.linha):
            print("chegamos :D")
            break







matriz = Matriz(
    quadrados=(
        Quadrado(0, 0, 0, Terrenos.INICIO),
        Quadrado(1, 0, 1, Terrenos.PLANO),
        Quadrado(2, 0, 2, Terrenos.ROCHOSO),
        Quadrado(3, 0, 3, Terrenos.PLANO),
        Quadrado(4, 1, 0, Terrenos.PLANO),
        Quadrado(5, 1, 1, Terrenos.PLANO),
        Quadrado(6, 1, 2, Terrenos.PLANO),
        Quadrado(7, 1, 3, Terrenos.DESTINO),
        Quadrado(8, 2, 0, Terrenos.ROCHOSO),
        Quadrado(9, 2, 1, Terrenos.PLANO),
        Quadrado(10, 2, 2, Terrenos.PLANO),
        Quadrado(11, 2, 3, Terrenos.ROCHOSO)
    )
)

a = matriz.entrada()
vizinhos = listar_vizinhos(matriz, a)
menor = prox_quadrado(vizinhos, matriz.destino())
print("o produto mais barato e ", menor.index)

busca_gulosa(matriz)