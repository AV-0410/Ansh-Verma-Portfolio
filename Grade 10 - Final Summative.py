#
# Summative Day 5
# Joseph Chen - Harold M Brathwaite SS (2482)
#
# Jan 24
# 100 points
# Class comments
# Your work
# Turned in
#
# AnshVerma_Forest Adventurer.py
# Text
#
# AnshVerma_Forest Adventurer
# Google Docs
# Private comments
import random

# player_status() takes in a player name, their heath (hp), and location
# function prints out the player information
def player_status(name, hp, location):
   print(name, ":", hp, "HP")

   # Map location numbers to descriptive names
   if location == 1:
       location = "Lake"

   elif location == 2:
       location = "Deeper in Forest"

   elif location == 3:
       location = "Hut"

   elif location == 4:
       location = "Back To Older Weapon"

   #output location - Looks like      Location : ___
   print("Location :", location)

# path_1() asks user for a game location and returns the choice
# Function prints location names
#user can either choose to go towards a lake or deeper into the forest
def path_1():
   print("\nAs the sun dips below the horizon, casting a warm glow through the towering trees, you realize you have been walking for about an hour.")
   print("The air is filled with the sounds of rustling leaves and distant bird calls, creating an enchanting atmosphere.")
   print("Suddenly, you find yourself at a crossroads with two diverging paths:")

  #print the options with a sense of mystery and curiosity
   print("\t1. Follow the path leading to a tranquil lake.")
   print("\t2. Go deeper into the mysterious and dimly lit forest, where shadows dance amongst the ancient trees.")

   # user input
   location = int(input("Choose your path (1 or 2): ")) #user inputs 1 or 2, to choose path
   return location

#choose_weapon(location) takes in (location) and returns weapon, hp, damage, enemy_type
#outputs the user their options and asks for input
def choose_weapon(location):
   weapon = ''#will hold what weapon the user is holding
   hp = 0 #will hold users hp
   damage = 0 #will hold users damage


   if location == 1: #if user chooses lake
       # Provide details for weapons at the lake
       print("\nAfter walking towards the lake for about two hours, the enchanting sounds of rippling water surround you.")
       print("As you approach the shoreline, you discover two weapons laid before you – a sharp Axe and a finely crafted Bow and Arrow.")
       print("You realize that your tribe's fate lies in your hands, and you can only carry one weapon.")

       print("\taxe (30-70 damage, -8 HP per use)")
       print("\tbowarow (30-80 damage, -18 HP per use)")

       #user chooses weapon
       weapon = input("Choose your weapon (axe or bowarrow)*Please type answer in all lowercase as seen above* : ")
       enemy_type = "Magical Serpents"

       if (weapon == 'axe'):
           hp_loss = 8
           damage = random.randint(30, 80)
       elif (weapon == 'bowarrow'):
           hp_loss = 18
           damage = random.randint(60, 90)

   if location == 2: #if user chooses to go deeper into forest
       # Provide details for weapons in the deeper forest
       print("\nAfter walking deeper into the forest for about two hours, the trees began casting mysterious shadows on the forest floor.")
       print("As you venture further, you stumble upon two distinct weapons that catch your eye – a sturdy Spear and a sleek Crossbow.")
       print("In the midst of the ancient trees, you realize that your choice will shape the challenges you face ahead. You can only carry one weapon.")
       print("\tspear (30-70 damage, -8 HP per use)")
       print("\tcrossbow (30-70 damage, -18 HP per use)")

       #user inputs weapon
       weapon = input("Choose your weapon (spear or crossbow) *Please type answer in all lowercase as seen above* : ")
       enemy_type = "Magical Gorillas"

       if (weapon == 'spear'):
           hp_loss = 8
           damage = random.randint(30, 70)
       elif (weapon == 'crossbow'):
           hp_loss = 18
           damage = random.randint(30, 80)

   return weapon, hp_loss, damage, enemy_type

