from models.partida import Partida
from persistence.json_manager import JsonManager
from utils.config import PARTIDAS_JSON


class PartidaRepository:

    def listar(self):

        dados = JsonManager.ler(PARTIDAS_JSON)

        return [
            Partida.from_dict(item)
            for item in dados
        ]

    def salvar(self, partida: Partida):

        partidas = JsonManager.ler(PARTIDAS_JSON)

        partidas.append(partida.to_dict())

        JsonManager.escrever(
            PARTIDAS_JSON,
            partidas
        )

    def buscar_por_id(self, id: int):

        partidas = self.listar()

        for partida in partidas:

            if partida.id == id:
                return partida

        return None

    def atualizar(self, partida_atualizada: Partida):

        partidas = JsonManager.ler(PARTIDAS_JSON)

        for i, partida in enumerate(partidas):

            if partida["id"] == partida_atualizada.id:

                partidas[i] = partida_atualizada.to_dict()

                break

        JsonManager.escrever(
            PARTIDAS_JSON,
            partidas
        )

    def deletar(self, id: int):

        partidas = JsonManager.ler(PARTIDAS_JSON)

        partidas = [
            partida
            for partida in partidas
            if partida["id"] != id
        ]

        JsonManager.escrever(
            PARTIDAS_JSON,
            partidas
        )