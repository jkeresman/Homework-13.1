import json
from encoder_decoder import player_encoder, player_decoder


def write_to_json(json_file, player_list):
    with open(json_file, "w") as file:
        json.dump(player_list, file, default=player_encoder, indent=4, sort_keys=True)


def read_from_json(json_file):
    with open(json_file, "r") as file:
        return json.load(file, object_hook=player_decoder)
