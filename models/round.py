class Round:
    def __init__(self, name, start, end, matches=None):
        self.name = name
        self.start = start
        self.end = end
        self.matches = [] if matches is None else matches
