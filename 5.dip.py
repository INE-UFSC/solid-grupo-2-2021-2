"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""
from abc import abstractmethod


class IStatsReporter():
    @abstractmethod
    def report():
        pass


class IPlayer():
    @abstractmethod
    def name():
        pass

    @abstractmethod
    def hp():
        pass


class StatsReporter(IStatsReporter):
    def __init__(self, char: IPlayer):
        if isinstance(char, IPlayer):
            self.char = char

    def report(self):
        if self.char != None:
            print(f'Name:{self.char.name()}')
            print(f'HP:{self.char.hp()}')


class Player(IPlayer):
    def __init__(self, name):
        self.__reporter = StatsReporter(self)
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

    def stats(self):
        self.__reporter.report()
