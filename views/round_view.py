from settings import SEPARATOR
from models.match import Match


def generate_players_pairs(players, current_round, players_total_score):
    print(SEPARATOR)
    print(current_round.name.upper())
    if current_round.name == "Round 1":
        first_round_players_list = sorted(players, key=lambda player: player.ranking, reverse=True)
        number_of_players = len(first_round_players_list)
        players_part_up = first_round_players_list[0:int((number_of_players/2))]
        players_part_down = first_round_players_list[int((number_of_players/2)):]
        for player in players_part_up:
            opponent = players_part_down[players_part_up.index(player)]
            player.opponents.append(opponent)
            opponent.opponents.append(player)
            new_match = Match(player, opponent)
            current_round.matches.append(new_match)
            print(f"Match: {player} VS {opponent}")
    else:
        "ANOTHER ROUNDS"
        sort_players_dict = dict(sorted(players_total_score.items(), key=lambda x: (x[1], x[0].ranking), reverse=True))
        round_players_list = list(sort_players_dict).copy()
        assign_all_players_control = False
        while assign_all_players_control is False:
            i = 1
            control = False
            while control is False:
                player = round_players_list[0]
                opponent = round_players_list[round_players_list.index(player)+i]
                if player not in opponent.opponents:
                    player.opponents.append(opponent)
                    opponent.opponents.append(player)
                    new_match = Match(player, opponent)
                    current_round.matches.append(new_match)
                    round_players_list.remove(player)
                    round_players_list.remove(opponent)
                    print(f"Match: {player} VS {opponent}")
                    control = True
                else:
                    i += 1
                    if i >= len(round_players_list):
                        opponent = round_players_list[1]
                        new_match = Match(player, opponent)
                        current_round.matches.append(new_match)
                        round_players_list.remove(player)
                        round_players_list.remove(opponent)
                        print(f"Match: {player} VS {opponent}")
                        control = True
                if len(round_players_list) == 0:
                    assign_all_players_control = True


def enter_results(select_round, tournament):
    possible_scores = ["0", "0.5", "1"]
    for match in select_round.matches:
        print(SEPARATOR)
        print(f"Résultat match {match.player_one} VS {match.player_two}")
        score_control = False
        score_player_one = ""
        score_player_two = ""
        while score_control is False:
            score_player_one = input(f"Score {match.player_one}: ")
            while score_player_one not in possible_scores:
                score_player_one = input(f"Merci d'entrer un score valide (0, 1 ou 0.5). Score {match.player_one}: ")
            score_player_two = input(f"Score {match.player_two}: ")
            while score_player_two not in possible_scores:
                score_player_two = input(f"Merci d'entrer un score valide (0, 1 ou 0.5). Score {match.player_two}: ")
            if (float(score_player_one)+float(score_player_two)) == 1:
                score_control = True
            else:
                print("La somme des scores des deux joueurs doit être égale à 1.")
        match.result.append(float(score_player_one))
        match.result.append(float(score_player_two))
        if select_round.name == "Round 1":
            tournament.players_total_score[match.player_one] = float(score_player_one)
            tournament.players_total_score[match.player_two] = float(score_player_two)
        else:
            tournament.players_total_score[match.player_one] += float(score_player_one)
            tournament.players_total_score[match.player_two] += float(score_player_two)
