from models.tournament import Tournament
from views import tournament_view


class TournamentController:

    def __init__(self, tournaments=None):
        self.tournaments = [] if tournaments is None else tournaments

    def post_new_tournament(self):
        tournament = tournament_view.add_tournament_view()
        new_tournament = Tournament(name=tournament["name"],
                                    locality=tournament["locality"],
                                    start=tournament["start"],
                                    end=tournament["end"],
                                    time_ctrl=tournament["time_ctrl"],
                                    )
        if hasattr(tournament, "total_rounds"):
            new_tournament.total_rounds = tournament["total_rounds"]
        self.tournaments.append(new_tournament)
