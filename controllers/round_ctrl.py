from models.round import Round
from views.round_view import generate_players_pairs, enter_results
from views.tournament_view import choose_tournament_view
from datetime import datetime


class RoundController:
    def __init__(self, tournaments, rounds=None, current_matches=None):
        self.tournaments = tournaments
        self.rounds = [] if rounds is None else rounds
        self.current_matches = [] if current_matches is None else current_matches

    def start_round(self):
        tournaments = filter(lambda tournament: len(tournament.players) % 2 == 0 and len(tournament.players) >= 8,
                             self.tournaments)
        current_tournament = choose_tournament_view(list(tournaments))
        if current_tournament is not None:
            if len(current_tournament.rounds) < int(current_tournament.total_rounds):
                if len(current_tournament.rounds) > 0 and current_tournament.rounds[-1].end is None:
                    print("Un round est en cours, merci d'entrer les résultats avant d'en lancer un nouveau.")
                else:
                    new_round_name = "Round 1" if len(current_tournament.rounds) == 0 \
                        else f"Round {len(current_tournament.rounds)+1}"
                    new_round_start = datetime.now()
                    new_round = Round(new_round_name, new_round_start)
                    current_tournament.rounds.append(new_round)
                    generate_players_pairs(current_tournament.players,
                                           new_round,
                                           current_tournament.players_total_score)
            else:
                print("Tous les rounds de ce tournoi ont été joués.")

    def rounds_results(self):
        tournaments = filter(lambda tournament: len(tournament.rounds) > 0 and tournament.rounds[-1].end is None,
                             self.tournaments)
        selected_tournament = choose_tournament_view(list(tournaments))
        if selected_tournament is not None:
            select_round = selected_tournament.rounds[-1]
            enter_results(select_round, selected_tournament)
            select_round.end = datetime.now()
            if len(selected_tournament.rounds) == int(selected_tournament.total_rounds):
                for player in selected_tournament.players:
                    player.opponents.clear()
                print("Le tournoi est terminé. Voici le classement: ")
                sorted_players_by_score = dict(sorted(selected_tournament.players_total_score.items(),
                                                      key=lambda x: (x[1], x[0].ranking), reverse=True))
                for player, score in sorted_players_by_score.items():
                    print(f"- {player}: {score} points.")
