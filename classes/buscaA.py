import heapq
import csv

CAMINHO_ARQ = r'.\csv\matriz.csv'

def carregar_matriz():
    matriz = []
    casas = []
    inicio = None
    fim = None

    terrenos = {
        0: -1,   # Inicio, valores de flag, somente
        13: -2,  # Fim
        14: 200, # Montanha
        15: 1,   # Plano
        16: 5    # Rochoso
    }

    try:
        with open(CAMINHO_ARQ, 'r', newline='') as arquivo:
            csv_reader = csv.reader(arquivo, delimiter=';')
            for i, linha in enumerate(csv_reader):
                linha_processada = []
                for j, valor_str in enumerate(linha):
                    valor = int(valor_str)
                    
                    if valor == 0:
                        inicio = (i, j)
                        custo = -1
                    elif 1 <= valor <= 12:
                        casas.append([i, j, valor])
                        custo = 1 # Custo especial para casas de cavaleiros
                    elif valor == 13:
                        fim = (i, j)
                        custo = -2
                    else:
                        custo = terrenos.get(valor, 1)
                    
                    linha_processada.append(custo)
                matriz.append(linha_processada)
        
        return matriz, inicio, fim, casas
    except FileNotFoundError:
        print("Arquivo não encontrado.")


def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def busca_a(matriz, inicio, fim):
    rows = len(matriz)
    cols = len(matriz[0])
    
    # heapq armazena (f, i, j)
    lista_aberta = [(0, inicio[0], inicio[1])]
    
    # Armazena o melhor custo g encontrado para cada nó
    g_score = {inicio: 0}
    
    # Armazena o caminho: filho -> pai
    veio_de = {}

    while lista_aberta:
        _, curr_i, curr_j = heapq.heappop(lista_aberta)
        atual = (curr_i, curr_j)

        if atual == fim:
            return reconstruir_caminho(veio_de, atual), g_score[atual]

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            vizinho_i, vizinho_j = curr_i + di, curr_j + dj
            vizinho = (vizinho_i, vizinho_j)

            if 0 <= vizinho_i < rows and 0 <= vizinho_j < cols:
                # O custo para mover para o vizinho
                custo_movimento = matriz[vizinho_i][vizinho_j]
                if custo_movimento < 0: custo_movimento = 1 # Ajuste para início/fim
                
                tentativa_g = g_score[atual] + custo_movimento

                if vizinho not in g_score or tentativa_g < g_score[vizinho]:
                    veio_de[vizinho] = atual
                    g_score[vizinho] = tentativa_g
                    f_score = tentativa_g + heuristica(vizinho, fim)
                    heapq.heappush(lista_aberta, (f_score, vizinho_i, vizinho_j))

    return None, float('inf')

def reconstruir_caminho(veio_de, atual):
    caminho = []
    while atual in veio_de:
        caminho.append(atual)
        atual = veio_de[atual]
    caminho.append(atual)
    return caminho[::-1]

# Execução

        
"""
if dados:
    matr, start, end, casas_lista = dados
    # Exemplo de uso
    destino_teste = (37, 21)
    path, total_cost = busca_a(matr, (37,21), (31, 17))
    
    if path:
        print(f"Caminho encontrado! Custo: {total_cost}")
        print(" -> ".join(map(str, path)))
    else:
        print("Caminho não encontrado.")
"""

def calculo_rotas(matriz, casas_lista, inicio, fim):
    casas_lista.sort(key=lambda x: x[2])
    inicio_atual = inicio
    for casa in casas_lista:
        destino_atual = (casa[0], casa[1])
        caminho, total_custo = busca_a(matriz, inicio_atual, destino_atual)

        if caminho:
            print(f"Caminho encontrado! Custo: {total_custo}")
            print(" -> ".join(map(str, caminho)))
        inicio_atual = destino_atual
    destino_atual = fim    
    caminho, total_custo = busca_a(matriz, inicio_atual, destino_atual)

    if caminho:
        print(f"Caminho encontrado! Custo: {total_custo}")
        print(" -> ".join(map(str, caminho)))


dados = carregar_matriz()

matr, start, end, casas_lista = dados

calculo_rotas(matr, casas_lista, start, end)