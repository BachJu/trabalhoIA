from classes.CavaleiroBronze import CavaleiroBronze
from classes.CavaleiroOuro import CavaleiroOuro
from classes.Batalha import BatalhaHeuristica
from classes.buscaA import *

def main():
    cavaleirosOuro = CavaleiroOuro.alocarCavaleirosDeOuroCsvParaLista('csv/cavaleirosDeOuro.csv')
    print(cavaleirosOuro)
    print("\n")

    cavaleirosBronze = CavaleiroBronze.alocarCavaleirosDeBronzeCsvParaLista('csv/cavaleirosDeBronze.csv')
    print(cavaleirosBronze)
    print("\n")

    ordem_fixa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    batalha = BatalhaHeuristica(cavaleirosBronze, cavaleirosOuro, ordem_fixa)
    tempo, batalhas = batalha.h()
    print("-" * 30)
    print(f"Tempo estimado total para vencer todas as batalhas: {tempo:.2f}")
    print("-" * 30)
    for batalha in batalhas:
        print(f"Casa: {batalha['casa']}")
        print(f"Cavaleiros: {', '.join(batalha['cavaleiros'])}")
        print(f"Tempo da batalha: {batalha['tempo_batalha']:.2f}")
        print("-" * 30)

    print("\n")
    print(cavaleirosBronze)
    print("\n")
    
    #carregando a matriz
    dados = carregar_matriz()

    matr, inicio, fim, casas_lista = dados

    #ao invés de utilizarmos a função, utilizamos o calculo_rotas que lida com as casas dos cavaleiros
    custo_matriz = calculo_rotas(matr, casas_lista, inicio, fim)
    print(f"Tempo de busca A* -> {custo_matriz} min")

if __name__ == "__main__":
    main()

