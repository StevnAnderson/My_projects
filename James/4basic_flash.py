# imports
from random import randint as rand
import tkinter as TK

# variables
range_min = int()
range_max = int()
answers = []
operands_1 = []
operands_2 = []


# functions
def add():
    operands_1.append(rand(range_min, range_max))
    operands_2.append(rand(range_min, range_max))


# gui

