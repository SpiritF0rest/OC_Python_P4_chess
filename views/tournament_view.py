from datetime import datetime
from settings import SEPARATOR


def add_tournament_view():
    tournament = {
        "name": "",
        "locality": "",
        "start": "",
        "end": "",
        "time_ctrl": "",
    }
    tournament_control = False
    print(SEPARATOR)
    while tournament_control is False:
        tournament_name = input("Nom: ")
        while not tournament_name.isalnum():
            tournament_name = input("Merci d'entrer un nom de tournoi valide. Nom: ")
        tournament["name"] = tournament_name
        tournament_locality = input("Lieu: ")
        while not tournament_locality.isalpha():
            tournament_locality = input("Merci d'entrer un lieu valide. Lieu: ")
        tournament["locality"] = tournament_locality
        start_date_control = False
        today = datetime.today().strftime("%d-%m-%Y")
        while start_date_control is False:
            tournament_start = input("Début du tournoi, ex: 02-05-2023: ")
            try:
                datetime.strptime(tournament_start, "%d-%m-%Y")
                if datetime.strptime(tournament_start, "%d-%m-%Y") > datetime.strptime(today, "%d-%m-%Y"):
                    tournament["start"] = tournament_start
                    start_date_control = True
                else:
                    print("La date de début de tournoi ne peut être antérieure à la date du jour.")
            except ValueError:
                print("Merci d'entrer une date valide, ex: 02-05-2023.")
        end_date_control = False
        while end_date_control is False:
            tournament_end = input("Fin du tournoi, ex: 03-05-2023: ")
            try:
                datetime.strptime(tournament_end, "%d-%m-%Y")
                if datetime.strptime(tournament_end, "%d-%m-%Y") >= datetime.strptime(tournament["start"], "%d-%m-%Y"):
                    tournament["end"] = tournament_end
                    end_date_control = True
                else:
                    print("La date de fin de tournoi ne peut être antérieure à la date de début du tournoi.")
            except ValueError:
                print("Merci d'entrer une date valide, ex: 02-05-2023.")
        tournament_time_ctrl = input("Contrôle du temps (bullet, blitz ou coup rapide): ")
        while tournament_time_ctrl not in ["bullet", "blitz", "coup rapide"]:
            tournament_time_ctrl = input("Merci d'entrer un contrôle de temps valide, bullet, blitz ou coup rapide: ")
        tournament["time_ctrl"] = tournament_time_ctrl
        tournament_total_rounds_update = input("Voulez-vous changer le nombre de tours, (4 par défaut)? (oui/non): ")
        while tournament_total_rounds_update not in ["oui", "non"]:
            tournament_total_rounds_update = input("Merci de répondre par oui ou non. Changement du nombre de tours ? ")
        if tournament_total_rounds_update == "oui":
            tournament_total_rounds = input("Nombre de tours: ")
            while not tournament_total_rounds.isdigit() and tournament_total_rounds < 3:
                tournament_total_rounds = input("Merci d'entrer un nombre de tour valide.")
            tournament["total_rounds"] = tournament_total_rounds
        else:
            print("Le nombre de tours est donc par défaut: 4.")
        tournament_control = True
    print(f"""Nouveau tournoi ajouté !
    {tournament["name"]} à {tournament["locality"]}:
    - Début: {tournament["start"]}
    - Fin: {tournament["end"]}
    - Contrôle de temps: {tournament["time_ctrl"]}
    - Nombre de tours: {tournament["total_rounds"] if hasattr(tournament, "total_rounds") else 4}""")
    return tournament

