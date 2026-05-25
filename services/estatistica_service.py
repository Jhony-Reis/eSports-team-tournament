from models.estatistica import (
    Estatistica
)


class EstatisticaService:

    def registrar_partida(
        self,
        estatistica: Estatistica
    ):

        estatistica.adicionar_partida()

    def registrar_mvp(
        self,
        estatistica: Estatistica
    ):

        estatistica.adicionar_mvp()

    def calcular_kd(
        self,
        estatistica: Estatistica
    ):

        return estatistica.calcular_kd()