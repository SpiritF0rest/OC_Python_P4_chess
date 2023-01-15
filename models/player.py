class Player:
    def __init__(self, lastname, firstname, birth_date, gender, ranking, opponents=None):
        self.lastname = lastname
        self.firstname = firstname
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.opponents = [] if opponents is None else opponents

    def __str__(self):
        return self.firstname + " " + self.lastname
