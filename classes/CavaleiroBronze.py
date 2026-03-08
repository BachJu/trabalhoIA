import os
import pandas as pd

class CavaleiroBronze:
    index: int
    nome: str
    poderCosmico: float
    pontosDeEnergia: int

    def __init__(self, index, nome, poderCosmico, pontosDeEnergia):
        self.index = index
        self.nome = nome
        self.poderCosmico = poderCosmico
        self.pontosDeEnergia = pontosDeEnergia
    
    def alocarCavaleirosDeBronzeCsvParaLista(caminho):
        if not os.path.exists(caminho):
            raise FileNotFoundError(f"O caminho não foi encontrado: {caminho}")
        
        if not os.path.isfile(caminho):
            raise ValueError(f"O caminho não é um arquivo: {caminho}")

        if not caminho.lower().endswith('.csv'):
            raise ValueError(f"O arquivo não é um csv: {caminho}")
        
        colunas = ['index', 'cavaleiro', 'poderCosmico', 'pontosDeEnergia']

        df = pd.read_csv(caminho, sep=';')

        if not (set(colunas).issubset(df.columns)):
            print("O csv não possui as colunas esperadas.")
            return
        
        #definir uma lista com todos os Cavaleiros de Bronze
        cavaleirosDeBronze = [CavaleiroBronze(row["index"], row["cavaleiro"], row["poderCosmico"], row["pontosDeEnergia"]) for i, row in df.iterrows()]

        #print(cavaleirosDeBronze)
        return cavaleirosDeBronze
    
    def gastarPontosDeEnergia(self):
        self.pontosDeEnergia -= 1
        try:
            self.atualizarCsv()
        except:
            print("Não foi possivel atualizar o csv")
    
    def atualizarCsv(self):
        '''
        Função responsável de atualizar o csv quando for gasto pontos de energia
        '''
        caminho = '/csv/poderCosmicoDosCavaleiros.csv'
        
        df = pd.read_csv(caminho, sep=';')
        df.loc[df['index'] == self.index, 'pontosDeEnergia'] = self.pontosDeEnergia
        df.to_csv(caminho, sep=';', index=False)
    
    #para quando for imprimir só um objeto
    def __str__(self):
        return f"Cavaleiro -> {self.nome} | Poder cosmico -> {self.poderCosmico} | Pontos de energia -> {self.pontosDeEnergia}"
    
    #para quando for imprimir a lista
    def __repr__(self):
        return f"\nCavaleiro -> {self.nome} | Poder cosmico -> {self.poderCosmico} | Pontos de energia -> {self.pontosDeEnergia}"