import numpy as np
from colorama import Fore, Back, Style 
from os import system
import random
from time import sleep,time
import math

from src.input import *
from src.buildings import *
from src.base import *
from src.king import *

class Utils():
    def convert_to_euclid(self, xd, yd):
        return math.sqrt(xd**2 + yd**2)
        
    
