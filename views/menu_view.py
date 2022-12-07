from settings import SEPARATOR


def print_menu(menu, message, intro):
    print(SEPARATOR)
    print(intro)
    print(f"Faites votre choix parmi les {len(menu)} options suivantes : ")
    [print(f"{index}: {value['text']}") for index, value in menu.items()]
    choice = input(message)
    number_of_tries = 0
    while choice not in menu:
        if number_of_tries == 10:
            number_of_tries -= 9
            print(SEPARATOR)
            print("Rappel: ")
            [print(f"{index}: {value['text']}") for index, value in menu.items()]
        choice = input("Merci de saisir une option valide. Votre choix: ")
        number_of_tries += 1
    return choice
