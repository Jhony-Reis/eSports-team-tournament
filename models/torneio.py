from models.time import Time
from models.partida import Partida
from enums.tipo_torneio import TipoTorneio


class Torneio:

    def __init__(
        self,
        id: int,
        nome: str,
        tipo: TipoTorneio
    ):

        self.__id = id
        self.__nome = nome
        self.__tipo = tipo

        self.__times = []
        self.__partidas = []

        self.__campeao = None

    @property
    def nome(self):
        return self.__nome

    @property
    def campeao(self):
        return self.__campeao

    @property
    def times(self):
        return self.__times

    @property
    def partidas(self):
        return self.__partidas

    def adicionar_time(self, time: Time):
        self.__times.append(time)

    def adicionar_partida(self, partida: Partida):
        self.__partidas.append(partida)

    def definir_campeao(self, time: Time):
        self.__campeao = time

    def to_dict(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "tipo": self.__tipo.value,
            "times": [
                time.to_dict()
                for time in self.__times
            ],
            "partidas": [
                partida.to_dict()
                for partida in self.__partidas
            ],
            "campeao": (
                self.__campeao.nome
                if self.__campeao
                else None
            )
        }
    
    @property
    def id(self):
        return self.__id

    @staticmethod
    def from_dict(data):

        torneio = Torneio(
            data["id"],
            data["nome"],
            TipoTorneio(data["tipo"])
        )

        for time_data in data["times"]:
            torneio.adicionar_time(
                Time.from_dict(time_data)
            )

        for partida_data in data["partidas"]:
            torneio.adicionar_partida(
                Partida.from_dict(partida_data)
            )

        return torneio

    def __str__(self):
        return self.__nome