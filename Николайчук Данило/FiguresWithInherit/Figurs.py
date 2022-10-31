from abc import ABC, abstractmethod

from Colors import *

import time

import turtle

from turtle import *

from DifferentExceptions import DifferentError


class Figur(ABC):

    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
