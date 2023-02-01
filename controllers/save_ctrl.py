from tinydb import TinyDB
from datetime import datetime
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match


class SaveController:
    def __init__(self, players, tournaments):
        self.players = players
        self.tournaments = tournaments

    def save_players_data(self):
        db = TinyDB("chess_data.json", indent=4)
        players_table = db.table("players")
        players_table.truncate()
        if len(self.players) > 0:
            for player in self.players:
                players_table.insert({
                        'index': self.players.index(player),
                        'lastname': player.lastname,
                        'firstname': player.firstname,
                        'birth_date': player.birth_date,
                        'gender': player.gender,
                        'ranking': player.ranking
                })
        else:
            print("Aucun joueur existant à sauvegarder.")

    def save_tournaments_data(self):
        db = TinyDB("chess_data.json", indent=4)
        tournament_table = db.table("tournaments")
        tournament_table.truncate()
        if len(self.tournaments) > 0:
            for tournament in self.tournaments:
                players = [self.players.index(player) for player in tournament.players] \
                    if len(tournament.players) > 0 else []
                rounds = []
                if len(tournament.rounds) > 0:
                    for round_el in tournament.rounds:
                        matches = []
                        if len(round_el.matches) > 0:
                            for match in round_el.matches:
                                serialized_match = {
                                    'player_one_index': self.players.index(match.player_one),
                                    'player_two_index': self.players.index(match.player_two),
                                    'result': match.result
                                }
                                matches.append(serialized_match)
                        serialized_round = {
                            'name': round_el.name,
                            'start': round_el.start.strftime("%d-%m-%y %H:%M:%S"),
                            'end': round_el.end.strftime("%d-%m-%y %H:%M:%S"),
                            'matches': matches
                        }
                        rounds.append(serialized_round)
                players_score = {self.players.index(player): score
                                 for (player, score) in tournament.players_total_score.items()} \
                    if len(tournament.players_total_score) > 0 else {}
                tournament_table.insert({
                    'name': tournament.name,
                    'locality': tournament.locality,
                    'start': tournament.start,
                    'end': tournament.end,
                    'time_ctrl': tournament.time_ctrl,
                    'description': tournament.description,
                    'players': players,
                    'rounds': rounds,
                    'players_total_score': players_score,
                    'total_rounds': tournament.total_rounds
                })
        else:
            print("Aucun tournoi existant à sauvegarder")

    def save_data(self):
        self.save_players_data()
        self.save_tournaments_data()

    def loading_data(self):
        self.players.clear()
        self.tournaments.clear()
        db = TinyDB("chess_data.json", indent=4)
        serialized_players = db.table("players").all()
        serialized_tournaments = db.table("tournaments").all()
        if len(serialized_players) > 0:
            for player in serialized_players:
                loaded_player = Player(lastname=player["lastname"],
                                       firstname=player["firstname"],
                                       birth_date=player["birth_date"],
                                       gender=player["gender"],
                                       ranking=player["ranking"])
                self.players.append(loaded_player)
        if len(serialized_tournaments) > 0:
            for tournament in serialized_tournaments:
                players = [self.players[index] for index in tournament["players"]] \
                    if len(tournament["players"]) > 0 else []
                players_score = {self.players[int(index)]: score
                                 for (index, score) in tournament["players_total_score"].items()} \
                    if len(tournament["players_total_score"]) > 0 else {}
                loaded_tournament = Tournament(name=tournament["name"],
                                               locality=tournament["locality"],
                                               start=tournament["start"],
                                               end=tournament["end"],
                                               time_ctrl=tournament["time_ctrl"],
                                               description=tournament["description"],
                                               players=players,
                                               rounds=[],
                                               players_total_score=players_score,
                                               total_rounds=tournament["total_rounds"])
                if len(tournament["rounds"]) > 0:
                    for round_el in tournament["rounds"]:
                        loaded_round = Round(name=round_el["name"],
                                             start=datetime.strptime(round_el["start"], "%d-%m-%y %H:%M:%S"),
                                             end=datetime.strptime(round_el["end"], "%d-%m-%y %H:%M:%S"),
                                             matches=[])
                        if len(round_el["matches"]) > 0:
                            for match in round_el["matches"]:
                                loaded_match = Match(player_one=self.players[match["player_one_index"]],
                                                     player_two=self.players[match["player_two_index"]],
                                                     result=match["result"])
                                loaded_round.matches.append(loaded_match)
                        loaded_tournament.rounds.append(loaded_round)
                self.tournaments.append(loaded_tournament)
