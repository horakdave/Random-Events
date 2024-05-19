import random
import time

maximum = 100

class Character:
    def __init__(self, name):
        self.name = name
        self.health = maximum

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
            "smashed keyboard on head of": (10, 20),
            "sniped": (40, 50),
            "slapped": (5, 5),
            "tackled": (0, 1),
            "drove a car over": (15, 20),
            "(MISSED)": (0, 0),
            "(MISSED)": (0, 0),
            "(MISSED)":(0, 0),
            "(MISSED)": (0, 0),
            "(MISSED)": (0, 0),
            "poisoned a drink of": (-5, 20),
            "upper punched":(5, 10),
            "headbutt": (10, 15),
            "elbow strike": (5, 10),
            "knee strike": (8, 12),
            "hair pull": (1, 3),
            "ear slap": (3, 7),
            "nose strike": (4, 8),
            "throat striked": (6, 10),
            "farted on": (0, 3),
            "insulted": (0, 5),
            "tickled": (0, 2),
            "told a bad joke to": (0, 3),
            "threw a pie at": (5, 10),
            "slammed a door on": (15, 20),
            "threw a snake at": (8, 12),
            "summoned a lightning bolt on": (25, 35),
            "sent a swarm of bees to attack": (10, 15),
            "cast a fireball at": (20, 25),
            "used mind control on": (5, 10),
            "froze": (10, 15),
            "teleported behind": (5, 10),
            "performed a roundhouse kick on": (15, 20),
            "threw a grenade at": (20, 30),
            "summoned a giant spider to attack": (15, 25),
            "lightning-fast punched": (10, 15),
            "used a smoke bomb on": (5, 10),
            "unleashed a sonic scream on": (15, 20),
            "inflicted a curse on": (10, 15),
            "performed a backflip kick on": (10, 15),
            "threw a shuriken at": (8, 12),
            "used a time freeze on": (20, 25),
            "summoned a meteor to strike": (30, 40),
            "transformed into a werewolf and attacked": (25, 30),
            "thunderously blew up": (20, 25),
            "used a shadow clone jutsu on": (15, 20),
            "performed a spinning tornado kick on": (15, 20),
            "threw a vial of acid at": (15, 20),
            "energy blastsed": (25, 30),
            "used a gravity manipulation on": (10, 15),
            "activated a force field around": (20, 25),
            "performed a dragon's breath attack on": (30, 35),
            "threw a boulder at": (25, 30),
            "summoned a swarm of locusts to attack": (15, 20),
            "summoned devastating earthquake on": (35, 40),
            "used a mind-reading technique on": (10, 15),
            "activated a time distortion field around": (25, 30),
            "performed a whirlwind strike on": (20, 25),
            "threw a chain lightning at": (30, 35),
            "summoned a spectral dragon to attack": (40, 50),
            "shot a celestial beam on": (35, 40),
            "used a reality-warping ability on": (25, 30),
            "activated a black hole around": (40, 50),
            "performed a divine judgment on": (50, 60),
            "threw a comet at": (45, 55),
            "shot a cosmic blast at": (40, 50),
            "used a dimension-warping technique on": (30, 40),
            "activated a supernova around": (50, 60),
            "threw a kitten at": (2, 5),
            "threw a pillow at": (2, 4),
        }
        attack_type, damage_range = random.choice(list(attacks.items()))
        damage = random.randint(*damage_range)
        other.health -= damage
        emoji = "💀💀💀💀💀" if other.health <= 0 else ""  # Check if the character is killed
        print(f"{self.name} {attack_type} {other.name} causing {damage} damage. {emoji}")
        other.display_health_bar()

    def display_health_bar(self):
        health_ratio = self.health / maximum
        bar_length = 5
        current_health = int(health_ratio * bar_length)
        health_bar = "[" + "❤️" * current_health + "🖤" * (bar_length - current_health) + "]"
        print(f"{self.name} Health: {health_bar}")
        print("")
    
    def heal_self(self):
        heal_amount = random.randint(15, 20)
        self.health = min(maximum, self.health + heal_amount)
        print(f"{self.name} healed themselves for {heal_amount} health.")
        self.display_health_bar()

    def take_steroids(self):
        steroid_amount = random.randint(10, 15)  # Define the steroid boost range as needed
        self.health += steroid_amount
        print(f"{self.name} took steroids and gained {steroid_amount} health!")
        self.display_health_bar()


characters = [Character(name) for name in ["David", "Bonifac", "Arnost", "Herald"]] #pridejte postav kolik chcete

while len([c for c in characters if c.is_alive()]) > 1:
    attacker, victim = random.sample([c for c in characters if c.is_alive()], 2)
    attacker.attack(victim)
    time.sleep(5)

print("The winner is:", [c.name for c in characters if c.is_alive()][0])