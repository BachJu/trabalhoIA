from Terrenos import *

#classe com as caracteristicas de cada quadrado
#sendo essas caracteristas:
#index
#linha
#coluna
#e o tipo do terreno
#um quadrado inicializa-se com o terreno vazio
class Quadrado:
    index: int
    linha: int
    coluna: int
    terreno: Terrenos = Terrenos.NENHUM

    def __init__(self, index, linha, coluna, terreno):
        self.index = index
        self.linha = linha
        self.coluna = coluna
        self.terreno = terreno