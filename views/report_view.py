from textwrap import dedent
from settings import SEPARATOR


def players_report_view(players):
    print(SEPARATOR)
    sort_type = input(dedent("""\
    Quel type de tri souhaitez-vous ?
      1 - par ordre alphabétique
      2 - par classement
    Choix: """))
    while sort_type not in ["1", "2"]:
        sort_type = input("Merci de choisir une option valide entre '1' et '2'.")
    if sort_type == "1":
        # sorting by players alphabetical
        player_sorted_list = sorted(players, key=lambda player_obj: (player_obj.lastname, player_obj.firstname))
    else:
        # sorting by players ranking then alphabetical
        player_sorted_list = sorted(players,
                                    key=lambda player_obj: (player_obj.ranking, player_obj.lastname),
                                    reverse=True)
    for player in player_sorted_list:
        print(f"{'-' * 25}")
        print(dedent(f"""\
        \033[1m{player} \033[0m
          Né(e) le: {player.birth_date}
          Sexe: {player.gender}
          Classement: {player.ranking}"""))


def all_tournaments_report_view(tournaments):
    print(SEPARATOR)
    print("Liste de tous les tournois")
    for tournament in tournaments:
        print(f"{'-' * 25}")
        print(dedent(f"""\
        \033[1m{tournaments.index(tournament)+1}-Tournoi: {tournament.name.capitalize()} \033[0m
          Lieu: {tournament.locality}
          Date: {f'{tournament.start} au {tournament.end}' if tournament.start != tournament.end else tournament.start}
          Contrôle du temps: {tournament.time_ctrl}
          Nombre de tours: {tournament.total_rounds}
          Description: {tournament.description}"""))


def rounds_of_specific_tournament_view(tournament):
    for element in tournament.rounds:
        print(f"{'-' * 25}")
        print(dedent(f"""\
        \033[1m- {element.name} \033[0m
          Début: {element.start}
          Fin: {element.end if element.end is not None else 'en cours'}
          Nombre de matchs joués: {len(element.matches)}"""))


def matches_of_specific_tournament_view(tournament):
    for element in tournament.rounds:
        if len(element.matches) > 0:
            print(f"{'-' * 25}")
            print(f"\033[1m{element.name}: \033[0m")
            for match in element.matches:
                print(dedent(f"""\
                - Match {match.player_one} contre {match.player_two}
                  Résultat: {match.result[0]} / {match.result[1]}"""))
        else:
            print(f"Il n'y a pas encore de match dans le {element.name}")
