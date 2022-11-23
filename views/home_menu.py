def print_menu(menu, separator, number_of_tries):
    active_menu = menu.copy()
    print(separator)
    if number_of_tries == 0:
        print(f"{active_menu['0']['introduction']} Faites votre choix parmi les {len(active_menu)-1} options suivantes : ")
    elif number_of_tries == 10:
        print("Rappel: ")
    active_menu.pop("0")
    for index, value in active_menu.items():
        print(f"{index}: {value['text']}")


def get_choice(message):
    choice = input(message)
    return choice

