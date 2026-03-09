import heapq
import csv

#valor global para o caminho do arquivo matriz.csv
CAMINHO_ARQ = r'.\csv\matriz.csv'

def carregar_matriz():
    #matriz vazia para guardar o arquivo csv
    matriz = []
    #lista para representar as casas dos cavaleiros
    casas = []
    #transformaremos em tuplas
    inicio = None
    fim = None

    #dicionário com os custos de cada terreno
    terrenos = {
        14: 200, # Montanha
        15: 1,   # Plano
        16: 5    # Rochoso
    }

    #tenta abrir o caminho
    try:
        with open(CAMINHO_ARQ, 'r', newline='') as arquivo:
            csv_reader = csv.reader(arquivo, delimiter=';')
            for i, linha in enumerate(csv_reader):
                linha_processada = []
                for j, valor_str in enumerate(linha):
                    valor = int(valor_str)
                    #indir_ica o início
                    if valor == 0:
                        inicio = (i, j)
                        custo = -1
                    #indir_ica as casas dos cavaleiros
                    elif 1 <= valor <= 12:
                        casas.append([i, j, valor])
                        custo = 1 # Custo especial para casas de cavaleiros
                    #indir_ica o fim
                    elif valor == 13:
                        fim = (i, j)
                        custo = -2
                    #caso não seja uma casa especil, verifica os terrenos
                    else:
                        custo = terrenos.get(valor, 1)
                    
                    linha_processada.append(custo)
                #acrescentamos a linha visitada na matriz final
                matriz.append(linha_processada)
        #para auxílio, retornamos a matriz, tulpas que representam onde foi encontrado o início e o fim, uma lisita com o endereço das casas e seu índir_ice
        return matriz, inicio, fim, casas
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo não encontrado.")

#função para o cálculo de heurísticas
#atual e objetivo são tuplas com dois valores
def heuristica(atual, objetivo):
    return abs(atual[0] - objetivo[0]) + abs(atual[1] - objetivo[1])

#busca A*
#parâmetros
def busca_a(matriz: list[tuple], inicio: tuple, fim: tuple):

    #encontramos o valor máximo de linha e coluna da matriz
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    # heapq que armazena (f -> calculado, i, j)
    lista_aberta = [(0, inicio[0], inicio[1])]
    
    #armazena o melhor custo de g
    g_score = {inicio: 0}
    
    #armazena o caminho: filho -> pai
    caminho_percorrido = {}

    #iterando a lista_aberta
    while lista_aberta:
        _, atual_i, atual_j = heapq.heappop(lista_aberta)
        atual = (atual_i, atual_j)

        #verificamos se a posição atual é igual a posição final
        if atual == fim:
            return reconstruir_caminho(caminho_percorrido, atual), g_score[atual]

        #verificação para cada vizinho na ordem direita, esquerda, cima e baixo
        for dir_i, dir_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            vizinho_i, vizinho_j = atual_i + dir_i, atual_j + dir_j
            vizinho = (vizinho_i, vizinho_j)

            #verificando a validade do novo valor
            #ele não pode ser menor que 0 e nem maior do que os limites da matriz
            if 0 <= vizinho_i < linhas and 0 <= vizinho_j < colunas:
                # O custo para mover para o vizinho
                custo_movimento = matriz[vizinho_i][vizinho_j]
                if custo_movimento < 0: custo_movimento = 1 # Ajuste para as flags de início/fim
                
                #calculamos o g para cada vizinho
                tentativa_g = g_score[atual] + custo_movimento

                if vizinho not in g_score or tentativa_g < g_score[vizinho]:
                    caminho_percorrido[vizinho] = atual
                    g_score[vizinho] = tentativa_g
                    f_score = tentativa_g + heuristica(vizinho, fim)
                    heapq.heappush(lista_aberta, (f_score, vizinho_i, vizinho_j))
    #caso não consiga encontrar o caminho, retorna None e um valor inf como flag
    return None, float('inf')

#reconstruindo o caminho do objetivo até o início
def reconstruir_caminho(caminho_percorrido, atual):
    #lista vazia para guardar o caminho
    caminho = []
    while atual in caminho_percorrido:
        caminho.append(atual)
        atual = caminho_percorrido[atual]
    caminho.append(atual)
    #retornamos o caminho invertido
    return caminho[::-1]

def calculo_rotas(matriz, casas_lista, inicio, fim) -> int:
    #inicializando variável para guardar o total do custo do caminho
    total_custo = 0
    #ordenando a lista pelo índice dos números das casas dos cavaleiros de ouro
    casas_lista.sort(key=lambda x: x[2])
    #iniciamos na posição de início
    inicio_atual = inicio

    #iteração no vetor de casas
    for casa in casas_lista:

        destino_atual = (casa[0], casa[1])
        #a nossa busca A* retorna um caminho e o custo total desse caminho
        caminho, custo_caminho = busca_a(matriz, inicio_atual, destino_atual)

        #caso seja possível encontrar um caminho, somamos seu custo ao custo total do algoritmo
        if caminho:
            #Para fins de visualização do caminho, remova do comentário
            #print(f"Caminho encontrado.\n Custo: {custo_caminho}")
            #print(" -> ".join(map(str, caminho)))
            total_custo +=custo_caminho
        else:
            raise ValueError("Impossível encontrar um caminho.")
        
        #setamos o início da próxima iteração como o destino que foi buscado
        inicio_atual = destino_atual
    #por fim, setamos o destino final
    destino_atual = fim    
    caminho, custo_caminho = busca_a(matriz, inicio_atual, destino_atual)

    if caminho:
        #Para fins de visualização do caminho, remova do comentário
        #print(f"Caminho encontrado.\n Custo: {custo_caminho}")
        #print(" -> ".join(map(str, caminho)))
        total_custo +=custo_caminho
        #print(f"O algoritmo de busca A* gastou no total: {total_custo}")
    else:
            raise ValueError("Impossível encontrar um caminho.")
    
    #retorno do total gasto no algoritmo
    return total_custo
