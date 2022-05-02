from exceptions import NotPositiveNumberError
from player import Player, FootballPlayer, BasketballPlayer


def new_player() -> Player:
    first_name = input("Enter player's first name: ")
    last_name = input("Enter player's last name: ")
    height = float(input("Enter player's height: "))
    weight = float(input("Enter player's weight: "))

    return Player(first_name=first_name, last_name=last_name, height_cm=height, weight_kg=weight)


def new_football_player() -> FootballPlayer:
    while True:
        try:
            player = new_player()
            break
        except NotPositiveNumberError as ex:
            print(f"{ex} Please try again")
        except ValueError as ex:
            print(f"{ex} Please try again")

    goals = int(input("Enter number of goals: "))
    yellow_cards = int(input("Enter number of yellow cards: "))
    red_cards = int(input("Enter number of red cards: "))

    return FootballPlayer(player=player, goals=goals, yellow_cards=yellow_cards, red_cards=red_cards)


def new_basketball_player() -> BasketballPlayer:
    while True:
        try:
            player = new_player()
            break
        except NotPositiveNumberError as ex:
            print(f"{ex} Please try again")
        except ValueError as ex:
            print(f"{ex} Please try again")

    points = int(input("Enter number of points: "))
    rebounds = int(input("Enter number of rebounds: "))
    assists = int(input("Enter number of assists: "))

    return BasketballPlayer(player=player, points=points, rebounds=rebounds, assists=assists)
