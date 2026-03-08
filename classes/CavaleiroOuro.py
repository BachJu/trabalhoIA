class CavaleiroOuro:
    casa: str
    dificuldade: int

    def __init__(self, casa, dificuldade):
        self.casa = casa
        self.dificuldade = dificuldade

    #para quando for imprimir só um obejto
    def __str__(self):
        return f"Casa -> {self.casa} | Dificuldade -> {self.dificuldade}"

    #para quando for imprimir uma lista
    def __repr__(self):
        return f"\nCasa -> {self.casa} | Dificuldade -> {self.dificuldade}"