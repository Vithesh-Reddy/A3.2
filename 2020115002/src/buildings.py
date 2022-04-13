import numpy as np
from colorama import Fore, Back, Style 
from os import system
import random
from time import sleep,time


class Building():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = -1
        self.width = -1
        self.hpts = -1
        self.alive = True
        self. walls = []

    def reduce_health(self, damage):
        self.hpts -= damage
        if self.hpts <= 0:
            self.alive = False
            self.hpts = 0

class Th(Building):
    def __init__(self, x, y, ihpts):
        super().__init__(x, y)
        self.bg_pixel = Back.GREEN+' '+Style.RESET_ALL
        self.height = 3
        self.width = 4
        self.ihpts = ihpts
        self.hpts = ihpts
        # self.dist_king = -1
        # self.dist_barbs = [None] * 25
    
    def colour(self):
        # if(self.clr_key == ' '):
        #     self.bg_pixel = Back.RED + ' ' + Style.RESET_ALL
        #     return
        if(self.alive == False):
            self.bg_pixel = Back.BLACK + ' ' + Style.RESET_ALL
            return
        if self.hpts >= self.ihpts//2:
            self.bg_pixel = Back.GREEN+' '+Style.RESET_ALL
        elif self.hpts >= self.ihpts//5:
            self.bg_pixel = Back.YELLOW+' '+Style.RESET_ALL
        else:
            self.bg_pixel = Back.LIGHTRED_EX+' '+Style.RESET_ALL

class Hut(Building):
    def __init__(self, x, y, ihpts):
        super().__init__(x, y)
        self.bg_pixel = Back.GREEN+' '+Style.RESET_ALL
        self.height = 1
        self.width = 1
        self.count = 5
        self.ihpts = ihpts
        self.hpts = ihpts
    
    def colour(self):
        # if(self.clr_key == ' '):
        #     self.bg_pixel = Back.LIGHTCYAN_EX + ' ' + Style.RESET_ALL
        #     return
        if(self.alive == False):
            self.bg_pixel = Back.BLACK + ' ' + Style.RESET_ALL
            return
        if self.hpts >= self.ihpts//2:
            self.bg_pixel = Back.GREEN+' '+Style.RESET_ALL
        elif self.hpts >= self.ihpts//5:
            self.bg_pixel = Back.YELLOW+' '+Style.RESET_ALL
        else:
            self.bg_pixel = Back.LIGHTRED_EX+' '+Style.RESET_ALL

class Cannon(Building):
    def __init__(self, x, y, ihpts):
        super().__init__(x, y)
        self.bg_pixel = Back.BLUE+' '+Style.RESET_ALL
        self.height = 1
        self.width = 2
        self.count = 4
        self.ihpts = ihpts
        self.hpts = ihpts
        self.damage = 10
        self.clr_key = 'x'
        self.curr_troop = None
        self.range = 10
    
    def colour(self):
        if(self.clr_key == 'a'):
            self.bg_pixel = Back.WHITE + ' ' + Style.RESET_ALL
            return
        if(self.alive == False):
            self.bg_pixel = Back.BLACK + ' ' + Style.RESET_ALL
            return
        if self.hpts >= self.ihpts//2:
            self.bg_pixel = Back.GREEN+' '+Style.RESET_ALL
        elif self.hpts >= self.ihpts//5:
            self.bg_pixel = Back.YELLOW+' '+Style.RESET_ALL
        else:
            self.bg_pixel = Back.LIGHTRED_EX+' '+Style.RESET_ALL
    
class Wall(Building):
    def __init__(self, x, y, ihpts):
        super().__init__(x, y)
        self.bg_pixel = Back.CYAN + ' ' + Style.RESET_ALL
        self.height = 1
        self.width = 1
        self.ihpts = ihpts
        self.hpts = ihpts
    
class Tower(Building):
    def __init__(self, x, y, ihpts):
        super().__init__(x, y)
        self.bg_pixel = Back.BLUE+' '+Style.RESET_ALL
        self.height = 2
        self.width = 2
        self.count = 4
        self.ihpts = ihpts
        self.hpts = ihpts
        self.damage = 10
        self.clr_key = 'x'
        self.curr_troop = None
        self.range = 10
    
    def colour(self):
        if(self.clr_key == 'a'):
            self.bg_pixel = Back.WHITE + ' ' + Style.RESET_ALL
            return
        if(self.alive == False):
            self.bg_pixel = Back.BLACK + ' ' + Style.RESET_ALL
            return
        if self.hpts >= self.ihpts//2:
            self.bg_pixel = Back.GREEN+' '+Style.RESET_ALL
        elif self.hpts >= self.ihpts//5:
            self.bg_pixel = Back.YELLOW+' '+Style.RESET_ALL
        else:
            self.bg_pixel = Back.LIGHTRED_EX+' '+Style.RESET_ALL