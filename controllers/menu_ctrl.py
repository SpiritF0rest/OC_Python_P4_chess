import sys
from views import home_menu


def home_menu_ctrl(separator):
    menu = {
        "0": {
            "introduction": "Bienvenue !"
        },
        "1": {
            "text": "Créer un nouveau tournoi",
            "action": tournament_menu
        },
        "2": {
            "text": "Ajouter un joueur",
            "action": add_player_menu
        },
        "3": {
            "text": "Modifier le classement d'un joueur",
            "action": update_ranking_menu
        },
        "4": {
            "text": "Générer un rapport",
            "action": report_generator_menu
        },
        "5": {
            "text": "Sauvegarder",
            "action": None
        },
        "6": {
            "text": "Quitter",
            "action": sys.exit
        },
    }
    number_of_tries = 0
    home_menu.print_menu(menu, separator, number_of_tries)
    choice = home_menu.get_choice("Votre choix: ")
    while choice not in menu or choice == "0":
        if number_of_tries == 10:
            home_menu.print_menu(menu, separator, number_of_tries)
            number_of_tries = 1
        choice = home_menu.get_choice("Merci de saisir une option valide. Votre choix: ")
        number_of_tries += 1
    if choice == "6":
        print("À bientôt !")
        menu[choice]["action"]()
    menu[choice]["action"](separator)


def tournament_menu(separator):
    menu = {
        "0": {
            "introduction": "Nouveau tournoi ?"
        },
        "1": {
            "text": "Créer un nouveau tournoi",
            "action": None
        },
        "2": {
            "text": "Sélectionner les joueurs",
            "action": None
        },
        "3": {
            "text": "Lancer le tournoi",
            "action": None
        },
        "4": {
            "text": "Terminer le tournoi",
            "action": None
        },
        "5": {
            "text": "Sauvegarder",
            "action": None
        },
        "6": {
            "text": "Retour au menu principal",
            "action": home_menu_ctrl
        },
    }
    number_of_tries = 0
    home_menu.print_menu(menu, separator, number_of_tries)
    choice = home_menu.get_choice("Votre choix: ")
    while choice not in menu or choice == "0":
        if number_of_tries == 10:
            home_menu.print_menu(menu, separator, number_of_tries)
            number_of_tries = 1
        choice = home_menu.get_choice("Merci de saisir une option valide. Votre choix: ")
        number_of_tries += 1
    menu[choice]["action"](separator)


def add_player_menu(separator):
    menu = {
        "0": {
            "introduction": "Un nouveau joueur ?"
        },
        "1": {
            "text": "Créer un joueur",
            "action": None
        },
        "2": {
            "text": "Afficher un joueur",
            "action": None
        },
        "3": {
            "text": "Sauvegarder",
            "action": None
        },
        "4": {
            "text": "Retour au menu principal",
            "action": home_menu_ctrl
        },
    }
    number_of_tries = 0
    home_menu.print_menu(menu, separator, number_of_tries)
    choice = home_menu.get_choice("Votre choix: ")
    while choice not in menu or choice == "0":
        if number_of_tries == 10:
            home_menu.print_menu(menu, separator, number_of_tries)
            number_of_tries = 1
        choice = home_menu.get_choice("Merci de saisir une option valide. Votre choix: ")
        number_of_tries += 1
    menu[choice]["action"](separator)


def update_ranking_menu(separator):
    menu = {
        "0": {
            "introduction": "Un nouveau classement ?"
        },
        "1": {
            "text": "Modifier le classement d'un joueur",
            "action": None
        },
        "2": {
            "text": "Afficher le classement d'un joueur",
            "action": None
        },
        "3": {
            "text": "Sauvegarder",
            "action": None
        },
        "4": {
            "text": "Retour au menu principal",
            "action": home_menu_ctrl
        },
    }
    number_of_tries = 0
    home_menu.print_menu(menu, separator, number_of_tries)
    choice = home_menu.get_choice("Votre choix: ")
    while choice not in menu or choice == "0":
        if number_of_tries == 10:
            home_menu.print_menu(menu, separator, number_of_tries)
            number_of_tries = 1
        choice = home_menu.get_choice("Merci de saisir une option valide. Votre choix: ")
        number_of_tries += 1
    menu[choice]["action"](separator)


def report_generator_menu(separator):
    menu = {
        "0": {
            "introduction": "Un rapport ?"
        },
        "1": {
            "text": "Liste de tous les joueurs",
            "action": None
        },
        "2": {
            "text": "Liste de tous les joueurs d'un tournoi précis",
            "action": None
        },
        "3": {
            "text": "Liste de tous les tournois",
            "action": None
        },
        "4": {
            "text": "Liste de tous les tours d'un tournoi",
            "action": None
        },
        "5": {
            "text": "Liste de tous les matchs d'un tournoi",
            "action": None
        },
        "6": {
            "text": "Sauvegarder",
            "action": None
        },
        "7": {
            "text": "Retour au menu principal",
            "action": home_menu_ctrl
        },
    }
    number_of_tries = 0
    home_menu.print_menu(menu, separator, number_of_tries)
    choice = home_menu.get_choice("Votre choix: ")
    while choice not in menu or choice == "0":
        if number_of_tries == 10:
            home_menu.print_menu(menu, separator, number_of_tries)
            number_of_tries = 1
        choice = home_menu.get_choice("Merci de saisir une option valide. Votre choix: ")
        number_of_tries += 1
    menu[choice]["action"](separator)
