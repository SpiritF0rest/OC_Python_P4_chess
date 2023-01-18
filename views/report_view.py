from settings import SEPARATOR


def all_players_report_view(players):
    print(SEPARATOR)
    sort_type = input("""Quel type de tri souhaitez-vous ?
    1 - par ordre alphabétique
    2 - par classement""")
    while sort_type not in ["1", "2"]:
        sort_type = input("Merci de choisir une option valide entre '1' et '2'.")
    if sort_type == "1":
        pass
    else:
        pass


def all_tournaments_report_view(tournaments):
    print(SEPARATOR)
    print("Liste de tous les tournois")
    for tournament in tournaments:
        print(f"{'-' * 25}")
        print(f"""{tournaments.index(tournament)} - Tournoi: {tournament.name.capitalize()}
        Lieu: {tournament.locality}
        Date: {f'{tournament.start} au {tournament.end}' if tournament.start != tournament.end else tournament.start}
        Contrôle du temps: {tournament.time_ctrl}
        Nombre de tours: {tournament.total_rounds}
        Description: {tournament.description}""")


def rounds_of_specific_tournament_view(tournament):
    for element in tournament.rounds:
        print(f"{'-' * 25}")
        print(f"""- {element.name}
        Début: {element.start}
        Fin: {element.end if element.end is not None else 'en cours'}
        Nombre de matchs joués: {len(element.matches)}""")


def matches_of_specific_tournament_view(tournament):
    for element in tournament.rounds:
        if len(element.matches) > 0:
            print(f"{'-' * 25}")
            print(f"{element.name}:")
            for match in element.matches:
                print(f"""- Match {match.player_one} contre {match.player_two}
                Résultat: {match.result[0]} / {match.result[1]}""")
        else:
            print(f"Il n'y a pas encore de match dans le {element.name}")
