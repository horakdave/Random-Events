import random
import time

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 25  # maximum

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        if not self.is_alive():
            return
        attacks = {
            "punched": (1, 10),
            "kicked in the balls": (10, 15),
            "kicked": (5, 15),
            "sayed your mum to": (0, 2),
            "pulled out a fricking gun on": (20, 30),
            "spat on": (1, 5),
            "threw a rock at": (10, 15),
            "threw a paper airplane at": (0, 5),
            "healed": (-20, -10),
            "smashed keyboard on head of": (10, 20),
            "sniped": (40, 50),
            "slapped": (5, 5),
            "tackled": (0, 1),
            "gave steroids to": (-5, -5),
            "drove a car over": (15, 20),
            "(MISSED)": (0, 0),
            "(MISSED)": (0, 0),
            "(MISSED)":(0, 0),
            "(MISSED)": (0, 0),
            "(MISSED)": (0, 0),
            "poisoned a drink of": (-5, 20),
            "upper punched":(5, 10)
            
        }
        attack_type, damage_range = random.choice(list(attacks.items()))
        damage = random.randint(*damage_range)
        other.health -= damage
        emoji = "💀💀💀💀💀" if other.health <= 0 else ""  # Check if the character is killed
        print(f"{self.name} {attack_type} {other.name} causing {damage} damage. {emoji}")
        other.display_health_bar()

    def display_health_bar(self):
        health_ratio = self.health / 50  # maximum
        bar_length = 5
        current_health = int(health_ratio * bar_length)
        health_bar = "[" + "❤️" * current_health + "🖤" * (bar_length - current_health) + "]"
        print(f"{self.name} Health: {health_bar}")
        print("")


characters = [Character(name) for name in ["David", "Bonifac", "Arnost", "Herald"]] #pridejte postav kolik chcete

while len([c for c in characters if c.is_alive()]) > 1:
    attacker, victim = random.sample([c for c in characters if c.is_alive()], 2)
    attacker.attack(victim)
    time.sleep(3)

print("The winner is:", [c.name for c in characters if c.is_alive()][0])