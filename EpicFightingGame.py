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
            "struck with a lightning-fast punch": (10, 15),
            "used a smoke bomb on": (5, 10),
            "unleashed a sonic scream on": (15, 20),
            "inflicted a curse on": (10, 15),
            "performed a backflip kick on": (10, 15),
            "threw a shuriken at": (8, 12),
            "used a time freeze on": (20, 25),
            "summoned a meteor to strike": (30, 40),
            "transformed into a werewolf and attacked": (25, 30),
            "struck with a thunderous blow": (20, 25),
            "used a shadow clone jutsu on": (15, 20),
            "performed a spinning tornado kick on": (15, 20),
            "threw a vial of acid at": (15, 20),
            "struck with a barrage of energy blasts": (25, 30),
            "used a gravity manipulation on": (10, 15),
            "activated a force field around": (20, 25),
            "performed a dragon's breath attack on": (30, 35),
            "threw a boulder at": (25, 30),
            "summoned a swarm of locusts to attack": (15, 20),
            "struck with a devastating earthquake": (35, 40),
            "used a mind-reading technique on": (10, 15),
            "activated a time distortion field around": (25, 30),
            "performed a whirlwind strike on": (20, 25),
            "threw a chain lightning at": (30, 35),
            "summoned a spectral dragon to attack": (40, 50),
            "struck with a celestial beam": (35, 40),
            "used a reality-warping ability on": (25, 30),
            "activated a black hole around": (40, 50),
            "performed a divine judgment on": (50, 60),
            "threw a comet at": (45, 55),
            "struck with a cosmic blast": (40, 50),
            "used a dimension-warping technique on": (30, 40),
            "activated a supernova around": (50, 60),
            "threw a kitten at": (2, 5),
            "tickled with a feather": (1, 3),
            "threw a water balloon at": (3, 7),
            "summoned a swarm of butterflies to distract": (2, 5),
            "cast a confetti explosion at": (5, 10),
            "used a rubber chicken slap on": (3, 6),
            "performed a dance-off against": (5, 8),
            "threw a pillow at": (2, 4),
            "summoned a rain of marshmallows on": (4, 8),
            "struck with a rubber band snap": (2, 5),
            "used a tickle machine on": (4, 7),
            "activated a bubble shield around": (6, 10),
            "performed a silly string attack on": (3, 6),
            "threw a rubber duck at": (4, 7),
            "summoned a cloud of glitter to blind": (5, 9),
            "struck with a foam sword": (3, 6),
            "used a whoopee cushion blast on": (5, 8),
            "activated a confetti cannon around": (7, 12),
            "performed a balloon animal distraction on": (4, 8),
            "threw a cupcake at": (3, 6),
            "summoned a swarm of ladybugs to annoy": (2, 4),
            "struck with a pillow fight attack": (4, 7),
            "used a bubble machine on": (6, 10),
            "activated a party popper surprise around": (8, 12),
            "performed a marshmallow launcher attack on": (5, 9),
            "threw a rubber chicken at": (3, 6),
            "summoned a rain of confetti on": (4, 8),
            "struck with a silly spring-loaded boxing glove": (5, 9),
            "used a glitter bomb on": (7, 12),
            "activated a foam party around": (6, 10),
            "performed a whoopee cushion shockwave on": (8, 12),
            "threw a party hat at": (4, 7),
            "summoned a swarm of party balloons to lift": (3, 6),
            "struck with a streamer whip": (5, 9),
            "used a party horn blast on": (7, 12),
            "activated a disco ball distraction around": (6, 10),
            "performed a confetti shower attack on": (8, 12),
            "threw a cake at": (5, 9),
            "summoned a rain of bubbles on": (4, 7),
            "struck with a pinata smash": (6, 10),
            "used a dance floor trap on": (8, 12),
            "activated a laser light show around": (7, 12),
            "performed a balloon animal army attack on": (9, 15),
            "threw a party popper at": (6, 10),
            "summoned a swarm of party streamers to entangle": (5, 9),
            "struck with a confetti cannon blast": (7, 12),
            "used a disco ball dazzle on": (9, 15),
            "activated a fireworks display around": (8, 12),
            "performed a pinata explosion attack on": (10, 15),
            "threw a party favor at": (7, 12),
            "summoned a rain of glow sticks on": (6, 10),
            "struck with a party horn shockwave": (8, 12),
            "used a balloon drop on": (10, 15),
            "activated a party lights show around": (9, 15),
            "performed a confetti storm attack on": (11, 18),
            "threw a cake pop at": (8, 12),
            "summoned a swarm of party hats to confuse": (7, 10),
            "struck with a pinata burst": (9, 15),
            "used a dance-off distraction on": (11, 18),
            "activated a laser show around": (10, 15),
            "performed a balloon animal stampede on": (12, 20),
            "threw a party whistle at": (9, 15),
            "summoned a rain of glow necklaces on": (8, 12),
            "struck with a party popper explosion": (10, 15),
            "used a disco ball spin on": (12, 20),
            "activated a confetti blizzard around": (11, 18),
            "performed a pinata surprise attack on": (13, 22),
            "threw a party streamer at": (10, 15),
            "summoned a swarm of party confetti to disorient": (9, 13),
            "struck with a party horn blast": (11, 18),
            "used a balloon barrage on": (13, 22),
            "activated a party fog around": (12, 20),
            "performed a party lights dazzle attack on": (14, 25),
            "threw a cupcake cannon at": (11, 18),
            "summoned a rain of party favors on": (10, 15),
            "struck with a pinata blast": (12, 20),
            "used a dance floor quake on": (14, 25),
            "activated a laser light extravaganza around": (13, 22),
            "performed a balloon animal army invasion on": (15, 30),
            "threw a party confetti bomb at": (12, 20),
            "summoned a swarm of party balloons to lift and carry away": (11, 18),
            "struck with a confetti cannon explosion": (13, 22),
            "activated a fireworks grand finale around": (14, 25),
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
    time.sleep(3)

print("The winner is:", [c.name for c in characters if c.is_alive()][0])