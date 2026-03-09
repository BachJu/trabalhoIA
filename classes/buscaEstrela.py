import heapq
import csv

from terreno import *

CAMINHO_ARQ = r'.\csv\matriz.csv'

class No():

    def __init__(self, pai = None, posicao = None):
        self.pai = pai
        self.posicao = posicao

        self.g = 0
        self.h = 0
        self.f = 0
    
    #verifica se os dois são iguais
    def verificar_igualdade(self, outro) -> bool:
        return self.posicao == outro.posicao

"""
def carregar_mapa_e_pontos(caminho_arquivo="mapa.txt"):
    mapa = []
    pontos_de_interesse = {}
    
    mapa_simbolos = {
        'P': 'plano', 'R': 'rochoso', 'M': 'montanhoso'
    }
    casas_simbolos = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C']
    
    try:
        with open(caminho_arquivo, 'r') as f:
            for i, linha in enumerate(f):
                linha_terrenos = []
                caracteres = linha.strip().split()
                
                for j, char in enumerate(caracteres):
                    char_upper = char.upper()
                    if char_upper in mapa_simbolos:
                        linha_terrenos.append(mapa_simbolos[char_upper])
                    elif char_upper in casas_simbolos or char_upper in ['S', 'E']:
                        linha_terrenos.append('casa')
                        pontos_de_interesse[char_upper] = (i, j)
                    else:
                        linha_terrenos.append('plano')
                
                if linha_terrenos:
                    mapa.append(linha_terrenos)
                    
        return mapa, pontos_de_interesse
    except FileNotFoundError:
        return None, None
"""

def matriz() -> list[list]:
    #a matriz será uma lista vazia
    matriz = []
    casas = []

    try:
        with(open(CAMINHO_ARQ, 'r', newline='') as arquivo):
            csv_reader = csv.reader(arquivo, delimiter=';')
            inicio = []
            fim = []
            
            i = 0

            for linha in csv_reader:
                lista = []
                terreno = -99
                for j in range(len(linha)):
                    match int(linha[j]):
                        #inicio
                        case 0:
                            inicio = [i, j]
                            terreno = -1
                        #casas
                        case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
                            #posicao i, j, e numero da casa
                            casas.append([i, j, linha[j]])
                            terreno = 0

                        #destino
                        case 13:
                            fim = [i, j]
                            terreno = -2
                        #montanha
                        case 14:
                            terreno = 200
                        #plano
                        case 15:
                            terreno = 1
                        #rochoso
                        case 16:
                            terreno = 5
                    
                    lista.append(terreno)

                matriz.append(lista)
                i +=1
        
        arquivo.close()
        return matriz, inicio, fim, casas

    except FileNotFoundError:
        print("deu merda ")

matr, inicio, fim, casas = matriz()
print(matr, inicio, fim, casas)
