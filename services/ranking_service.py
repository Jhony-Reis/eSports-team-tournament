from models.ranking import Ranking
from models.partida import Partida


class RankingService:

    def atualizar_ranking(
        self,
        ranking: Ranking,
        partida: Partida
    ):

        vencedor = partida.vencedor

        if vencedor is None:
            return

        if vencedor.nome == ranking.time.nome:

            ranking.adicionar_vitoria()

        else:

            ranking.adicionar_derrota()

    def ordenar_ranking(
        self,
        rankings: list
    ):

        return sorted(
            rankings,
            key=lambda r: r.pontos,
            reverse=True
        )