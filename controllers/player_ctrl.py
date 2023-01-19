from models.player import Player
from views import player_view


class PlayerController:

    def __init__(self, players=None):
        self.players = [] if players is None else players

    def post_new_player(self):
        player = player_view.add_player_view()
        new_player = Player(player["lastname"],
                            player["firstname"],
                            player["birth_date"],
                            player["gender"],
                            player["ranking"])
        self.players.append(new_player)

    def update_player_ranking(self):
        player_view.update_ranking(self.players, False)

    def get_player_informations(self):
        if len(self.players) > 0:
            player_view.get_player_informations_view(self.players, "les informations")
        else:
            print("Aucun joueur existant.")

    def get_player_ranking(self):
        if len(self.players) > 0:
            player_view.get_player_informations_view(self.players, "le classement")
        else:
            print("Aucun joueur existant.")
