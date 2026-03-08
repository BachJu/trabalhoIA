#classe para definir os minutos em que cada terreno demora para ser percorrido
#nenhum = serve para criar um terreno vazio
#montanha = 200 min
#plano = 1 min
#rochoso = 5 min
#valores de INICIO e DESTINO servem apenas como flag, não possuem valor real
class Terrenos(int):
    NENHUM = -99
    MONTANHA = 200
    PLANO = 1
    ROCHOSO = 5
    INICIO = 0
    DESTINO = -1