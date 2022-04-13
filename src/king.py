import numpy as np
from colorama import Fore, Back, Style 
from os import system
import random
from time import sleep,time

from src.base import *
from src.input import *
from src.buildings import *

class King():
    def __init__(self,x ,y, ihpts):
        self.x = x
        self.y = y
        self.bg_pixel = Back.MAGENTA + ' ' + Style.RESET_ALL
        self.width = 3
        self.height = 2
        self.damage = 5
        self.speed = 1
        self.ihpts = ihpts
        self.hpts = ihpts
        self.alive = True
        self.clr_key = 'x'
        self.dist_th = -1
        self.dist_hut = [0,0,0,0,0]
        self.dist_cannon = [0,0,0,0]
        self.dist_tower = [0,0,0,0]
        self.dist_wall = [None] * 100
        self.dist_th_eu = -1
        self.dist_hut_eu = [0,0,0,0,0]
        self.dist_cannon_eu = [0,0,0,0]
        self.dist_tower_eu = [0,0,0,0]
        self.dist_wall_eu = [None] * 100

    def get_coordinates(self):
        return self.x, self.y

    def reduce_health(self, damage):
        self.hpts -= damage
        if self.hpts <= 0:
            self.alive = False
            self.hpts = 0
    
    def colour(self):
        if(self.alive == False):
            self.bg_pixel = Back.LIGHTBLACK_EX + ' ' + Style.RESET_ALL
            return
        if(self.clr_key == ' '):
            self.bg_pixel = Back.RED + ' ' + Style.RESET_ALL
            return
        if(self.clr_key == 'l'):
            self.bg_pixel = Back.BLUE + ' ' + Style.RESET_ALL
            return
        else:
            self.bg_pixel = Back.MAGENTA + ' ' + Style.RESET_ALL
        # if self.hpts >= self.ihpts//2:
        #     self.bg_pixel = Back.MAGENTA+' '+Style.RESET_ALL
        # elif self.hpts >= self.ihpts//5:
        #     self.bg_pixel = Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL
        # else:
        #     self.bg_pixel = Back.LIGHTCYAN_EX+' '+Style.RESET_ALL

    def move(self, key, speed):
        if(self.alive):
            if(key == 'w'):
                self.y -= int(speed)
                if(self.y < 0):
                    self.y = 0
            elif(key == 's'):
                self.y += int(speed)
                if(self.y + self.height > 50):
                    self.y -= int(speed) 
            elif(key == 'a'):
                self.x -= int(speed)
                if(self.x < 0):
                    self.x = 0
            elif(key == 'd'):
                self.x += int(speed) 
                if(self.x + self.width > 100):
                    self.x -= int(speed)
    
    def retrace(self,key, speed):
        if(key == 'w'):
            self.y += speed
        elif(key == 's'):
            self.y -= speed
        elif(key == 'a'):
            self.x += speed
        elif(key == 'd'):
            self.x -= speed
