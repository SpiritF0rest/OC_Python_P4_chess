class Match:
    def __init__(self, player_one, player_two, result=None):
        self.player_one = player_one
        self.player_two = player_two
        self.result = [] if result is None else result