#after_fight(weapon, hp_loss, damage, location) takes in (weapon, hp_loss, damage, location)
# returns weapon, hp_loss, damage, location
#function only runs if user beats initial enemy
#will give user option to explore hut, or go to previous weapon
def after_fight(weapon, hp_loss, damage, location):
   print("\nOh-no! Your", weapon, "has shattered into pieces after the intense battle.")
   print("You stand amidst the aftermath, determined to find a new weapon quickly.")

   print("\nAs you journey through the mystical forest, you can see an ancient hut afar.")

   #user inputs if they want to explore hut or go back to weapon that was left
   print("\t1. Explore the hut.")
   print("\t2. Get other weapon")
   choice = int(input("Do you dare to explore the mysterious hut, or would you rather backtrack to the weapons you left behind? (Enter 1 to explore the hut, 2 to get other weapon): "))

   if choice == 1:
       # Details for choosing to explore the hut
       #gets a new weapon with new stats
       print("\nInside the hut, a dim light reveals a treasure of forgotten artifacts.")
       print("Among them, you discover a legendary Dualed Sword.")
       print("Dualed Sword (45-90 damage, -15 HP per use)")
       weapon = 'dualedsword'
       hp_loss = 15
       damage = random.randint(40, 90)
       location = 3

   if choice == 2:
       # Details for choosing to go back
       print("\nYou decide to retrace your steps, heading back to where you initially found the two weapons.")

       if location == 1:
           # Details if going back to the lake
           #swaps weapon
           if weapon == 'axe':
               print("After walking back, you retrieve the bow and arrow now.")
               weapon = 'bowarrow'
               hp_loss = 18
               damage = random.randint(30, 80)

           elif weapon == 'bowarrow':
               print("After walking back, you retrieve the axe now.")
               weapon = 'axe'
               hp_loss = 8
               damage = random.randint(30, 70)

       location = 4

       if location == 2:
           # Details if going back to the deep forest
           # swaps weapons
           if weapon == 'spear':
               print("After walking back, you retrieve the crossbow now.")
               weapon = 'crossbow'
               hp_loss = 18
               damage = random.randint(30, 80)

           elif weapon == 'crossbow':
               print("After walking back, you retrieve the spear now.")
               weapon = 'spear'
               hp_loss = 8
               damage = random.randint(30, 70)

       location = 4

   return weapon, hp_loss, damage, location


#initial_enemy (location) takes in location
#returns the stats of the first enemy
def initial_battle(location):
   if location == 1:
       return 'Magical Serpents', 100, random.randint(30, 65)
   else:
       return 'Magical Gorillas', 100, random.randint(30, 65)


#play(hp, enemy_damage, damage, hp_loss, hp_enemy, enemy_type, weapon, location, name)
#takes in (hp, enemy_damage, damage, hp_loss, hp_enemy, enemy_type, weapon, location, name)
#returns 1 for win, 2 for loss
#outputs the fights between both enemies
#randomizes attacks
def play(hp, enemy_damage, damage, hp_loss, hp_enemy, enemy_type, weapon, location, name) :

   #right after you receive your 2nd weapon
   if location == 3 or location == 4 :
       print("\nAs you pick up your weapon, the sky suddenly illuminates with a radiant yellow beam, guiding you towards the gold for your quest.")
       print("You walk towards it with renewed confidence, but then, from the shadows, a", enemy_type, "emerges!")

   #first fight
   else :
       print("\nYou continue walking, but the forest grows denser, and an eerie silence hangs in the air.")
       print("Suddenly, you hear a faint sound in the distance – a mysterious melody that sends shivers down your spine.")
       print("Driven by curiosity, you cautiously approach the source of the sound.")
       print("To your surprise, a clearing reveals itself, adorned with ancient runes and a mystical portal.")
       print("You sense the presence of an otherworldly force and brace yourself for the unknown.")
       print("And then, from the portal", enemy_type, "materialize!")

   print("\n" + enemy_type, ":", hp_enemy, "HP")
   print("Your", weapon, "costs", hp_loss, "HP everytime you attack.")


   #loop for fights
   while hp_enemy > 0 and hp > 0:

       #user randomized attacks
       if (weapon == 'axe'):
           hp_loss = 8
           damage = random.randint(30, 70)
       elif (weapon == 'bowarrow'):
           hp_loss = 18
           damage = random.randint(30, 80)

       elif weapon == 'spear':
           hp_loss = 8
           damage = random.randint(30, 70)

       elif weapon == 'crossbow':
           hp_loss = 18
           damage = random.randint(30, 80)

       else :
          hp_loss = 15
          damage = random.randint(45, 90)

       hp_enemy = hp_enemy - damage
       print("\nYou dealt", damage, "damage to the", enemy_type + "!")
       print(enemy_type, ":", hp_enemy, "HP left")

       if hp_enemy <= 0 :
           #defeating the enemy
           print("\nCongratulations! You defeated the", enemy_type + "!")
           return 1

       print("\nNow the", enemy_type, "attack!")
       hp = hp - enemy_damage
       print("The", enemy_type, "dealt", enemy_damage, "damage to you!")

       hp = hp - hp_loss
       print(name, ":", hp, " HP left")

       if hp <= 0  :
           #being defeated
           print("\nOh-no! You were defeated by the", enemy_type + "!")
           return 2

