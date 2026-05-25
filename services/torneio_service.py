from models.torneio import Torneio
from models.partida import Partida
from models.time import Time

from repositories.torneio_repository import (
    TorneioRepository
)


class TorneioService:

    def __init__(self):

        self.__repository = (
            TorneioRepository()
        )

    def criar_torneio(
        self,
        torneio: Torneio
    ):

        self.__repository.salvar(
            torneio
        )

    def adicionar_time(
        self,
        torneio: Torneio,
        time: Time
    ):

        torneio.adicionar_time(time)

        self.__repository.atualizar(
            torneio
        )

    def gerar_confrontos(
        self,
        torneio: Torneio
    ):

        times = torneio.times

        partidas = []

        id_partida = 1

        for i in range(len(times)):

            for j in range(i + 1, len(times)):

                partida = Partida(
                    id_partida,
                    times[i],
                    times[j]
                )

                partidas.append(partida)

                id_partida += 1

        for partida in partidas:

            torneio.adicionar_partida(
                partida
            )

        self.__repository.atualizar(
            torneio
        )

    def definir_campeao(
        self,
        torneio: Torneio,
        time: Time
    ):

        torneio.definir_campeao(time)

        self.__repository.atualizar(
            torneio
        )

    def listar_torneios(self):

        return self.__repository.listar()

    def buscar_torneio(self, id: int):

        return self.__repository.buscar_por_id(id)