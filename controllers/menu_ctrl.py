import sys

from controllers import player_ctrl
from controllers.player_ctrl import PlayerController
from views import menu_view


class MenuController:

    def __init__(self):
        self.player_controller = PlayerController()
        # self.tournament_controller = TournamentController(self.player_controller.players)

    def home_menu_ctrl(self):
        menu = {
            "1": {
                "text": "Créer un nouveau tournoi",
                "action": self.tournament_menu
            },
            "2": {
                "text": "Ajouter un joueur",
                "action": self.add_player_menu
            },
            "3": {
                "text": "Modifier le classement d'un joueur",
                "action": self.update_ranking_menu
            },
            "4": {
                "text": "Générer un rapport",
                "action": self.report_generator_menu
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
        choice = menu_view.print_menu(menu, number_of_tries, "Votre choix: ", "Bienvenue !")
        if choice == "6":
            print("À bientôt !")
            menu[choice]["action"]()
        menu[choice]["action"]()

    def tournament_menu(self):
        menu = {
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
                "action": self.home_menu_ctrl
            },
        }
        number_of_tries = 0
        choice = menu_view.print_menu(menu, number_of_tries, "Votre choix: ", "Nouveau tournoi ?")
        menu[choice]["action"]()

    def add_player_menu(self):
        menu = {
            "1": {
                "text": "Créer un joueur",
                "action": player_ctrl.player_menu
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
                "action": self.home_menu_ctrl
            },
        }
        number_of_tries = 0
        choice = menu_view.print_menu(menu, number_of_tries, "Votre choix: ", "Un nouveau joueur ?")
        menu[choice]["action"]()

    def update_ranking_menu(self):
        menu = {
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
                "action": self.home_menu_ctrl
            },
        }
        number_of_tries = 0
        choice = menu_view.print_menu(menu, number_of_tries, "Votre choix: ", "Un nouveau classement ?")
        menu[choice]["action"]()

    def report_generator_menu(self):
        menu = {
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
                "action": self.home_menu_ctrl
            },
        }
        number_of_tries = 0
        choice = menu_view.print_menu(menu, number_of_tries, "Votre choix: ", "Un rapport ?")
        menu[choice]["action"]()
