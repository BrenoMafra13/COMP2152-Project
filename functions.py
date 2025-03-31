# Import the random library to use for the dice later
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
    if combat_strength >= m_health_points:
        # Player was strong enough to kill monster in one blow
        m_health_points = 0
        print("    |    You have killed the monster")
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
    else:
        # Monster only damaged the player
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points

# Recursion
# You can choose to go crazy, but it will reduce your health points by 5
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    # Base Case
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2

    # Recursive Case
    else:
        # inception_dream(5)
        # 1 + inception_dream(4)
        # 1 + 1 + inception_dream(3)
        # 1 + 1 + 1 + inception_dream(2)
        # 1 + 1 + 1 + 1 + inception_dream(1)
        # 1 + 1 + 1 + 1 + 2
        return 1 + int(inception_dream(num_dream_lvls - 1))

# Lab 06 - Question 3 and 4
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

def load_game():
    filename = "save.txt"
    filepath = os.path.join(os.getcwd(), filename)
    try:
        with open(filepath, "r") as file:
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

# Lab 06 - Question 5b
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
