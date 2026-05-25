from models.jogador import Jogador
from persistence.json_manager import JsonManager
from utils.config import JOGADORES_JSON


class JogadorRepository:

    def listar(self):

        dados = JsonManager.ler(JOGADORES_JSON)

        return [
            Jogador.from_dict(item)
            for item in dados
        ]

    def salvar(self, jogador: Jogador):

        jogadores = JsonManager.ler(JOGADORES_JSON)

        jogadores.append(jogador.to_dict())

        JsonManager.escrever(
            JOGADORES_JSON,
            jogadores
        )

    def buscar_por_id(self, id: int):

        jogadores = self.listar()

        for jogador in jogadores:

            if jogador.id == id:
                return jogador

        return None

    def atualizar(self, jogador_atualizado: Jogador):

        jogadores = JsonManager.ler(JOGADORES_JSON)

        for i, jogador in enumerate(jogadores):

            if jogador["id"] == jogador_atualizado.id:

                jogadores[i] = jogador_atualizado.to_dict()

                break

        JsonManager.escrever(
            JOGADORES_JSON,
            jogadores
        )

    def deletar(self, id: int):

        jogadores = JsonManager.ler(JOGADORES_JSON)

        jogadores = [
            jogador
            for jogador in jogadores
            if jogador["id"] != id
        ]

        JsonManager.escrever(
            JOGADORES_JSON,
            jogadores
        )