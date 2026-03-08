class CavaleiroBronze:
    nome: str
    poderCosmico: float
    pontosDeEnergia: int

    def __init__(self, nome, poderCosmico, pontosDeEnergia):
        self.nome = nome
        self.poderCosmico = poderCosmico
        self.pontosDeEnergia = pontosDeEnergia
    
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