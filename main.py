import random
import os
import platform
import functions
from hero import Hero  

print("Operating System:", os.name)
print("Python Version:", platform.python_version())

# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

num_stars = 0
lifesteal = 0
shield = 0          
shield_regen = 4    

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

# --- Input Phase: Get valid combat strengths ---
i = 0
input_invalid = True
while input_invalid and i < 5:
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")
    if not (combat_strength.isnumeric() and m_combat_strength.isnumeric()):
        print("    |    Invalid input. Please enter integer numbers for Combat Strength.")
        i += 1
        continue
    elif int(combat_strength) not in range(1, 7) or int(m_combat_strength) not in range(1, 7):
        print("    |    Please enter a valid integer between 1 and 6.")
        i += 1
        continue
    else:
        input_invalid = False

if not input_invalid:
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # --- Weapon Roll ---
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
    """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)
    combat_strength = min(6, combat_strength + weapon_roll)
    print("    |    The hero's weapon is " + str(weapons[weapon_roll - 1]))
    functions.adjust_combat_strength(combat_strength, m_combat_strength)

    # --- Weapon Analysis ---
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    if weapon_roll <= 2:
        print("    |    --- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("    |    --- Your weapon is meh")
    else:
        print("    |    --- Nice weapon, friend!")
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # --- Health Points ---
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")
    print("    |", end="    ")
    input("Roll for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Monster rolled " + str(m_health_points) + " health points")

    # --- Loot Collection ---
    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 4 items:")
    input("Press enter to see what's inside and make your choices...")

    # Collect Loot and Make Choices
=======
    print("    |    !!You find a loot bag!! You look inside to find 2 items:")
    print("    |", end="    ")
    input("Roll for first item (Press enter)")
    loot_options, belt = functions.collect_loot(loot_options, belt)
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")
    loot_options, belt = functions.collect_loot(loot_options, belt)
    print("    |    You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("    |    Your belt: ", belt)

    # Use Loot
    belt, health_points, combat_strength = functions.use_loot(belt, health_points, combat_strength)

    print("    |", end="    ")
    print(f"Updated combat strength after using items: {combat_strength}")
=======
    # --- Use Loot ---
    belt, health_points = functions.use_loot(belt, health_points)

    print("    |", end="    ")
    input("Analyze the roll (Press enter)")
    print("    |    --- You are matched in strength: " + str(combat_strength == m_combat_strength))
    print("    |    --- You have a strong player: " + str((combat_strength + health_points) >= 15))

    # --- Monster's Magic Power ---
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
            @%   @                      
     @     @                        
         &                          
  @      .                          

 @       @                    @     
          @                  @      
  @         @              @  @     
   @            ,@@@@@@@     @      
     @                     @        
        @               @           
             @@@@@@@                
                                  """
    print(ascii_image4)
    power_roll = random.choice(list(monster_powers.keys()))
    m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(m_combat_strength) +
          " using the " + power_roll + " magic power")
    
    # --- Optional Legendary Quest ---
    if random.random() < 1.0:
        print("\n*** A legendary treasure chest appears! ***")
        class TempHero:
            pass
        temp_hero = TempHero()
        temp_hero.combat_strength = combat_strength
        temp_hero.health_points = health_points
        temp_hero.weapon = None
        temp_hero.shield = 0
        temp_hero.lifesteal = 0
        if functions.legendary_quest(temp_hero):
            combat_strength = temp_hero.combat_strength
            health_points = temp_hero.health_points
            if getattr(temp_hero, "weapon", None):
                print("    |    New weapon equipped:", temp_hero.weapon)
            if getattr(temp_hero, "shield", 0) > 0:
                print("    |    New shield acquired:", temp_hero.shield)
                shield = temp_hero.shield
            if getattr(temp_hero, "lifesteal", 0) > 0:
                print("    |    New lifesteal ability acquired:", temp_hero.lifesteal)
        lifesteal = temp_hero.lifesteal

    # --- Dream Level Sequence ---
    print("    ------------------------------------------------------------------")
    num_dream_lvls = functions.dream_level()
    if num_dream_lvls != 0:
        health_points -= 1
        crazy_level = functions.inception_dream(num_dream_lvls)
        combat_strength += crazy_level
        print("    |    combat strength: " + str(combat_strength))
        print("    |    health points: " + str(health_points))
    print("    |    Number of dream levels: ", num_dream_lvls)
    
    # ------------------- PRIMARY FIGHT SEQUENCE (DRAGON FIGHT) -------------------
    print("    ------------------------------------------------------------------")
    print(dragon_art)
    print("    |    You meet the dragon. FIGHT!!")
    while m_health_points > 0 and health_points > 0:
        print("    |", end="    ")
        input("Roll to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)
        if attack_roll % 2 != 0:
            print("    |", end="    ")
            input("You strike (Press enter)")
            m_health_points, health_points = functions.hero_attacks(combat_strength, m_health_points, lifesteal, health_points)
            if m_health_points == 0:
                num_stars = 3
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The dragon strikes (Press enter)!!!")
                health_points, shield = functions.monster_attacks(m_combat_strength, health_points, shield, 0)
                if shield > 0:
                    shield += shield_regen
                    print("    |    Your shield regenerates by " + str(shield_regen) +
                          " points. New shield value: " + str(shield))
                if health_points == 0:
                    num_stars = 1
                else:
                    num_stars = 2
        else:
            print("    |", end="    ")
            input("The dragon strikes (Press enter)")
            health_points, shield = functions.monster_attacks(m_combat_strength, health_points, shield, 0)
            if shield > 0:
                shield += shield_regen
                print("    |    Your shield regenerates by " + str(shield_regen) +
                      " points. New shield value: " + str(shield))
            if health_points == 0:
                num_stars = 1
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The hero strikes!! (Press enter)")
                m_health_points, health_points = functions.hero_attacks(combat_strength, m_health_points, lifesteal, health_points)
                if m_health_points == 0:
                    num_stars = 3
                else:
                    num_stars = 2

    if m_health_points <= 0:
        winner = "Hero"
        print("\nYou defeated the dragon!")
    else:
        winner = "Monster"
        print("You lost the fight with the dragon! Game over.")
        exit()

    # ------------------- FINAL SCORE DISPLAY ---------------------------
    tries = 0
    input_invalid = True
    while input_invalid and tries < 5:
        print("    |", end="    ")
        hero_name = input("Enter your Hero's name (in two words): ")
        name_parts = hero_name.split()
        if len(name_parts) != 2:
            print("    |    Please enter a name with two parts (separated by a space)")
            tries += 1
        elif not (name_parts[0].isalpha() and name_parts[1].isalpha()):
            print("    |    Please enter an alphabetical name")
            tries += 1
        else:
            short_name = name_parts[0][:2] + name_parts[1][:1]
            print("    |    I'm going to call you " + short_name + " for short")
            input_invalid = False

    if not input_invalid:
        stars_display = "*" * num_stars
        print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")
        functions.save_game(winner, hero_name=short_name, num_stars=num_stars)
        print("    ------------------------------------------------------------------")
        print("    |    Game saved")
        print("    ------------------------------------------------------------------")
        print("    |    Thank you for playing")
        print("    ------------------------------------------------------------------")





