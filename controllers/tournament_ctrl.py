from models.tournament import Tournament
from controllers.round_ctrl import RoundController
from views import tournament_view


class TournamentController:

    def __init__(self, players, tournaments=None):
        self.players = players
        self.tournaments = [] if tournaments is None else tournaments

    def post_new_tournament(self):
        tournament = tournament_view.add_tournament_view()
        new_tournament = Tournament(name=tournament["name"],
                                    locality=tournament["locality"],
                                    start=tournament["start"],
                                    end=tournament["end"],
                                    time_ctrl=tournament["time_ctrl"],
                                    )
        if "total_rounds" in tournament:
            new_tournament.total_rounds = tournament["total_rounds"]
        self.tournaments.append(new_tournament)

    def add_player_to_tournament(self):
        select_tournament = tournament_view.choose_tournament_view(self.tournaments)
        select_player = tournament_view.add_player_to_tournament_view(select_tournament, self.players)
        if select_player is not None:
            select_tournament.players.append(select_player)
            print(select_tournament)

    def run_tournament(self):
        #ici on passe la liste des joueurs à round_ctrl avec le nombre de tours et index du tournoi

        pass
