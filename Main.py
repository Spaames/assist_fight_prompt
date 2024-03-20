from Character import Character  # Importer le module sous le nom character
import os
from Console import Console

class Main:
  def __init__(self):
    os.system('clear')

    Console.sayPreparation()
    ## création de la liste
    characters = []
    listing = True
    order = 1
    friendly = True
    while listing:
      name = Console.askName()
      if name == '':
        listing = False
        break
      friendly_input = Console.askFriendly()
      if friendly_input == "1":
        friendly = True
      else:
        friendly = False
      hp = Console.askHP(name)
      characters.append(Character(name, hp, order, friendly))  # Utilisation de character.Character
      order += 1
      os.system('clear')

    characters = sorted(characters, key=lambda x: x.getOrder())

    ##Maintenant, le combat commence :

    os.system('clear')

    print("Début du combat...\n\n")

    ##fonction pour determiner la fin du combat, à appeler à chaque fois


    def endOfFight(characters):
      ennemi = 0
      for character in characters:
        if character.friendly == False:
          ennemi +=1
      if ennemi > 0:
        return False
      else:
        return True
    

    while endOfFight(characters) is False:
      for character in characters:
          print(f"C'est au tour de {character.name} de jouer, que fait-il ?\n")
          choixAttaque = input("[1] Attaque\n[2] Autre chose\n")
          endOfTour = False
          if choixAttaque == "1":
            while endOfTour == False:
              print("\n Qui reçoit des dégats ?\n")
              for character in characters:
                print(f"[{character.order}] - {character.name}\n")
              choixEnnemi = int(input("Choissisez un nombre ci-dessus : "))
              if choixEnnemi == 0:
                endOfTour = True
                break
              else:
                for i in range(len(characters)):
                  print(f"character.order = {character.order} / choixEnnemi = {choixEnnemi}")
                  if character.order == choixEnnemi:
                    degats = int(input("\nCombien de dégats a t-il reçu ? : "))
                    character.lowerHealth(degats)
                    if character.isDead():
                      characters.remove(character)
                    break
    
    print("le combat est terminé")


              
             
      
if __name__ == "__main__":
  main_instance = Main()
