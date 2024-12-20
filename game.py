import random

class Character:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def attack(self, other):
        damage = random.randint(self.weapon["min_damage"], self.weapon["max_damage"])
        other.health -= damage
        other.health = max(0, other.health) 
        print(f"{self.name} атакует {other.name} с {self.weapon['name']} наносит {damage} урон")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} исцелен  на {amount} очков")

    def is_alive(self):
        return self.health > 0

gnome = Character("Gnome", 150, {"name": "Hammer", "min_damage": 10, "max_damage": 20})
elf = Character("Elf", 120, {"name": "Bow", "min_damage": 15, "max_damage": 25})
human = Character("Human", 200, {"name": "Sword", "min_damage": 20, "max_damage": 30})
goblin = Character("Goblin", 100, {"name": "Dagger", "min_damage": 5, "max_damage": 15})

characters = [gnome, elf, human, goblin]

def random_healing():
    healer = random.choice(characters)
    healer.heal(100)
    print(f"Бог боголсовил {healer.name} и исцелил на 100 очков")

def fight_round(attacker, defender):
    if attacker.is_alive() and defender.is_alive():
        attacker.attack(defender)
        print(f"{attacker.name} жизни : {attacker.health}, {defender.name}жизни : {defender.health}\n")

def main_game():
    round_counter = 0
    while len([c for c in characters if c.is_alive()]) > 1:
        round_counter += 1
        print(f"Раунд {round_counter}")
        attacker, defender = random.sample([c for c in characters if c.is_alive()], 2)
        fight_round(attacker, defender)

        if round_counter % 5 == 0:
            random_healing()

    winner = next((c for c in characters if c.is_alive()), None)
    if winner:
        print(f"Победитеть {winner.name} с отрывом {winner.health} жизни")
    else:
        print("Оба погибли, ничья")

if __name__ == "__main__":
    main_game()
    
    
