class Round:
    def __init__(self, name, start, end=None, matches=None):
        self.name = name
        self.start = start
        self.end = end
        self.matches = [] if matches is None else matches
