# Frog game

class Frog:
    """
    创建青蛙世界游戏
    """

    def __init__(self, name):
        """
        主角名字复制
        :param name:
        """
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        """
        :param obstacle:
        用来描述青蛙和障碍物的交互
        """

        act = obstacle.action()
        msg = f'{self} the Frog encounters {obstacle} and {act}!'
        print(msg)


class Bug:
    """
    虫子类
    """

    def __str__(self):
        return 'a bug'

    def action(self):
        """
        青蛙支持一种行为吃掉虫子
        :return:
        """
        return 'eats it'


class FrogWorld:
    """
    抽象工厂，主要作用是创建游戏中的主角和障碍物
    """

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Frog World -------'

    def make_character(self):
        """
        创建青蛙主角
        :return:
        """
        return Frog(self.player_name)

    def make_obstacle(self):
        """
        创建青蛙遇到的障碍物虫子
        :return:
        """
        return Bug()


# Wizard game

class Wizard:
    """
    创建巫师的游戏
    """

    def __init__(self, name):
        """
        定义游戏主角的名字
        :param name:
        """
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        """
        定义游戏主角的行为，和兽人战斗
        :param obstacle:
        :return:
        """
        act = obstacle.action()
        msg = f'{self} the Wizard battles against {obstacle} and {act}!'
        print(msg)


class Ork:
    """
    兽人
    """

    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld:
    """
    巫师世界的抽象工厂
    """

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard World -------'

    def make_character(self):
        """
        初始化游戏主角
        :return:
        """
        return Wizard(self.player_name)

    def make_obstacle(self):
        """
        创建障碍物
        :return:
        """
        return Ork()


# Game environment
class GameEnvironment:
    """初始化游戏环境，即根据不同的工厂（根据条件来返回游戏的种类），采用不同的行动"""

    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input(f'Welcome {name}. How old are you? ')
        age = int(age)
    except ValueError as err:
        print(f"Age {age} is invalid, please try again...")
        return False, age
    return True, age


def main():
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
