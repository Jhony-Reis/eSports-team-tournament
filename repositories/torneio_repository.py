from models.torneio import Torneio
from persistence.json_manager import JsonManager
from utils.config import TORNEIOS_JSON


class TorneioRepository:

    def listar(self):

        dados = JsonManager.ler(TORNEIOS_JSON)

        return [
            Torneio.from_dict(item)
            for item in dados
        ]

    def salvar(self, torneio: Torneio):

        torneios = JsonManager.ler(TORNEIOS_JSON)

        torneios.append(torneio.to_dict())

        JsonManager.escrever(
            TORNEIOS_JSON,
            torneios
        )

    def buscar_por_id(self, id: int):

        torneios = self.listar()

        for torneio in torneios:

            if torneio.id == id:
                return torneio

        return None

    def atualizar(self, torneio_atualizado: Torneio):

        torneios = JsonManager.ler(TORNEIOS_JSON)

        for i, torneio in enumerate(torneios):

            if torneio["id"] == torneio_atualizado.id:

                torneios[i] = (
                    torneio_atualizado.to_dict()
                )

                break

        JsonManager.escrever(
            TORNEIOS_JSON,
            torneios
        )

    def deletar(self, id: int):

        torneios = JsonManager.ler(TORNEIOS_JSON)

        torneios = [
            torneio
            for torneio in torneios
            if torneio["id"] != id
        ]

        JsonManager.escrever(
            TORNEIOS_JSON,
            torneios
        )