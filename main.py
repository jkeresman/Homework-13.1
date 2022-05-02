from exceptions import NotPositiveNumberError
from functions import new_football_player, new_basketball_player
from json_functions import read_from_json, write_to_json


def main():

    players_file = "json_files/players.json"

    players = read_from_json(json_file=players_file)

    while True:

        print("1) Football player\n2) Basketball player\n3) Quit")
        answer = input("Your answer: ")

        if answer == "1":
            while True:
                try:
                    player = new_football_player()
                    break
                except NotPositiveNumberError as ex:
                    print(f"{ex} Please try again")
                except ValueError as ex:
                    print(f"{ex} Please try again")
            players.append(player)

        elif answer == "2":
            while True:
                try:
                    player = new_basketball_player()
                    break
                except NotPositiveNumberError as ex:
                    print(f"{ex} Please try again")
                except ValueError as ex:
                    print(f"{ex} Please try again")
            players.append(player)

        elif answer == "3":
            break

        else:
            print("Wrong input. Please try again!!")

    write_to_json(json_file=players_file, player_list=players)


if __name__ == "__main__":
    main()
