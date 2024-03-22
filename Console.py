from Color import Color
import os
import time

class Console:

    def __init__(self) -> None:
        pass

    def sayPreparation():
        print('''₱ⱤɆ₱₳Ɽ₳₮łØ₦   ĐɄ   ₵Ø₥฿₳₮...''')

    def askName():
        var = input("Entrez le nom du personnage : ")
        return var

    def askFriendly():
        print("\n" + Color.GREEN + "-1- Allié\n" + Color.RED + "-2- Ennemi\n" + Color.RESET)
        var = input("Indiquez la lettre correspondante : ")
        return var

    def askHP(name):
        var = int(input(f"\nEntrez ses points de vies: "))
        return var

    def sayFightStarting():
        print('''ĐɆ฿Ʉ₮ ĐɄ ₵Ø₥฿₳₮...''')

    def sayRound(name):
        print(f"C'est au tour de {name} de jouer, que fait-il ?\n")

    def askAction():
        print("-1- Attaque\n-2- Autre chose\n")
        var = int(input("Indiquez la lettre correspondante : "))
        return var

    def sayTarget():
        print("\nQui reçoit des dégats ?\n")

    def sayCharacter(order, name, hp, friendly):
        if friendly == True:
            print(Color.GREEN + f"-{order}-  {name}  {hp}PV" + Color.RESET)
        else :
            print(Color.RED + f"-{order}-  {name}  {hp}PV" + Color.RESET)

    def askTarget():
        print("-0-  Personne\n")
        var = int(input("Choissisez un nombre ci-dessus : "))
        return var

    def askDegats():
        var = int(input("\nCombien de dégats a t-il reçu ? : "))
        return var

    def sayFightOver():
        print('''₮ØɄ₴ ⱠɆ₴ Ɇ₦₦Ɇ₥ł₴ ₴Ø₦₮ V₳ł₦₵Ʉ₴''')
    
    def clearConsole():
        os.system('cls' if os.name == 'nt' else 'clear')

    def waitingScreen(sec):
        time.sleep(sec)

    def sayIsDead(name):
        print(Color.MAGENTA + f"{name} a été vaincu !!!\n" + Color.RESET)