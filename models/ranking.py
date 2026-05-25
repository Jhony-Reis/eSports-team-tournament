from models.time import Time


class Ranking:

    def __init__(self, time: Time):

        self.__time = time

        self.__vitorias = 0
        self.__derrotas = 0
        self.__pontos = 0

    @property
    def time(self):
        return self.__time

    @property
    def pontos(self):
        return self.__pontos

    def adicionar_vitoria(self):

        self.__vitorias += 1
        self.__pontos += 3

    def adicionar_derrota(self):
        self.__derrotas += 1

    def to_dict(self):
        return {
            "time": self.__time.to_dict(),
            "vitorias": self.__vitorias,
            "derrotas": self.__derrotas,
            "pontos": self.__pontos
        }
    
    @property
    def id(self):
        return self.__id

    @staticmethod
    def from_dict(data):

        ranking = Ranking(
            Time.from_dict(data["time"])
        )

        ranking.__vitorias = data["vitorias"]
        ranking.__derrotas = data["derrotas"]
        ranking.__pontos = data["pontos"]

        return ranking

    def __str__(self):
        return f"{self.__time.nome} - {self.__pontos} pts"