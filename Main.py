from Character import Character  # Importer le module sous le nom character
from Console import Console

class Main:
  def __init__(self):
    Console.clearConsole()

    Console.sayPreparation()
    Console.waitingScreen(3)
    Console.clearConsole()
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
      Console.clearConsole()

    characters = sorted(characters, key=lambda x: x.getOrder())

    ##Maintenant, le combat commence :

    Console.clearConsole()

    Console.sayFightStarting()
    Console.waitingScreen(3)
    Console.clearConsole()

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
          Console.clearConsole()
          Console.sayRound(character.name, character.friendly)
          choixAttaque = Console.askAction()
          endOfTour = False
          if choixAttaque == 1:
            while endOfTour == False:
              Console.sayTarget()
              for character in characters:
                Console.sayCharacter(character.order, character.name, character.hp, character.friendly)
              choixEnnemi = Console.askTarget()
              if choixEnnemi == 0:
                endOfTour = True
                break
              else:
                for i in range(len(characters)):
                  if characters[i].order == choixEnnemi:
                    degats = Console.askDegats()
                    characters[i].lowerHealth(degats)
                    if characters[i].isDead():
                      Console.sayIsDead(characters[i].name)
                      characters.remove(characters[i])
                    break
    
    Console.clearConsole()
    Console.sayFightOver()
    Console.waitingScreen(3)

              
             
      
if __name__ == "__main__":
  main_instance = Main()