#play_game()
#main function
#combines all functions together, so user can play game

def play_game():
   hp = 100  #initialize player hp
   location = "Entrance of Forest"
   weapon = 0
   name = input("Enter your display name : ")  # player name

   # Start Game with welcoming message and backstory
   print('\nWELCOME TO FOREST ADVENTURER ')

   #provide a backstory
   print("\n" + name + ", your tribe, known for their valor and bravery, has entrusted you with a perilous quest – to retrieve the gold hidden deep within the heart of the Enchanted Magical Forest.")
   print("Legend has it that no one has ever ventured into this mystical realm and returned alive. Yet, driven by the call of adventure, you stand at the entrance, ready to face the unknown.")

   # Set the stage for the challenges ahead
   print("Alas, due to your tribe's humble resources, they couldn't equip you with a weapon. The forest is known to be fraught with dangers, and you must rely on your wit and courage to navigate through the shadows.")

   print("")

   #display initial player status
   player_status(name, hp, location)

   # Choose the initial path
   location = path_1()

   # Check the chosen path and proceed accordingly
   if location == 1 or location == 2:
       # Player chooses a weapon and faces initial enemy
       weapon, hp_loss, damage, enemy_type = choose_weapon(location)
       enemy_type, hp_enemy, enemy_damage = initial_battle(location)

       # Start the game with the first battle
       game = play(hp, enemy_damage, damage, hp_loss, hp_enemy, enemy_type, weapon, location, name)

       # Start the game with the first battlE
       if (game) == 1:
           print("HP reset to 100 for winning!")
           print("")
           hp = 100
           player_status (name, hp, location)

           # after first battle function
           weapon, hp_loss, damage, location = after_fight(weapon, hp_loss, damage, location)

           print()
           player_status (name, hp, location)

           # Prepare for the final battle against the 3 Headed Giant
           enemy_type = '3 Headed Giant'
           hp_enemy = 120
           enemy_damage = random.randint(35, 80)

           # Start the final battle
           game = play(hp, enemy_damage, damage, hp_loss, hp_enemy, enemy_type, weapon, location, name)

           # Check the result of the final battle and output winning message
           if game == 1:
               print("After defeating the 3 Headed Giant, you run straight towards the gold, showering in it")
               print("\nWhat a brave adventurer! You have completed your quest!")
               print("You make your way back through familiar paths that you followed to reach the gold!")
               print("When you make it back your clan gathers around cheering for you and your legacy will be remembered for ages to come!")
               print("\nGAME OVER. Thanks for playing!")

           #losing message
           else:
               print("\nGAME OVER! To restart, play again.")

       else:
           print("\nGAME OVER! To restart, play again.")
   else:
       # handle invalid input for the path
       location = path_1()

#execute the game
play_game()