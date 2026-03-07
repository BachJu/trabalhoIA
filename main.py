import pandas as pd

from classes.Cavaleiro import CavaleiroOuro
from classes.Cavaleiro import CavaleiroBronze
from classes.Cavaleiro import Batalha

def main():
    '''
    
    '''

    #caminho onde está localizada as informações dos Cavaleiros de Ouro
    caminho = 'nivelDeDificuldadeDasCasas.csv'
    df = pd.read_csv(caminho, sep=';')
    #definir uma lista com todos os Cavaleiros de Ouro
    cavaleirosDeOuro = [CavaleiroOuro(row['casa'], row['dificuldade']) for i, row in df.iterrows()]

    #print(cavaleirosDeOuro)

    #caminho onde está localizada todas as informações dos Cavaleiros de Bronze
    caminho = 'poderCosmicoDosCavaleiros.csv'
    df = pd.read_csv(caminho, sep=';')
    #definir uma lista com todos os Cavaleiros de Bronze
    cavaleirosDeBronze = [CavaleiroBronze(row["cavaleiro"], row["poderCosmico"], row["pontosDeEnergia"]) for i, row in df.iterrows()]

    #print(cavaleirosDeBronze)

    ''' testando se a função de tempo gasto por batalha está funcionando
    cavaleiroOuro = cavaleirosDeOuro[0]
    cavaleirosBronze = cavaleirosDeBronze
    calc = Batalha()
    print(calc.tempoGastoPorBatalha(cavaleiroOuro, cavaleirosBronze))
    print(cavaleirosDeBronze)
    '''

if __name__ == "__main__":
    main()