from Color import Color
import os
import time

class Console:

    def __init__(self) -> None:
        pass

    def say_preparation():
        print('''₱ⱤɆ₱₳Ɽ₳₮łØ₦   ĐɄ   ₵Ø₥฿₳₮...''')

    def ask_name():
        var = input("Entrez le nom du personnage : ")
        return var

    def ask_friendly():
        print("\n" + Color.GREEN + "-1- Allié\n" + Color.RED + "-2- Ennemi\n" + Color.RESET)
        var = input("Indiquez la lettre correspondante : ")
        return var

    def ask_hp(name):
        var = int(input(f"\nEntrez ses points de vies: "))
        return var

    def say_fight_starting():
        print('''ĐɆ฿Ʉ₮ ĐɄ ₵Ø₥฿₳₮...''')

    def say_round(name, friendly):
        if friendly == True:
            print(f"C'est au tour de " + Color.GREEN + name + Color.RESET + " de jouer, que fait-il ?\n")
        else:
            print(f"C'est au tour de " + Color.RED + name + Color.RESET + " de jouer, que fait-il ?\n")

    def ask_action():
        print("-1- Attaque\n-2- Autre chose\n")
        var = int(input("Indiquez la lettre correspondante : "))
        return var

    def say_target():
        print("\nQui reçoit des dégats ?\n")

    def say_character(order, name, hp, friendly):
        if friendly == True:
            print(Color.GREEN + f"-{order}-  {name}  {hp}PV" + Color.RESET)
        else :
            print(Color.RED + f"-{order}-  {name}  {hp}PV" + Color.RESET)

    def ask_target():
        print("-0-  Personne\n")
        var = int(input("Choissisez un nombre ci-dessus : "))
        return var

    def ask_degats():
        var = int(input("\nCombien de dégats a t-il reçu ? : "))
        return var

    def say_fight_over():
        print('''₮ØɄ₴ ⱠɆ₴ Ɇ₦₦Ɇ₥ł₴ ₴Ø₦₮ V₳ł₦₵Ʉ₴''')
    
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    def waiting_screen(sec):
        time.sleep(sec)

    def say_is_dead(name):
        print(Color.MAGENTA + f"{name} a été vaincu !!!\n" + Color.RESET)