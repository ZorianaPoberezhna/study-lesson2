import random
import json
from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name: str):
        self._name = name
        self._attack = 10
        self._defence = 5
        self._health = 100
        self._level = 1
        self._exp = 0
        self._crit_chance = 0.1
        self._crit_damage = 1.5
        self._inventory = Inventory()
        self._equipped_items = []

    @abstractmethod
    def base_starts(self):
        pass

    @property
    def name(self):
        return self._name

    @property
    def attack(self):
        return self._attack + sum(item.attack_bonus for item in self._equipped_items)

    @property
    def defence(self):
        return self._defence + sum(item.defence_bonus for item in self._equipped_items)

    @property
    def health(self):
        return self._health

    def receive_damage(self, damage: float):
        reduced_damage = max(damage - self.defence, 0)
        self._health -= reduced_damage
        if self._health <= 0:
            print(f"{self._name} was defeated")
            return False
        return True

    def attack_target(self, target):
        is_critical = random.random() < self._crit_chance
        damage = self.attack * (self._crit_damage if is_critical else 1)
        print(f"{self._name} attacks {target.name} for {damage} damage!")
        target.receive_damage(damage)

    def gain_exp(self, amount: int):
        self._exp += amount
        if self._exp >= 100 * self._level:
            self.level_up()

    def level_up(self):
        self._level += 1
        self._attack += 5
        self._defence += 2
        self._health += 20
        self._exp += 0
        print(f"{self._name} leveled up to level {self._level}!")

    def to_dict(self):
        return {
            'name': self._name,
            'attack': self._attack,
            'defence': self._defence,
            'health': self._health,
            'level': self._level,
            'exp': self._exp,
            'crit_chance': self._crit_chance,
            'crit_damage': self._crit_damage,
        }

    @classmethod
    def from_dict(cls, data):
        char = cls(data['name'])
        char._attack = data['attack']
        char._defence = data['defence']
        char._health = data['health']
        char._level = data['level']
        char._exp = data['exp']
        char._crit_chance = data['crit_chance']
        char._crit_damage = data['crit_damage']
        return char

class Warrior(Character):
    def base_starts(self):
        self._attack = 15
        self._defence = 10
        self._health = 120

class Mage(Character):
    def base_starts(self):
        self._attack = 20
        self._defence = 5
        self._health = 80

class Rogue(Character):
    def base_starts(self):
        self._attack = 12
        self._defence = 7
        self._health = 90

class Paladin(Character):
    def base_starts(self):
        self._attack = 10
        self._defence = 12
        self._health = 110

class Bot(Character):
    def __init__(self, level):
        super().__init__(f"Bot_Lv{level}")
        self._attack = random.randint(5, 10) + level
        self._defence = random.randint(3, 7) + level
        self._health + random.randint(50, 100) + level * 10

    def base_starts(self):
        pass

    def to_dict(self):
        return {
            'name': self._name,
            'attack': self._attack,
            'defence': self._defence,
            'health': self._health,
            'level': self._level
        }

class Item:
    def __init__(self, name: str, attack_bonus: int = 0, defence_bonus: int = 0, health_bonus: int = 0):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defence_bonus = defence_bonus
        self.health_bonus = health_bonus

class Inventory:
    def __init__(self):
        self.items = []

    def add_items(self, item: Item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(f"Item: {item.name} - Attack: {item.attack_bonus}, "
                  f"Defence: {item.defence_bonus}, Health: {item.health_bonus}")


class Game:
    def __init__(self):
        self.characters = []
        self.bots = []

    def add_character(self, character: Character):
        self.characters.append(character)

    def add_bot(self, bot: Bot):
        self.bots.append(bot)

    def battle(self, char1: Character, char2: Character):
        print(f"Battle started between {char1.name} and {char2.name}")
        while char1.health > 0 and char2.health > 0:
            char1.attack_target(char2)
            if char2.health > 0:
                char2.attack_target(char1)
        winner = char1 if char1.health > 0 else char2
        print(f"{winner.name} wins!")
        winner.gain_exp(50)

    def enter_forest(self, player: Character):
        while True:
            bot = Bot(level=player._level)
            print(f"Encountered {bot.name} in the forest!")
            self.battle(player, bot)

            command = input("Continue fighting or stop? (fight/stop): ").lower()
            if command == 'stop':
                break

    def save_game(self, filename="data.json"):
        game_data = {
            'characters': [char.to_dict() for char in self.characters]
        }
        with open(filename, 'w') as file:
            json.dump(game_data, file)
        print(f"Game saved to {filename}")

    def load_game(self, filename="data.json"):
        try:
            with open(filename, 'r') as file:
                game_data = json.load(file)
                self.characters = [Warrior.from_dict(data) for data in game_data['characters']]
                print(f"Game loaded from {filename}")
        except FileNotFoundError:
            print("Save file not found.")


warrior = Warrior("Conan")
mage = Mage("Merlin")
warrior.base_starts()
mage.base_starts()

game = Game()
game.add_character(warrior)
game.add_character(mage)


game.save_game()

game.battle(warrior, mage)