import random
import os


# Will the line below print when you import functions_lab10.py into main.py?
# print("Inside functions_lab10.py")

def use_loot(belt, health_points, combat_strength):
    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    while belt:
        item_used = belt.pop(0)
        if item_used == "Health Potion":
            health_gain = 5
            health_points = min(100, health_points + health_gain)
            print(f"    |    You used {item_used}, increasing your health by {health_gain} to {health_points}.")
        elif item_used == "Leather Boots":
            shield = 3
            health_points = min(100, health_points + shield)
            print(f"    |    You used {item_used}, giving you a shield of {shield}. Total life + shield is now {health_points}.")
        elif item_used == "Poison Potion":
            decrease_health = 3
            health_points = max(0, health_points - decrease_health)
            print(f"    |    You used {item_used}, decreasing your health by {decrease_health} points, now your health is {health_points}.")
        elif item_used == "Secret Note":
            combat_strength += 2
            print(f"    |    You read the Secret Note and discovered a strategic advantage. Combat strength increased by 2 to {combat_strength}.")
        else:
            print(f"    |    You used {item_used}, but it appears to be ineffective.")

    return belt, health_points, combat_strength

=======
def use_loot(belt, health_points):
    # Increased healing effect for the Health Potion to 5 HP.
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        if first_item == "Health Potion":
            health_points = min(20, (health_points + 5))
            print("    |    You used " + first_item + " to increase your health to " + str(health_points))
        else:
            print("    |    You used " + first_item + ". It feels sturdy!")
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print("    |    You used " + first_item + " and your health is reduced to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points



def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    if len(loot_options) < 4:
        print("Not enough items to choose from!")
        return loot_options, belt
    selected_items = random.sample(loot_options, 4)

    pairs = [(selected_items[i], selected_items[i + 1]) for i in range(0, 4, 2)]
    for idx, (item1, item2) in enumerate(pairs, start=1):
        print(f"\n    |    Pair {idx}: {item1} and {item2}.")
        choice = input(f"Type 1 for {item1} or 2 for {item2}: ")
        while choice not in ['1', '2']:
            print("\nInvalid input. Please enter '1' or '2'.")
            choice = input(f"Type 1 for {item1} or 2 for {item2}: ")

        chosen_item = item1 if choice == '1' else item2
        belt.append(chosen_item)
        loot_options.remove(chosen_item)

    print("\n    |    Your belt: ", belt)
    return loot_options, belt

# Hero's Attack Function
def hero_attacks(combat_strength, m_health_points):
=======

# Hero's Attack Function (includes lifesteal effect)
def hero_attacks(combat_strength, m_health_points, lifesteal=0, hero_health=0):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  

  """
    print(ascii_image)
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    damage = random.randint(1, combat_strength)
    if damage >= m_health_points:
        m_health_points = 0
        print("    |    You dealt " + str(damage) + " damage and killed the monster!")
    else:

        # Player only damaged the monster
        m_health_points -= combat_strength

        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points

# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        # Monster was strong enough to kill player in one blow
        health_points = 0
        print("    |    Player is dead")
=======
        m_health_points -= damage
        print("    |    You dealt " + str(damage) + " damage, reducing the monster's health to " + str(m_health_points))
    if lifesteal > 0:
        heal = int(damage * lifesteal)
        hero_health += heal
        print("    |    Vampirism activated! You heal for " + str(heal) + " points. Your health is now " + str(hero_health))
    return m_health_points, hero_health


# Monster's Attack Function with Shield Mechanics and Regeneration
def monster_attacks(m_combat_strength, hero_health, hero_shield=0, shield_regen=0):
    dragon_art = r"""
                           /           /
                  ___====-_  _-====___
            _--^^^#####//      \\#####^^^--_
         _-^##########// (    ) \\##########^-_
        -############//  |\^^/|  \\############-
      _/############//   (@::@)   \\############\_
     /#############((     \\//     ))#############\
    -###############\\    (oo)    //###############-
   -#################\\  / "" \  //#################-
  -###################\\/  (_)  \//###################-
 _#/|##########/\######(   "/"   )######/\##########|\#_
 |/ |#/\#/\#/\/  \#/\##\  ! ' !  /##/\#/  \/\#/\#/\| \|
 '  |/  V  V '   V  \\#\  \   /  /#/  V   '  V  V  \|  '
    '   '  '      '   /#\  | |  /#\   '      '  '   '
                     (  (  | |  )  )
                    __\  \ | | /  /__
                   (vvv(VVV)(VVV)vvv)
    """
    print(dragon_art)
    damage = random.randint(1, m_combat_strength)
    print("    |    Monster's attack damage: " + str(damage))
    
    # Shield absorbs damage if available.
    if hero_shield > 0:
        if damage <= hero_shield:
            print("    |    Your shield absorbed all " + str(damage) + " damage.")
            hero_shield -= damage
            damage = 0
        else:
            print("    |    Your shield absorbed " + str(hero_shield) + " damage and broke!")
            damage -= hero_shield
            hero_shield = 0
    if damage > 0:
        hero_health -= damage
        print("    |    You took " + str(damage) + " damage. Your health is now " + str(hero_health))

    else:
        print("    |    No damage got through. Your health remains at " + str(hero_health))
    
    # Regenerate shield after every monster attack.
    if shield_regen > 0:
        hero_shield += shield_regen
        print("    |    Your shield regenerates by " + str(shield_regen) + " points. New shield value: " + str(hero_shield))
    
    return hero_health, hero_shield


# Recursion (Inception Dream)
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2
    else:
        return 1 + int(inception_dream(num_dream_lvls - 1))


# Lab 06 - Question 3 and 4
=======

# Lab 06 - Save and Load Game Functions

def save_game(winner, hero_name="", num_stars=0):
    filename = "save.txt"
    filepath = os.path.join(os.getcwd(), filename)
    last_game_state, last_monsters_count = load_game()
    new_total_monsters_killed = last_monsters_count + 1 if winner == "Hero" else last_monsters_count
    try:
        with open(filepath, "a") as file:
            if winner == "Hero":
                file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
            elif winner == "Monster":
                file.write("Monster has killed the hero.\n")
            file.write(f"Total monsters killed: {new_total_monsters_killed}\n")
    except Exception as e:
        print(f"Failed to write to file: {e}")
=======
    new_total_monsters_killed = last_monsters_count
    with open("save.txt", "a") as file:
        if winner == "Hero":
            new_total_monsters_killed += 1
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero.\n")
        file.write(f"Total monsters killed: {new_total_monsters_killed}\n")


def load_game():
    filename = "save.txt"
    filepath = os.path.join(os.getcwd(), filename)
    try:
        with open(filepath, "r") as file:
=======
        with open("save.txt", "r") as file:
            print("Loading from saved file")
            last_monsters_count = 0
            last_game_state = ""
            for line in file:
                if line.startswith("Total monsters killed"):
                    last_monsters_count = int(line.strip().split(":")[1].strip())
                elif line.strip():
                    last_game_state = line.strip()
            print(f"Total monsters killed: {last_monsters_count}")
            return last_game_state, last_monsters_count
    except FileNotFoundError:
        print("No previous game found, starting first game")
        return "", 0


# Lab 06 - Adjust Combat Strength
def adjust_combat_strength(combat_strength, m_combat_strength):
    last_game_state, total_monsters_killed = load_game()
    if last_game_state:
        if "Hero" in last_game_state and "gained" in last_game_state:
            num_stars = int(last_game_state.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                m_combat_strength += 1
        elif "Monster has killed the hero" in last_game_state:
            combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")
    return combat_strength, m_combat_strength


def dream_level():
    while True:
        user_input = input("Quantity of dream levels to go down? (Enter 0 to 3): ")
        try:
            dream_lvls = int(user_input)
            if 0 <= dream_lvls <= 3:
                return dream_lvls
            else:
                print("Enter a number between 0 and 3.")
        except ValueError:
            print("Enter a valid integer.")


# Legendary Quest Function (updated for Excalibur +10 and Relic of Power +10)
def legendary_quest(hero):
    print("\n*** Legendary Quest Triggered! ***")
    chest_art = r"""
           __________
          /\____;;___\
         | /         /
         `. ())oo() .
         |\(%()*^^()^\
        %| |-%-------|
       % \ | %  ))   |
       %  \|%________|
        %%%%
    """
    print(chest_art)
    challenge_result = random.randint(1, 10)
    print("You roll the challenge dice... Result:", challenge_result)
    if challenge_result >= 3:
        print("You have overcome the challenge and unlocked the legendary chest!")
        legendary_items = [
            {"name": "Relic of Power", "type": "buff", "effect": "Increase combat strength by 10", "bonus": 10, "art": r"""
                __________
               '._==_==_=_.' 
               .-\:      /-. 
              | (|:.     |) | 
               '-|:.     |-'  
                 \::.    /   
                  '::. .'
                    ) (
                  _.' '._ 
                 `"""""""` 
            """},
            {"name": "Excalibur", "type": "weapon", "effect": "Equip to gain +10 to combat and health", "bonus": 10, "art": r"""
                 _
                (_)
                |=|
                |=|
            /|__|_|__|\
           (    ( )    )
            \|\/\"/\/|/
              |  Y  |
              |  |  |
              |  |  |
             _|  |  |
          __/ |  |  |\
         /  \ |  |  |  \
        __|  |  |  |   |
      /\/  |  |  |   |\
       <   +\ | |\ />  \
        >   + \  | LJ    |
              + \|+  \  < \
        (O)      +    |    )
         |             \  /\ 
       ( | )   (o)      \/  )
      _\\|//__( | )______)_/ 
              \\|// 
            """},
            {"name": "Mystic Amulet", "type": "shield", "effect": "Provides shield regeneration of 4 per turn", "bonus": 4, "art": r"""
                o--o--=g=--o--o
               /      .'       \
               o      '.       o
                \             /
                 o           o
                  \         /
                   o       o
                    \     /
                     o   o
                      \_/
                       =
                      .^.
                     '   '
                     '. .'
                       !
            """},
            {"name": "Vampirism Cape", "type": "lifesteal", "effect": "Gain 50% of damage dealt as HP", "bonus": 0.5, "art": r"""
             ,*-~\"`^\"*u_                                _u*\"^`\"~-*,
          p!^       /  jPw                            w9j \        ^!p
        w^.._      /      \_                      _/\"     \        _.^w
             *_   /          \_      _    _      _/         \     _* 
               q /           / \q   ( `--` )   p/ \          \   p
               jj5****._    /    ^\_) o  o (_/^    \    _.****6jj
                        *_ /      \"==) ;; (==\"      \ _*
                         `/.w***,   /(    )\   ,***w.\"
                          ^ ilmk ^c/ )    ( \c^      ^
                                  'V')_)(_('V'
                                      `` ``
            """}
        ]
        reward = random.choice(legendary_items)
        print(f"You have found the {reward['name']}! {reward['effect']}")
        print(reward["art"])
        if reward["name"] == "Excalibur":
            decision = input("Do you want to equip Excalibur? (y/n): ")
            if decision.lower() == "y":
                hero.combat_strength += reward["bonus"]
                hero.health_points += reward["bonus"]
                hero.weapon = "Excalibur"
                print("Excalibur equipped! Your combat and health points increased by 10 each.")
            else:
                print("You leave Excalibur behind.")
        elif reward["name"] == "Relic of Power":
            hero.combat_strength += reward["bonus"]
            hero.relic = True
            print(f"Your combat strength increases by {reward['bonus']}.")
        elif reward["name"] == "Mystic Amulet":
            hero.shield = reward["bonus"]
            print("You gain the Mystic Amulet! You now regenerate 4 shield points each turn.")
        elif reward["name"] == "Vampirism Cape":
            hero.lifesteal = reward["bonus"]
            print("You gain the Vampirism Cape! You now steal half the damage dealt as health.")
        return True
    else:
        print("You failed the legendary quest challenge. The chest vanishes!")
        return False





