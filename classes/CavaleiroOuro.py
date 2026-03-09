import os
import pandas as pd

class CavaleiroOuro:
    casa: str
    dificuldade: int

    def __init__(self, casa, dificuldade):
        self.casa = casa
        self.dificuldade = dificuldade

    '''
    Função responsável por abrir o csv e ler as informações dele

    Parametros
    ----------
    caminho -> caminho para onde o arquivo .csv se encontra

    Retorno
    -------
    cavaleirosDeOuro -> lista com todos os cavaleiros de ouro e sua informação de dificuldade
    '''
    def alocarCavaleirosDeOuroCsvParaLista(caminho):
        if not os.path.exists(caminho):
            raise FileNotFoundError(f"O caminho não foi encontrado: {caminho}")
        
        if not os.path.isfile(caminho):
            raise ValueError(f"O caminho não é um arquivo: {caminho}")

        if not caminho.lower().endswith('.csv'):
            raise ValueError(f"O arquivo não é um csv: {caminho}")
        
        colunas = ['casa', 'dificuldade']

        df = pd.read_csv(caminho, sep=';')

        if not (set(colunas).issubset(df.columns)):
            print("O csv não possui as colunas esperadas.")
            return
        
        #definir uma lista com todos os Cavaleiros de Ouro
        cavaleirosDeOuro = [CavaleiroOuro(row['casa'], row['dificuldade']) for i, row in df.iterrows()]

        #print(cavaleirosDeOuro)
        return cavaleirosDeOuro

    #para quando for imprimir só um obejto
    def __str__(self):
        return f"Casa -> {self.casa} | Dificuldade -> {self.dificuldade}"

    #para quando for imprimir uma lista
    def __repr__(self):
        return f"\nCasa -> {self.casa} | Dificuldade -> {self.dificuldade}"