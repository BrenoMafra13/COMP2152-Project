import random
from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__(random.randint(1, 6) * 10, random.randint(1, 6) * 20)

    def __del__(self):
        print("The Hero is being destroyed.")
        super().__del__()

    def hero_attacks(self):
        attack_damage = random.randint(1, 10)
        print(f"Hero attacks: {attack_damage} damage to monster.")
        return attack_damage
