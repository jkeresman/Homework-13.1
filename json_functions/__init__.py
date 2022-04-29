import json


def write_to_json(json_file, player_list):
    with open(json_file, "w") as player_file:
        player_file.write(json.dumps(player_list))


def read_from_json(json_file):
    with open(json_file, "r") as player_file:
        player_list = json.loads(player_file.read())
    return player_list
