from enum import Enum
from random import randint, choice


class SuperAbility(Enum):
    explosion = 1
    CRITICAL_DAMAGE = 2
    BOOST = 3
    BLOCK_DAMAGE_REVERT = 4
    REBORN = 5
    HEAL = 6

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__damage = damage
        self.__health = health

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return (f'{self.__name} health: {self.__health} '
                f'damage: {self.__damage}')


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self):
        self.__defence = choice([e for e in SuperAbility])


    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if (hero.ability == SuperAbility.BLOCK_DAMAGE_REVERT and
                        self.defence != SuperAbility.BLOCK_DAMAGE_REVERT):
                    coef = randint(1, 2)
                    hero.blocked_damage = int(self.damage / (coef * 5))
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return (f'BOSS ' + super().__str__()
                + f' defence: {self.__defence}')


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coef = randint(2,5)
        boss.health -= self.damage * coef
        print(f'Warrior {self.name} '
              f'hit critically {self.damage * coef}')


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.BLOCK_DAMAGE_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted {self.blocked_damage}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage,
                         SuperAbility.HEAL)
        self.__heal_points = heal_points

    @property
    def heal_points(self):
        return self.__heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Witcher(Hero):
    def __init__(self, name, health, damage=0,):
        super().__init__(name, health, damage, SuperAbility.REBORN)

    def apply_super_power(self, boss, heroes):
        choice_hero = [hero for hero in heroes if hero.health == 0 ]
        chance = randint(1,5)
        if chance == 1 and choice_hero:
            reborn_hero = choice(choice_hero)
            reborn_hero.health = self.health
            self.health = 0
            print(f'{self.name} is sacrifice himself to reborn {reborn_hero.name}')

class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)


    def apply_super_power(self, boss, heroes):
        global  round_number
        for hero in heroes:
            if hero.health > 0 and round_number > 0 :
                hero.damage += 10


class Samurai(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        shurikens = randint(1,2)
        virus = 25
        heal = 15
        if shurikens == 1 :
            boss.health -= virus
            print('Virus actived')
        elif shurikens == 2 :
            boss.health += heal
            print(f'Oops, + {heal} health Boss')



round_number = 0


def start_game():
    boss = Boss('Tanos', 6000, 50)

    warrior_1 = Warrior('Ahiles', 280, 20)
    warrior_2 = Warrior('Sponge Bob', 270, 10)
    magic = Magic('Hendolf', 200, 20)
    berserk = Berserk('Gatz', 220, 30)
    doc = Medic('Haus', 250, 5, 15)
    junior = Medic('Zolo', 290, 5, 5)
    antivirus = Witcher('Salazar', 230,)
    wizzard = Magic('Socket', 250, 10)
    ronin = Samurai('kido', 270, 20)

    heroes_list = [warrior_1, warrior_2, magic, berserk, doc, junior, antivirus, wizzard, ronin]
    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_raound(boss, heroes_list)

def play_raound(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence()
    boss.attack(heroes)
    for hero in heroes:
        if (boss.defence != hero.ability and hero.health > 0 and boss.health > 0):
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)

def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def show_statistics(boss, heroes):
    print(f'ROUND: {round_number} ----------')
    print(boss)
    for hero in heroes:
        print(hero)

start_game()