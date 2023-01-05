from datetime import datetime
from settings import SEPARATOR
from models.match import Match


def generate_players_pairs(players, current_round, players_total_score):
    #FIRST ROUND
    if current_round.name == "Round 1":
        first_round_players_list = sorted(players, key=lambda player: player.ranking)
        number_of_players = len(first_round_players_list)
        players_part_down = first_round_players_list[0:(number_of_players/2)+1]
        players_part_up = first_round_players_list[number_of_players/2:]
        for player in players_part_up:
            opponent = players_part_down[players_part_up.index(player)]
            player.opponents.append(opponent)
            opponent.opponents.append(player)
            new_match = Match()
            new_match.player_one = player
            new_match.player_two = opponent
            current_round.matches.append(new_match)
    #ANOTHER ROUNDS
    else:
        sort_players_dict = dict(sorted(players_total_score.items(), key=lambda x: x[1], reverse=True))
        round_players_list = list(sort_players_dict).copy()
        i = 0
        for player, score in list(sort_players_dict.items())[:-1]:
            if score == list(sort_players_dict.items())[i+1][1]:
                if player.ranking < list(sort_players_dict.items())[i+1][0].ranking:
                    round_players_list[i], round_players_list[i+1] = round_players_list[i+1], round_players_list[i]
            i += 1
        number_of_players = len(round_players_list)
        for player in round_players_list:
            j = 1
            control = False
            while control is False or j < number_of_players:
                opponent = round_players_list[round_players_list.index(player)+j]
                if player not in opponent.opponents:
                    player.opponents.append(opponent)
                    opponent.opponents.append(player)
                    new_match = Match()
                    new_match.player_one = player
                    new_match.player_two = opponent
                    current_round.matches.append(new_match)
                    round_players_list.remove(player)
                    round_players_list.remove(opponent)
                    control = True
                else:
                    j += 1
