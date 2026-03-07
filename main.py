import csv

from classes.Cavaleiro import CavaleiroOuro
from classes.Cavaleiro import CavaleiroBronze

def main():
    '''
    
    '''

    #definir uma lista com todos os cavaleiros de ouro
    cavaleirosOuro = []

    #abrir o arquivo que está localizado os níveis de cada caveleiro de ouro
    with open('nivelDeDificuldadeDasCasas.csv', mode="r") as f:
        cavaleirosDeOuro = csv.DictReader(f, delimiter=';')

        for linha in cavaleirosDeOuro:
            cavaleiro = CavaleiroOuro(linha["casa"], linha["dificuldade"])
            #print(cavaleiro)
            cavaleirosOuro.append(cavaleiro)
    

    #definir uma lista com os cavaleiros de bronze
    cavaleirosBronze = []

    #abrir o arquivo que está localizado as informações dos cavaleiros de bronze
    with open('poderCosmicoDosCavaleiros.csv', mode="r") as f:
        cavaleirosDeBronze = csv.DictReader(f, delimiter=';')

        for linha in cavaleirosDeBronze:
            cavaleiro = CavaleiroBronze(linha["cavaleiro"], linha["poderCosmico"], linha["pontosDeEnergia"])
            print(cavaleiro)
            cavaleirosBronze.append(cavaleiro)


if __name__ == "__main__":
    main()