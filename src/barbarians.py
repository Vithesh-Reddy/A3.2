import numpy as np
from colorama import Fore, Back, Style 
from os import system
import math
import random
from time import sleep,time

class Barbarian():
    def __init__(self,x ,y, ihpts):
        self.x = x
        self.y = y
        self.bg_pixel = Back.RED + ' ' + Style.RESET_ALL
        self.width = 1
        self.height = 1
        self.damage = 3
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
        self.curr_building = None
        self.curr_building_dist = 100
        self.pbarb = False
    
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
        if self.hpts >= self.ihpts//2:
            self.bg_pixel = Back.RED+' '+Style.RESET_ALL
        elif self.hpts >= self.ihpts//5:
            self.bg_pixel = Back.LIGHTRED_EX+' '+Style.RESET_ALL
        else:
            self.bg_pixel = Back.LIGHTYELLOW_EX+' '+Style.RESET_ALL
    
    def move(self, x, y):
        cx = 0
        cy = 0
        if(y > self.y):
            self.y += int(self.speed)
            cy = int(self.speed)
            if(self.y > 49):
                self.y = 49
        elif(y < self.y):
            self.y -= int(self.speed)
            cy = -int(self.speed)
            if(self.y < 0):
                self.y = 0
        if(x > self.x):
            self.x += int(self.speed)
            cx = int(self.speed)
            if(self.x > 99):
                self.x = 99
        elif(x < self.x):
            self.x -= int(self.speed)
            cx = -int(self.speed)
            if(self.x < 0):
                self.x = 0
        return [cx, cy]
    
    def retrace(self,steps):
        if(steps[1] > 0):
            self.y -= steps[1]
            if(self.y < 0):
                self.y = 0
        elif(steps[1] < 0):
            self.y += -steps[1]
            if(self.y > 49):
                self.y = 49
        if(steps[0] > 0):
            self.x -= steps[0]
            if(self.x < 0):
                self.x = 0
        elif(steps[0] < 0):
            self.x += -steps[0]
            if(self.x > 99):
                self.x = 99