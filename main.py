from menus.jogador_menu import menu_jogador
from menus.time_menu import menu_time
from menus.partida_menu import menu_partida
from menus.torneio_menu import menu_torneio


def main():

    while True:

        print("\n=== SISTEMA DE TORNEIO E-SPORTS ===")

        print("1 - Jogadores")
        print("2 - Times")
        print("3 - Partidas")
        print("4 - Torneios")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        match opcao:

            case "1":
                menu_jogador()

            case "2":
                menu_time()

            case "3":
                menu_partida()

            case "4":
                menu_torneio()

            case "0":

                print("\nSistema encerrado.")
                break

            case _:
                print("\nOpção inválida.")


if __name__ == "__main__":
    main()