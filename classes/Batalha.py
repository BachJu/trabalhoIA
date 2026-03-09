from .CavaleiroBronze import *
from .CavaleiroOuro import *

class BatalhaHeuristica:
    def __init__(self, cavaleirosBronze, cavaleirosOuro, ordemCasas):
        cavaleirosBronze: list[CavaleiroBronze]
        cavaleirosOuro: list[CavaleiroOuro]
        ordemCasas: list

        self.cavaleirosBronze = cavaleirosBronze
        self.cavaleirosOuro = cavaleirosOuro
        self.ordemCasas = ordemCasas

    def cavaleirosDisponiveis(self):
        return [cavaleiro for cavaleiro in self.cavaleirosBronze if cavaleiro.pontosDeEnergia > 0]

    def somaPoderCosmico(self, cavaleiros):
        return sum(cavaleiro.poderCosmico for cavaleiro in cavaleiros)

    def tempoPorBatalha(self, cavaleiros_bronze, cavaleiro_ouro):
        poderCosmicoTotal = self.somaPoderCosmico(cavaleiros_bronze)
        tempoPorBatalha = cavaleiro_ouro.dificuldade / poderCosmicoTotal
        return tempoPorBatalha

    def batalhaPorCasa(self, cavaleirosBronze, cavaleiroOuro):
        tempoPorBatalha = self.tempoPorBatalha(cavaleirosBronze, cavaleiroOuro)

        #cavaleiros_nomes = [c.nome for c in cavaleirosBronze]
        #print(f"Batalha na casa {cavaleiroOuro.casa}: Cavaleiros {', '.join(cavaleiros_nomes)} enfrentaram {cavaleiroOuro.casa} e o tempo foi {tempoPorBatalha:.2f}.")

        for cavaleiro in cavaleirosBronze:
            cavaleiro.gastarPontosDeEnergia()

        return tempoPorBatalha

    def h(self):
        cavaleirosBronzeDisponiveis = sorted(self.cavaleirosDisponiveis(), key=lambda x: x.poderCosmico, reverse=True)
        casasOuroRestantes = sorted(self.cavaleirosOuro, key=lambda x: x.dificuldade, reverse=True)
        
        tempoEstimadoTotal = 0
        batalhasDetalhadas = []

        for casa_index in self.ordemCasas:
            cavaleiroOuro = casasOuroRestantes[casa_index]
            
            cavaleirosSelecionadosParaBatalha = []

            for cavaleiroBronze in cavaleirosBronzeDisponiveis:
                if cavaleiroBronze.pontosDeEnergia > 0 and len(cavaleirosSelecionadosParaBatalha) < 2:
                    cavaleirosSelecionadosParaBatalha.append(cavaleiroBronze)
            
            if cavaleirosSelecionadosParaBatalha:
                tempoPorBatalha = self.batalhaPorCasa(cavaleirosSelecionadosParaBatalha, cavaleiroOuro)
                tempoEstimadoTotal += tempoPorBatalha

                cavaleirosNomes = [cavaleiro.nome for cavaleiro in cavaleirosSelecionadosParaBatalha]

                batalhasDetalhadas.append({
                    'casa': cavaleiroOuro.casa,
                    'cavaleiros': cavaleirosNomes,
                    'tempo_batalha': tempoPorBatalha
                })

        return tempoEstimadoTotal, batalhasDetalhadas