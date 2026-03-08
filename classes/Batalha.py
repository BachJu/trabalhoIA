from CavaleiroBronze import *
from CavaleiroOuro import *

class Batalha:
    cavaleiroOuro: CavaleiroOuro
    cavaleiroBronze: list[CavaleiroBronze]

    def __init__(self, cavaleiroOuro, cavaleiroBronze=None):
        self.cavaleiroOuro = cavaleiroOuro
        self.cavaleiroBronze = cavaleiroBronze

    def tempoGastoPorBatalha(self, cavaleiroOuro, cavaleirosBronze):
        somaDoPoderCosmico = 0

        for cavaleiro in cavaleirosBronze:
            somaDoPoderCosmico += cavaleiro.poderCosmico
            cavaleiro.gastarPontosDeEnergia()
        
        deficuldadeDaCasa = cavaleiroOuro.dificuldade

        self.tempo = deficuldadeDaCasa / somaDoPoderCosmico

        return self.tempo

    def __str__(self):
        return f"Tempo gasto em batalha -> {self.tempo}"