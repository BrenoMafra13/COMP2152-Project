import random
from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__(random.randint(1, 6) * 10, random.randint(1, 6) * 20)

    def __del__(self):
        print("The Monster is being destroyed.")
        super().__del__()

    def monster_attacks(self):
        attack_damage = random.randint(1, 15)
        print(f"Monster attacks: {attack_damage} damage to hero.")
        return attack_damage
