from exceptions import NotPositiveNumberError
from functions import new_football_player, new_basketball_player
from json_functions import read_from_json, write_to_json


def main():

    football_players_file = "json_files/football_players.json"
    basketball_players_file = "json_files/basketball_players.json"

    football_players = read_from_json(json_file=football_players_file)
    basketball_players = read_from_json(json_file=basketball_players_file)

    print("Basketball players: ")
    for b_player in basketball_players:
        print(b_player)

    print("Football players: ")
    for f_player in football_players:
        print(f_player)

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
            football_players.append(player.__dict__)

        elif answer == "2":
            while True:
                try:
                    player = new_basketball_player()
                    break
                except NotPositiveNumberError as ex:
                    print(f"{ex} Please try again")
                except ValueError as ex:
                    print(f"{ex} Please try again")
            basketball_players.append(player.__dict__)

        elif answer == "3":
            break

        else:
            print("Wrong input. Please try again!!")

    write_to_json(json_file=football_players_file,player_list=football_players)
    write_to_json(json_file=basketball_players_file,player_list=basketball_players)


if __name__ == "__main__":
    main()
