import random
from combat import Combat

COLORS = ['yellow', 'red', 'blue', 'green']


class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points,self.max_hit_points)
        self.experiece = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def battlecry(self):
        return self.sound.upper()

    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hit_points,
                                              self.experiece)


class Goblin(Monster):
    max_hit_points = 3
    max_experience = 2
    sound = 'squeak'


class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 4
    max_experience = 7
    sound = 'troll'

class Dragon(Monster):
    min_hit_points = 30
    max_hit_points = 50
    min_experience = 40
    max_experience = 70
    sound = 'drlll'
