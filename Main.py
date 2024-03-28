from Character import Character  # Importer le module sous le nom character
from Console import Console

class Main:
  def __init__(self):
    Console.clear_console()

    Console.say_preparation()
    Console.waiting_screen(3)
    Console.clear_console()
    ## création de la liste
    characters = []
    listing = True
    order = 1
    friendly = True
    while listing:
      name = Console.ask_name()
      if name == '':
        listing = False
        break
      friendly_input = Console.ask_friendly()
      if friendly_input == "1":
        friendly = True
      else:
        friendly = False
      hp = Console.ask_hp(name)
      characters.append(Character(name, hp, order, friendly))  # Utilisation de character.Character
      order += 1
      Console.clear_console()

    characters = sorted(characters, key=lambda x: x.get_order())
    characters2 = sorted(characters, key=lambda x: x.get_order())

    ##Maintenant, le combat commence :

    Console.clear_console()

    Console.say_fight_starting()
    Console.waiting_screen(3)
    Console.clear_console()

    ##fonction pour determiner la fin du combat, à appeler à chaque fois


    def end_of_fight(liste):
      ennemi = 0
      for perso in liste:
        if perso.friendly == False:
          ennemi +=1
      if ennemi > 0:
        return False
      else:
        return True
    

    while end_of_fight(characters) is False:
      for character2 in characters2:
          Console.clear_console()
          if character2.is_dead():
            break
          else:
            Console.say_round(character2.name, character2.friendly)
            choix_attaque = Console.ask_action()
            end_of_tour = False
            if choix_attaque == 1:
              while end_of_tour == False:
                Console.say_target()
                for character2 in characters2:
                  if not character2.is_dead():
                    Console.say_character(character2.order, character2.name, character2.hp, character2.friendly)
                choix_ennemi = Console.ask_target()
                if choix_ennemi == 0:
                  end_of_tour = True
                  break
                else:
                  for character in characters:
                    if character.order == choix_ennemi:
                      degats = Console.ask_degats()
                      character.lower_health(degats)
                      characters2[choix_ennemi-1].lower_health(degats)
                      if character.is_dead():
                        Console.say_is_dead(character.name)
                        characters.remove(character)
                      
    
    Console.clear_console()
    Console.say_fight_over()
    Console.waiting_screen(3)

              
             
      
if __name__ == "__main__":
  main_instance = Main()
