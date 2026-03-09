from classes.CavaleiroBronze import CavaleiroBronze
from classes.CavaleiroOuro import CavaleiroOuro
from classes.Batalha import BatalhaHeuristica

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

if __name__ == "__main__":
    main()