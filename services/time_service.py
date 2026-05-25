from models.time import Time
from models.jogador import Jogador

from repositories.time_repository import (
    TimeRepository
)

from utils.config import (
    MAX_JOGADORES_POR_TIME
)

from utils.exceptions import (
    TimeLotadoException
)


class TimeService:

    def __init__(self):

        self.__repository = TimeRepository()

    def criar_time(self, time: Time):

        self.__repository.salvar(time)

    def adicionar_jogador(
        self,
        time: Time,
        jogador: Jogador
    ):

        if (
            len(time.jogadores)
            >= MAX_JOGADORES_POR_TIME
        ):
            raise TimeLotadoException(
                "Time lotado."
            )

        time.adicionar_jogador(jogador)

        self.__repository.atualizar(time)

    def remover_jogador(
        self,
        time: Time,
        jogador: Jogador
    ):

        time.remover_jogador(jogador)

        self.__repository.atualizar(time)

    def listar_times(self):

        return self.__repository.listar()

    def buscar_time(self, id: int):

        return self.__repository.buscar_por_id(id)