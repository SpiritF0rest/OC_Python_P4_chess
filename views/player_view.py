from datetime import datetime
from settings import SEPARATOR


def add_player_view():
    player = {
        "lastname": "",
        "firstname": "",
        "birth_date": "",
        "gender": "",
        "ranking": "",
    }
    player_control = False
    print(SEPARATOR)
    while player_control is not True:
        player_lastname = input("Nom: ")
        while not player_lastname.isalpha():
            player_lastname = input("Merci d'entrer un nom valide. Nom: ")
        player["lastname"] = player_lastname
        player_firstname = input("Prénom: ")
        while not player_firstname.isalpha():
            player_firstname = input("Merci d'entrer un prénom valide. Prénom: ")
        player["firstname"] = player_firstname
        date_control = False
        today = datetime.today().strftime("%d-%m-%Y")
        while date_control is not True:
            player_birth_date = input("Date de naissance, ex: 14-08-1987: ")
            try:
                datetime.strptime(player_birth_date, "%d-%m-%Y")
                if datetime.strptime(player_birth_date, "%d-%m-%Y") < datetime.strptime(today, "%d-%m-%Y"):
                    player["birth_date"] = player_birth_date
                    date_control = True
                else:
                    print("La date de naissance ne peut être postérieure à aujourd'hui.")
            except ValueError:
                print("Merci d'entrer une date d'anniversaire valide, ex: 14-08-1987")
        player_gender = input("Sexe (homme, femme ou autre): ")
        while player_gender not in ["homme", "femme", "autre"]:
            player_gender = input("Merci d'entrer une des valeurs (homme, femme ou autre). Sexe: ")
        player["gender"] = player_gender
        ranking_control = False
        while ranking_control is not True:
            player_ranking = input("Classement: ")
            try:
                rank = int(player_ranking)
                if rank >= 0:
                    player["ranking"] = int(player_ranking)
                    ranking_control = True
                else:
                    print('Le classement doit être un nombre entier positif.')
            except ValueError:
                print("Merci d'entrer un nombre entier positif.")
        player_control = True
    print(f"""Nouveau joueur créé !
    {player["lastname"]} {player["firstname"]}:
    - né le: {player["birth_date"]}
    - genre: {player["gender"]}
    - classement actuel: {player["ranking"]}""")
    return player
