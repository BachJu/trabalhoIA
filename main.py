from classes.CavaleiroBronze import CavaleiroBronze
from classes.CavaleiroOuro import CavaleiroOuro
from classes.Batalha import BatalhaHeuristica
from classes.buscaA import *
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def main():
    result = ""
    ouro_path = os.path.join(script_dir, 'csv', 'cavaleirosDeOuro.csv')
    cavaleirosOuro = CavaleiroOuro.alocarCavaleirosDeOuroCsvParaLista(ouro_path)

    bronze_path = os.path.join(script_dir, 'csv', 'cavaleirosDeBronze.csv')
    cavaleirosBronze = CavaleiroBronze.alocarCavaleirosDeBronzeCsvParaLista(bronze_path)

    #carregando a matriz
    dados = carregar_matriz()

    matr, inicio, fim, casas_lista = dados

    #ao invés de utilizarmos a função, utilizamos o calculo_rotas que lida com as casas dos cavaleiros
    custo_matriz, paths = calculo_rotas(matr, casas_lista, inicio, fim)

    ordem_fixa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    batalha = BatalhaHeuristica(cavaleirosBronze, cavaleirosOuro, ordem_fixa)
    tempo, batalhas = batalha.h()
    result += "-" * 30 + "\n"
    result += f"Tempo estimado total para vencer todas as batalhas: {tempo:.2f}\n"
    result += f"Tempo total (batalhas + caminho): {tempo + custo_matriz:.2f} min\n"
    result += "-" * 30 + "\n"
    for batalha in batalhas[::-1]: #inverter a ordem para mostrar a primeira casa primeiro
        result += f"Casa: {batalha['casa']}\n"
        result += f"Cavaleiros: {', '.join(batalha['cavaleiros'])}\n"
        result += f"Tempo da batalha: {batalha['tempo_batalha']:.2f}\n"
        result += "-" * 30 + "\n"

    result += "\n"
    result += f"Tempo de busca A* -> {custo_matriz} min\n"

    return result, paths

