"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""


class IDatabase:
    def save(self, animal):
        pass


class DatabaseSQL(IDatabase):
    def save(self, animal):
        pass


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass
