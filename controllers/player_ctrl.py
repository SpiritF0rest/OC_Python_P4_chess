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
