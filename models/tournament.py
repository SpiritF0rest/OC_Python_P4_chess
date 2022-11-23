class Tournament:
    def __int__(self, name, locality, start, end, rounds, players, time_ctrl, description, number_of_rounds=4):
        self.name = name
        self.locality = locality
        self.time_ctrl = time_ctrl
        self.description = description
        self.start = start
        self.end = end
        self.rounds = rounds
        self.players = players
        self.number_of_rounds = number_of_rounds
