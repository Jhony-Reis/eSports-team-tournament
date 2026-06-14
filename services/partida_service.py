from models.partida import Partida

from repositories.partida_repository import (
    PartidaRepository
)

from utils.exceptions import (
    PartidaFinalizadaException
)

from enums.status_partida import (
    StatusPartida
)


class PartidaService:

    def __init__(self):

        self.__repository = (
            PartidaRepository()
        )

    def iniciar_partida(
        self,
        partida: Partida
    ):

        if (
            partida.status
            == StatusPartida.FINALIZADA
        ):
            raise PartidaFinalizadaException(
                "Partida já finalizada."
            )

        partida.iniciar_partida()

        self.__repository.atualizar(
            partida
        )
    def criar_partida(self, partida: Partida):
        self.__repository.salvar(
            partida
        )

    def finalizar_partida(
        self,
        partida: Partida,
        placar_a: int,
        placar_b: int
    ):

        partida.finalizar_partida(
            placar_a,
            placar_b
        )

        self.__repository.atualizar(
            partida
        )

    def listar_partidas(self):

        return self.__repository.listar()

    def buscar_partida(self, id: int):

        return self.__repository.buscar_por_id(id)