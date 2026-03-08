from classes.CavaleiroBronze import CavaleiroBronze
from classes.CavaleiroOuro import CavaleiroOuro
from classes.Batalha import Batalha

def main():

    ''' testando se a função de tempo gasto por batalha está funcionando
    cavaleiroOuro = cavaleirosDeOuro[0]
    cavaleirosBronze = cavaleirosDeBronze
    calc = Batalha()
    print(calc.tempoGastoPorBatalha(cavaleiroOuro, cavaleirosBronze))
    print(cavaleirosDeBronze)
    '''

    cavaleiroOuro = CavaleiroOuro.alocarCavaleirosDeOuroCsvParaLista('csv/niveldeDificuldadeDasCasas.csv')
    print(cavaleiroOuro)

    cavaleiroBronze = CavaleiroBronze.alocarCavaleirosDeBronzeCsvParaLista('csv/poderCosmicoDosCavaleiros.csv')
    print(cavaleiroBronze)

    cavaleirosBronze = [cavaleiroBronze[0], cavaleiroBronze[1]]

    batalha = Batalha(0, cavaleiroOuro=cavaleiroOuro[0], cavaleiroBronze=cavaleirosBronze)
    print(batalha.cavaleiroOuro)
    print(batalha.cavaleiroBronze)
    batalha.tempoGastoPorBatalha()

    print(batalha.tempo)
    print(cavaleiroBronze)

if __name__ == "__main__":
    main()