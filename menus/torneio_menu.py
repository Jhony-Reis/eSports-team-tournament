from services.torneio_service import (
    TorneioService
)

from repositories.time_repository import (
    TimeRepository
)

from models.torneio import Torneio

from enums.tipo_torneio import (
    TipoTorneio
)


def menu_torneio():

    service = TorneioService()

    time_repository = (
        TimeRepository()
    )

    while True:

        print("\n=== MENU TORNEIO ===")

        print("1 - Criar torneio")
        print("2 - Listar torneios")
        print("3 - Adicionar time")
        print("4 - Gerar confrontos")
        print("5 - Listar confrontos")
        print("0 - Voltar")

        opcao = input("\nEscolha: ")

        match opcao:

            case "1":

                try:

                    id = int(input("ID: "))
                    nome = input(
                        "Nome torneio: "
                    )

                    print("\nTipos disponíveis:")
                    print("1 - Pontos Corridos")
                    print("2 - Eliminação Simples")

                    opcao_tipo = input("Escolha o tipo: ")

                    if opcao_tipo == "1":
                        tipo = TipoTorneio.PONTOS_CORRIDOS

                    elif opcao_tipo == "2":
                        tipo = TipoTorneio.ELIMINACAO_SIMPLES

                    else:
                        raise ValueError("Tipo inválido.")

                    # tipo = TipoTorneio(
                    #     input("Tipo: ").upper()
                    # )

                    torneio = Torneio(
                        id,
                        nome,
                        tipo
                    )

                    service.criar_torneio(
                        torneio
                    )

                    print(
                        "\nTorneio criado."
                    )

                except Exception as e:
                    print(f"\nErro: {e}")

            case "2":

                torneios = (
                    service.listar_torneios()
                )

                if not torneios:
                    print("\nNenhum torneio.")

                for torneio in torneios:
                    print(torneio)

            case "3":

                try:

                    torneio_id = int(
                        input(
                            "ID torneio: "
                        )
                    )

                    time_id = int(
                        input(
                            "ID time: "
                        )
                    )

                    torneio = (
                        service.buscar_torneio(
                            torneio_id
                        )
                    )

                    time = (
                        time_repository
                        .buscar_por_id(
                            time_id
                        )
                    )

                    if not torneio:
                        print(
                            "\nTorneio não encontrado."
                        )
                        continue

                    if not time:
                        print(
                            "\nTime não encontrado."
                        )
                        continue

                    service.adicionar_time(
                        torneio,
                        time
                    )

                    print(
                        "\nTime adicionado."
                    )

                except Exception as e:
                    print(f"\nErro: {e}")

            case "4":

                try:

                    torneio_id = int(
                        input(
                            "ID torneio: "
                        )
                    )

                    torneio = (
                        service.buscar_torneio(
                            torneio_id
                        )
                    )

                    if not torneio:
                        print(
                            "\nTorneio não encontrado."
                        )
                        continue

                    service.gerar_confrontos(
                        torneio
                    )

                    print(
                        "\nConfrontos gerados."
                    )

                except Exception as e:
                    print(f"\nErro: {e}")

            case "5":

                try:

                    torneio_id = int(
                        input("ID torneio: ")
                    )

                    torneio = (
                        service.buscar_torneio(
                            torneio_id
                        )
                    )

                    if not torneio:
                        print(
                            "\nTorneio não encontrado."
                        )
                        continue

                    if not torneio.partidas:
                        print(
                            "\nNenhum confronto gerado."
                        )
                        continue

                    print("\n=== CONFRONTOS ===")

                    for partida in torneio.partidas:

                        for partida in torneio.partidas:
                            print(partida)

                except Exception as e:
                    print(f"\nErro: {e}")

            case "0":
                break

            case _:
                print("\nOpção inválida.")