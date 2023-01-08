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
        tournaments = filter(lambda players: tournament.players % 2 == 0 and tournament.players >= 8, self.tournaments)
        tournament = choose_tournament_view(list(tournaments))
        if tournament is not None:
            new_round_name = "Round 1" if len(tournament.rounds) == 0 else f"Round {len(tournament.rounds)+1}"
            new_round_start = datetime.now()  # tz à préciser
            new_round = Round(new_round_name, new_round_start)
            generate_players_pairs(tournament.players, new_round, tournament.players_total_score)

    def rounds_results(self):
        tournaments = filter(lambda rounds: len(tournament.rounds) > 0 and tournament.rounds[-1].end is None, self.tournaments)
        tournament = choose_tournament_view(list(tournaments))
        if tournament is not None:
            select_round = tournament.rounds[-1]
            enter_results(select_round, tournament)
            select_round.end = datetime.now()  # tz à préciser
