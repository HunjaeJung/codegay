from character import Character
from monster import Dragon, Goblin, Troll
import sys


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        self.monster.battlecry()
        if self.monster.attack():
            print "{} is trying to attack!".format(self.monster)
            if raw_input("dodge?(y/n): ").lower() == 'y':
                if self.player.dodge():
                    print "dodge was successful"
                else:
                    self.player.hit_points -= 1
                    print "you're attacked!"
            else:
                print "{} hit you for 1 point!".format(self.monster)
                self.player.hit_points -= 1
        else:
            print "{} is not attacking now".format(self.monster)

    def player_turn(self):
        behavior = raw_input("[a]ttack/[r]est/[q]uit").lower()

        if behavior in 'arq':
            if behavior == 'a':
                print "You're attacking {}".format(self.monster)
                if self.player.attack():
                    if self.monster.dodge():
                        print "{} dodge".format(self.monster)
                    else:
                        if self.player.leveled_up():
                            self.monster.hit_points -= 2
                        else:
                            self.monster.hit_points -= 1

                        print "You hit {} with your {}".format(self.monster,
                                                               self.player.weapon)
                else:
                    print "not a good attack"
            elif behavior == 'r':
                self.player.rest()
            else:
                sys.exit()
        else:
            return self.player_turn()

    def cleanup(self):
        #let's tackle that!
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experiece
            print "You killed {}, and got {}. now you {}".format(self.monster,
                                                      self.monster.experiece,
                                                      self.player.experience)
            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            print '\n'+'='*20
            print self.player
            self.monster_turn()
            print '-'*20
            self.player_turn()
            print '\n'+'='*20
            self.cleanup()

        if self.player.hit_points:
            print "You win!"
        elif self.monsters or self.monster:
            print "You lose!"

        sys.exit()


Game()
