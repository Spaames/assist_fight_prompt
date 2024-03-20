from Color import Color

class Console:

    def __init__(self) -> None:
        pass

    def sayPreparation():
        print("Préparation du combat...\n")

    def askName():
        var = input("\nEntrez le nom du personnage : \n")
        return var

    def askFriendly():
        print("\n" + Color.GREEN + "[1] Allié\n" + Color.RED + "[2] Ennemi\n" + Color.RESET)
        var = input("Tapez la lettre correspondante :   ")
        print("\n")
        return var

    def askHP(name):
        var = int(input(f"\nEntrez ses points de vies: \n"))
        return var
