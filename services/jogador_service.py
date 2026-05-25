from models.jogador import Jogador
from repositories.jogador_repository import (
    JogadorRepository
)

from utils.validators import Validators


class JogadorService:

    def __init__(self):

        self.__repository = JogadorRepository()

    def cadastrar_jogador(
        self,
        jogador: Jogador
    ):

        if not Validators.validar_email(
            jogador.email
        ):
            raise ValueError("Email inválido.")

        if not Validators.validar_nickname(
            jogador.nickname
        ):
            raise ValueError(
                "Nickname inválido."
            )

        self.__repository.salvar(jogador)

    def listar_jogadores(self):

        return self.__repository.listar()

    def buscar_jogador(self, id: int):

        return self.__repository.buscar_por_id(id)

    def atualizar_jogador(
        self,
        jogador: Jogador
    ):

        self.__repository.atualizar(jogador)

    def deletar_jogador(self, id: int):

        self.__repository.deletar(id)