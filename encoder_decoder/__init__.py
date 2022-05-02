from player import Player, FootballPlayer, BasketballPlayer


def player_encoder(player: Player) -> dict:

    if isinstance(player, BasketballPlayer):
        return {
            'first_name': player.first_name,
            'last_name': player.last_name,
            'height_cm': player.height_cm,
            'weight_kg': player.weight_kg,
            'points': player.points,
            'rebounds': player.rebounds,
            'assists': player.assists,
            player.__class__.__name__: True,
        }

    elif isinstance(player, FootballPlayer):
        return {
            'first_name': player.first_name,
            'last_name': player.last_name,
            'height_cm': player.height_cm,
            'weight_kg': player.weight_kg,
            'goals': player.goals,
            'yellow_cards': player.yellow_cards,
            'red_cards': player.red_cards,
            player.__class__.__name__: True,
        }

    return player.__dict__


def player_decoder(player_dict: dict):

    player = Player(
        first_name=player_dict['first_name'],
        last_name=player_dict['last_name'],
        height_cm=player_dict['height_cm'],
        weight_kg=player_dict['weight_kg'],
    )

    if FootballPlayer.__name__ in player_dict:
        return FootballPlayer(
            player=player,
            goals=player_dict['goals'],
            yellow_cards=player_dict['yellow_cards'],
            red_cards=player_dict['red_cards'],
        )

    if BasketballPlayer.__name__ in player_dict:
        return BasketballPlayer(
            player=player,
            points=player_dict['points'],
            rebounds=player_dict['rebounds'],
            assists=player_dict['assists'],
        )
