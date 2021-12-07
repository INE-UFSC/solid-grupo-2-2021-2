"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC


class IJanela(ABC):
    def fechar(self):
        raise NotImplementedError


class IJanelaTamanhoVariavel(IJanela):
    def maximizar(self):
        raise NotImplementedError

    def minimizar(self):
        raise NotImplementedError


class IJanelaComMenu(IJanela):
    def mostrar_menu(self):
        raise NotImplementedError


class JanelaTamanhoFixo(IJanelaComMenu):
    def mostrar_menu(self):
        pass

    def fechar(self):
        pass


class JanelaSemMenu(IJanelaTamanhoVariavel):
    def maximizar(self):
        pass

    def minimizar(self):
        pass

    def fechar(self):
        pass
