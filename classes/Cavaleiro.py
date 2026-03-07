class CavaleiroBronze:

    def __init__(self, nome, poderCosmico, pontosDeEnergia):
        self.nome = nome
        self.poderCosmico = poderCosmico
        self.pontosDeEnergia = pontosDeEnergia
    
    def gastarPontosDeEnergia(self):
        self.pontosDeEnergia -= 1
    
    def __str__(self):
        return f"Cavaleiro -> {self.nome} | Poder cosmico -> {self.poderCosmico} | Pontos de energia -> {self.pontosDeEnergia}"
    
    def __repr__(self):
        return f"\nCavaleiro -> {self.nome} | Poder cosmico -> {self.poderCosmico} | Pontos de energia -> {self.pontosDeEnergia}"

class CavaleiroOuro:

    def __init__(self, casa, dificuldade):
        self.casa = casa
        self.dificuldade = dificuldade

    def __str__(self):
        return f"Casa -> {self.casa} | Dificuldade -> {self.dificuldade}"

    def __repr__(self):
        return f"\nCasa -> {self.casa} | Dificuldade -> {self.dificuldade}"