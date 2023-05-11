# Класс SuperHero
class SuperHero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def power_up(self):
        self.hp **= 2
        self.fly = True
        return f"{self.name} powered up! Fly in the {self.__class__.__name__}!"


class AirHero(SuperHero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage
        self.fly = False


class EarthHero(SuperHero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage
        self.fly = False


class SpaceHero(SuperHero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage
        self.fly = False


# Класс Villians
class Villain(SpaceHero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
        self.people = "monster"

    def gen_x(self):
        pass

    def crit(self, target):
        target.hp -= self.damage ** 2
        return f"{self.name} crit {target.name} for {self.damage ** 2} damage!"

hero1 = AirHero("Skyman", 100, 10)
hero2 = EarthHero("Rockman", 120, 12)
hero3 = SpaceHero("Starman", 150, 15)

villain1 = Villain("Mongol", 200, 20)
villain2 = Villain("Darkseid", 300, 30)

print(hero1.power_up())
print(hero2.power_up())
print(hero3.power_up())

print(villain1.crit(hero1))
print(villain2.crit(hero3))


