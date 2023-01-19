from views import report_view
from views.tournament_view import choose_tournament_view


class ReportController:
    def __init__(self, tournaments, players):
        self.tournaments = tournaments
        self.players = players

    def all_players_report(self):
        if len(self.players) > 0:
            report_view.players_report_view(self.players)
        else:
            print("Aucun joueur existant.")

    def players_of_specific_tournament_report(self):
        selected_tournament = choose_tournament_view(self.tournaments)
        if selected_tournament is not None:
            if len(selected_tournament.players) > 0:
                report_view.players_report_view(selected_tournament.players)
            else:
                print("Il n'y a pas encore de joueurs dans ce tournoi.")

    def all_tournaments_report(self):
        if len(self.tournaments) > 0:
            report_view.all_tournaments_report_view(self.tournaments)
        else:
            print("Aucun tournoi existant.")

    def rounds_of_specific_tournament_report(self):
        selected_tournament = choose_tournament_view(self.tournaments)
        if selected_tournament is not None:
            if len(selected_tournament.rounds) > 0:
                report_view.rounds_of_specific_tournament_view(selected_tournament)
            else:
                print("Il n'a pas encore de round existant pour ce tournoi.")

    def matches_of_specific_tournament_report(self):
        selected_tournament = choose_tournament_view(self.tournaments)
        if selected_tournament is not None:
            if len(selected_tournament.rounds) > 0:
                report_view.matches_of_specific_tournament_view(selected_tournament)
            else:
                print("Il n'y a pas encore de round existant pour ce tournoi.")
