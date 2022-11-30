class Tournament:
    def __init__(self, name, locality, start, end, time_ctrl, description, players=None, rounds=None, total_rounds=4):
        self.name = name
        self.locality = locality
        self.time_ctrl = time_ctrl
        self.description = description
        self.start = start
        self.end = end
        self.players = [] if players is None else players
        self.rounds = [] if rounds is None else rounds
        self.total_rounds = total_rounds
