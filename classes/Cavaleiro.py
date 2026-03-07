class CavaleiroBronze:

    def __init__(self, nome, poderCosmico, pontosDeEnergia):
        self.nome = nome
        self.poderCosmico = float(poderCosmico)
        self.pontosDeEnergia = int(pontosDeEnergia)
    
    def gastarPontosDeEnergia(self):
        self.pontosDeEnergia -= 1
    
    def atualizarCsv(self):
        '''
        Função responsável de atualizar o csv quando for gasto pontos de energia
        '''
    
    #para quando for imprimir só um objeto
    def __str__(self):
        return f"Cavaleiro -> {self.nome} | Poder cosmico -> {self.poderCosmico} | Pontos de energia -> {self.pontosDeEnergia}"
    
    #para quando for imprimir a lista
    def __repr__(self):
        return f"\nCavaleiro -> {self.nome} | Poder cosmico -> {self.poderCosmico} | Pontos de energia -> {self.pontosDeEnergia}"

class CavaleiroOuro:

    def __init__(self, casa, dificuldade):
        self.casa = casa
        self.dificuldade = int(dificuldade)

    #para quando for imprimir só um obejto
    def __str__(self):
        return f"Casa -> {self.casa} | Dificuldade -> {self.dificuldade}"

    #para quando for imprimir uma lista
    def __repr__(self):
        return f"\nCasa -> {self.casa} | Dificuldade -> {self.dificuldade}"

class Batalha:

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