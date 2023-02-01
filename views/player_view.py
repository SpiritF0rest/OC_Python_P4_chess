from datetime import datetime
from textwrap import dedent
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
        player_gender = input("Sexe ('H' = homme, 'F' = femme ou 'autre'): ")
        while player_gender not in ["H", "F", "autre"]:
            player_gender = input("Merci d'entrer une de ces valeurs ('H', 'F' ou 'autre'). Sexe: ")
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
    {player["firstname"].capitalize()} {player["lastname"].capitalize()}:
    - né le: {player["birth_date"]}
    - genre: {player["gender"]}
    - classement actuel: {player["ranking"]}""")
    return player


def update_ranking(players_list, is_end_tournament):
    print(SEPARATOR)
    if len(players_list) == 0:
        print("Aucun joueur. Merci de créer des joueurs avant de pouvoir modifier un classement.")
        return None
    if is_end_tournament is False:
        task_control = False
        while task_control is False:
            players_dict = {str(index): el for (index, el) in enumerate(players_list, start=1)}
            print(f"Sélectionnez le joueur :")
            [print(f"{index}: {el}") for (index, el) in players_dict.items()]
            select_player = input("choix: ")
            while select_player not in players_dict:
                select_player = input("Merci de saisir une option valide. Joueur n°: ")
            player = players_dict[select_player]
            print(f"Le classement actuel de {player} est: {player.ranking}")
            ranking_control = False
            while ranking_control is not True:
                new_rank = input("Nouveau classement: ")
                try:
                    rank = int(new_rank)
                    if rank >= 0:
                        player.ranking = int(new_rank)
                        ranking_control = True
                    else:
                        print('Le classement doit être un nombre entier positif.')
                except ValueError:
                    print("Merci d'entrer un nombre entier positif.")
            print(f"Le nouveau classement de {player} est: {player.ranking}")
            ask_end_task = input("Souhaitez-vous modifier un autre classement de joueur ? ('O' = oui, 'N' = non): ")
            while ask_end_task not in ["O", "N"]:
                ask_end_task = input("Merci de saisir une option valide ('O' = oui, 'N' = non). Choix: ")
            if ask_end_task == "N":
                task_control = True
    else:
        for player in players_list:
            print(f"Le classement actuel de {player} est: {player.ranking}")
            ranking_control = False
            while ranking_control is not True:
                new_rank = input("Nouveau classement: ")
                try:
                    rank = int(new_rank)
                    if rank >= 0:
                        player.ranking = int(new_rank)
                        ranking_control = True
                    else:
                        print('Le classement doit être un nombre entier positif.')
                except ValueError:
                    print("Merci d'entrer un nombre entier positif.")
            print(f"Le nouveau classement de {player} est: {player.ranking}")


def get_player_informations_view(players, type_of_information):
    print(SEPARATOR)
    player_sorted_list = sorted(players, key=lambda player_obj: (player_obj.lastname, player_obj.firstname))
    player_sorted_dict = {str(index): el for (index, el) in enumerate(player_sorted_list, start=1)}
    print(f"De quel joueur souhaitez vous {type_of_information} ?")
    [print(f"{index}: {el}") for (index, el) in player_sorted_dict.items()]
    selected_player = input("Choix: ")
    while selected_player not in player_sorted_dict:
        selected_player = input("Merci de saisir une option valide. Joueur n°: ")
    if type_of_information == "les informations":
        print(dedent(f"""\
        - {player_sorted_dict[selected_player]}
          Né(e) le: {player_sorted_dict[selected_player].birth_date}
          Sexe: {player_sorted_dict[selected_player].gender}
          Classement: {player_sorted_dict[selected_player].ranking}"""))
    elif type_of_information == "le classement":
        print(dedent(f"""\
        - {player_sorted_dict[selected_player]}
          Classement: {player_sorted_dict[selected_player].ranking}"""))
