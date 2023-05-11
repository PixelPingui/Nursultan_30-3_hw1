class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def print_name(self):
        print(self.name)

    def double_health_points(self):
        self.health_points *= 2

    def __str__(self):
        return f"{self.nickname} has {self.superpower} and {self.health_points} health points"

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Clark Kent', 'Superman', 'super strength', 100, 'Up, up, and away!')
hero.print_name()  # выводит 'Clark Kent'
hero.double_health_points()  # удваивает здоровье героя
print(hero)  # выводит 'Superman has super strength and 200 health points'
print(len(hero))  # выводит длину коронной фразы героя


