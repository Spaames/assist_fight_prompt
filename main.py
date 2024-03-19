import character as character

class Main:
  def __init__(self):
    print("Le combat commence...\n\n")
    ## création de la liste
    characters = []
    listing = True
    order = 1
    friendly = True
    while listing:
      name = input("Entrez le nom du personnage : [tapez 'end' pour arrêter]\n")
      if name == "end":
        listing = False
        break
      friendly = input("[1] Allié \n[2] Ennemi\n") ##changer plus tard avec keyboard pour détecter les touches et ne plus avoir à valider
      hp = input(f"Entrez les points de vie de {name}: \n")
      characters.append(character.Character(name, hp, order, friendly))
      order += 1
      
    characters = sorted(characters, key=lambda x: x.getOrder())

    ##Maintenant, le combat commence :
    








if __name__ == "__main__":
  main_instance = Main()
