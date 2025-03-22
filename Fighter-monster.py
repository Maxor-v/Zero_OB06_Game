# Исходные данные:
# - Есть класс `Fighter`, представляющий бойца.
# - Есть класс `Monster`, представляющий монстра.
# - Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
# Шаг 1:Создайте абстрактный класс для оружия
# - Создайте абстрактный класс `Weapon`, который будет содержать абстрактный метод `attack()`.
# Шаг 2: Реализуйте конкретные типы оружия
# - Создайте несколько классов, унаследованных от `Weapon`, например, `Sword` и `Bow`. Каждый из этих классов реализует метод `attack()` своим уникальным способом.
# Шаг 3: Модифицируйте класс `Fighter`
# - Добавьте в класс `Fighter` поле, которое будет хранить объект класса `Weapon`.
# - Добавьте метод `change_weapon()`, который позволяет изменить оружие бойца.
# Шаг 4: Реализация боя
# - Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
# Требования к заданию:
# - Код должен быть написан на Python.
# - Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
# - Программа должна выводить результат боя в консоль.
#
# Пример результата:
# Боец выбирает меч.
# Боец наносит удар мечом.
# Монстр побежден!
# Боец выбирает лук.
# Боец наносит удар из лука.
# Монстр побежден!

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def __init__(self):
        self.name = "меч"

    def attack(self):
        print("Боец наносит удар мечом.")


class Bow(Weapon):
    def __init__(self):
        self.name = "лук"

    def attack(self):
        print("Боец стреляет из лука.")

class Monster:
    def __init__(self):
        self.rip = False

    def kill_monster(self):
        self.rip = True
        print("Монстр побежден!")

class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon
        print(f"Боец выбирает {self.weapon.name}.")

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"\nБоец выбирает {self.weapon.name}.")

    def attack(self, monster: Monster):
        self.weapon.attack()
        monster.kill_monster()

# Демонстрация работы
if __name__ == "__main__":
    # Создаем оружие
    sword = Sword()
    bow = Bow()

    fighter = Fighter(sword)
    monster = Monster()
    fighter.attack(monster)

    # Меняем оружие на лук
    monster = Monster()
    fighter.change_weapon(bow)
    fighter.attack(monster)

    # Добавляем новое оружие
    class Gun(Weapon):
        def __init__(self):
            self.name = "пистолет"

        def attack(self):
            print("Боец стреляет из волыны.")


    # Используем новое оружие
    monster = Monster()
    fighter.change_weapon(Gun())
    fighter.attack(monster)