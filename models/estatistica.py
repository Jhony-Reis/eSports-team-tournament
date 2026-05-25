from models.jogador import Jogador


class Estatistica:

    def __init__(self, jogador: Jogador):

        self.__jogador = jogador

        self.__partidas_jogadas = 0
        self.__mvps = 0

    @property
    def jogador(self):
        return self.__jogador

    @property
    def partidas_jogadas(self):
        return self.__partidas_jogadas

    @property
    def mvps(self):
        return self.__mvps

    def adicionar_partida(self):
        self.__partidas_jogadas += 1

    def adicionar_mvp(self):
        self.__mvps += 1

    def calcular_kd(self):

        if self.__jogador.deaths == 0:
            return self.__jogador.kills

        return round(
            self.__jogador.kills /
            self.__jogador.deaths,
            2
        )

    def to_dict(self):
        return {
            "jogador": self.__jogador.to_dict(),
            "partidas_jogadas": self.__partidas_jogadas,
            "mvps": self.__mvps
        }
    
    @property
    def id(self):
        return self.__id

    @staticmethod
    def from_dict(data):

        estatistica = Estatistica(
            Jogador.from_dict(data["jogador"])
        )

        estatistica.__partidas_jogadas = data["partidas_jogadas"]
        estatistica.__mvps = data["mvps"]

        return estatistica

    def __str__(self):
        return (
            f"{self.__jogador.nickname} | "
            f"KD: {self.calcular_kd()}"
        )