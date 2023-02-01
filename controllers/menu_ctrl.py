from controllers.player_ctrl import PlayerController
from controllers.tournament_ctrl import TournamentController
from controllers.round_ctrl import RoundController
from controllers.report_ctrl import ReportController
from controllers.save_ctrl import SaveController
from views import menu_view


class MenuController:
    run_control = True

    def __init__(self):
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController(players=self.player_controller.players)
        self.round_controller = RoundController(tournaments=self.tournament_controller.tournaments)
        self.report_controller = ReportController(tournaments=self.tournament_controller.tournaments,
                                                  players=self.player_controller.players)
        self.save_controller = SaveController(players=self.player_controller.players,
                                              tournaments=self.tournament_controller.tournaments)

    def stop_script(self):
        print("À bientôt !")
        self.run_control = False

    def home_menu_ctrl(self):
        while self.run_control is True:
            menu = {
                "1": {
                    "text": "Gestion tournois",
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
                    "text": "Chargement des données",
                    "action": self.save_controller.loading_data
                },
                "6": {
                    "text": "Sauvegarder",
                    "action": self.save_controller.save_data
                },
                "7": {
                    "text": "Quitter",
                    "action": self.stop_script
                },
            }
            choice = menu_view.print_menu(menu, "Votre choix: ", "Menu principal: ")
            menu[choice]["action"]()
        return 0

    def tournament_menu(self):
        menu = {
            "1": {
                "text": "Créer un nouveau tournoi",
                "action": self.tournament_controller.post_new_tournament
            },
            "2": {
                "text": "Sélectionner les joueurs",
                "action": self.tournament_controller.add_player_to_tournament
            },
            "3": {
                "text": "Gestion des rounds",
                "action": self.round_menu
            },
            "4": {
                "text": "Sauvegarder",
                "action": self.save_controller.save_data
            },
            "5": {
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
                "text": "Afficher les informations d'un joueur",
                "action": self.player_controller.get_player_data
            },
            "3": {
                "text": "Sauvegarder",
                "action": self.save_controller.save_data
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
                "action": self.player_controller.update_player_ranking
            },
            "2": {
                "text": "Afficher le classement d'un joueur",
                "action": self.player_controller.get_player_ranking
            },
            "3": {
                "text": "Sauvegarder",
                "action": self.save_controller.save_data
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
                "action": self.report_controller.all_players_report
            },
            "2": {
                "text": "Liste de tous les joueurs d'un tournoi précis",
                "action": self.report_controller.players_of_specific_tournament_report
            },
            "3": {
                "text": "Liste de tous les tournois",
                "action": self.report_controller.all_tournaments_report
            },
            "4": {
                "text": "Liste de tous les tours d'un tournoi",
                "action": self.report_controller.rounds_of_specific_tournament_report
            },
            "5": {
                "text": "Liste de tous les matchs d'un tournoi",
                "action": self.report_controller.matches_of_specific_tournament_report
            },
            "6": {
                "text": "Sauvegarder",
                "action": self.save_controller.save_data
            },
            "7": {
                "text": "Retour au menu principal",
                "action": self.home_menu_ctrl
            },
        }
        choice = menu_view.print_menu(menu, "Votre choix: ", "Un rapport ?")
        menu[choice]["action"]()

    def round_menu(self):
        menu = {
            "1": {
                "text": "Créer un round",
                "action": self.round_controller.start_round
            },
            "2": {
                "text": "Saisir les résultats d'un round",
                "action": self.round_controller.rounds_results
            },
            "3": {
                "text": "Sauvegarder",
                "action": self.save_controller.save_data
            },
            "4": {
                "text": "Retour au menu principal",
                "action": self.home_menu_ctrl
            },
        }
        choice = menu_view.print_menu(menu, "Votre choix: ", "Gestion des rounds")
        menu[choice]["action"]()
