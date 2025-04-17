from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass

    def get_nome(self):
        return self.__nome

    def get_salario(self):
        return self.__salario
