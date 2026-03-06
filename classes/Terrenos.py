#classe para definir os minutos em que cada terreno demora para ser percorrido
#nenhum = serve para criar um terreno vazio
#montanha = 200 min
#plano = 1 min
#rochoso = 5 min
class Terrenos(int):
    NENHUM = 0
    MONTANHA = 200
    PLANO = 1
    ROCHOSO = 5
    INICIO = -10
    DESTINO = -15