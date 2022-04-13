import numpy as np
from colorama import Fore, Back, Style 
from os import system
import random
from time import sleep,time

from src.king import *

class Spell():
    def __init__(self):
        pass

    def rage(self, troop):
        troop.damage = troop.damage * 2
        troop.speed = troop.speed * 2
    
    def derage(self, troop):
        troop.damage = troop.damage // 2
        troop.speed = troop.speed // 2
    
    def heal(self, troops):
        for troop in troops:
            troop.hpts = troop.hpts * 1.5
            if(troop.hpts > troop.ihpts):
                troop.hpts = troop.ihpts
    