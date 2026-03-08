from .CavaleiroBronze import *
from .CavaleiroOuro import *

class Batalha:
    cavaleiroOuro: CavaleiroOuro
    cavaleiroBronze: list[CavaleiroBronze]

    def __init__(self, tempo, cavaleiroOuro, cavaleiroBronze):
        self.tempo = tempo
        self.cavaleiroOuro = cavaleiroOuro
        self.cavaleiroBronze = cavaleiroBronze

    def tempoGastoPorBatalha(self):
        somaDoPoderCosmico = 0

        for cavaleiro in self.cavaleiroBronze:
            somaDoPoderCosmico += cavaleiro.poderCosmico
            cavaleiro.gastarPontosDeEnergia()
        
        deficuldadeDaCasa = self.cavaleiroOuro.dificuldade

        self.tempo = deficuldadeDaCasa / somaDoPoderCosmico

        return self.tempo
    
    def heuristica():
        '''
        
        '''

    def __str__(self):
        return f"Tempo gasto em batalha -> {self.tempo}"