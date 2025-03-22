import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")
        print(f"У {other.name} осталось {max(0, other.health)} здоровья.\n")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра начинается!\n")
        round_number = 1

        while self.player.is_alive() and self.computer.is_alive():
            print(f"Раунд {round_number}:")

            # Ход игрока
            if self.player.is_alive():
                self.player.attack(self.computer)

            # Ход компьютера
            if self.computer.is_alive():
                self.computer.attack(self.player)

            round_number += 1

        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")

# Пример использования
game = Game("Игрок", "Компьютер")
game.start()
