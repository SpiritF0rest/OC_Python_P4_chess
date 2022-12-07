from controllers.player_ctrl import PlayerController
from controllers.tournament_ctrl import TournamentController
from views import menu_view


class MenuController:
    run_control = True

    def __init__(self):
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController(self.player_controller.players)

    def stop_script(self):
        print("À bientôt !")
        self.run_control = False

    def home_menu_ctrl(self):
        while self.run_control is True:
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
                    "action": self.stop_script
                },
            }
            choice = menu_view.print_menu(menu, "Votre choix: ", "Menu principal: ")
            menu[choice]["action"]()

    def tournament_menu(self):
        menu = {
            "1": {
                "text": "Créer un nouveau tournoi",
                "action": self.tournament_controller.post_new_tournament
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
        choice = menu_view.print_menu(menu, "Votre choix: ", "Nouveau tournoi ?")
        menu[choice]["action"]()

    def add_player_menu(self):
        menu = {
            "1": {
                "text": "Créer un joueur",
                "action": self.player_controller.post_new_player
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
        choice = menu_view.print_menu(menu, "Votre choix: ", "Un nouveau joueur ?")
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
        choice = menu_view.print_menu(menu, "Votre choix: ", "Un nouveau classement ?")
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
        choice = menu_view.print_menu(menu, "Votre choix: ", "Un rapport ?")
        menu[choice]["action"]()
