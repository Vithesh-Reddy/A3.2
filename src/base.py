import numpy as np
from colorama import Fore, Back, Style 
import os
import os.path
from os import system
import math
import random
from time import sleep,time

from src.input import *
from src.buildings import *
from src.king import *
from src.queen import *
from src.barbarians import *
from src.archers import *
from src.balloons import *
from src.spells import *

class Base():
    def __init__(self):
        self.cols = 100
        self.rows = 50
        self.bg_pixel = Back.BLACK+' '+Style.RESET_ALL
        self.th = Th(45, 20, 300)
        self.hero = None
        self.hero_text = 'x'
        self.hut = Hut(0, 0, 20)
        self.huts = np.zeros(self.hut.count, dtype=Hut)
        self.cannon = Cannon(0, 0, 0)
        self.tower = Tower(0, 0, 0)
        self.cannons = [self.cannon, self.cannon,self.cannon, self.cannon]
        self.towers = [Tower(0,0,0), Tower(0,0,0), Tower(0,0,0), Tower(0,0,0)]
        self.wall = Wall(0,0,10)
        self.walls = np.zeros(1, dtype=Wall)
        self.spell = Spell()
        self.th_coordinates = []
        self.cannon_coordinates = []
        self.tower_coordinates = []
        self.hut_coordinates = []
        self.wall_coordinates = []
        self.barbs = []
        self.pbarbs = []
        self.archers = []
        self.balloons = []
        self.troops = []
        self.ground_troops = []
        self.air_troops = []
        self.buildings = [self.th]
        self.all_buildings = [self.th]
        self.defense_buildings = []
        self.start_time = time()
        self.current_time = time()
        self.def_start_time = -1
        self.tower_start_time = -1
        self.barb_start_time = -1
        self.archer_start_time = -1
        self.balloon_start_time = -1
        self.barb_timer = 0.5
        self.archer_timer = 0.25
        self.balloon_timer = 0.25
        # self.pbarb_timer = 0.5
        self.rage_ct = 0
        self.heal_ct = 0
        self.p_ct = 1
        self.hero_ct = 1
        self.barb_ct = 5
        self.archer_ct = 5
        self.balloon_ct = 3
        self.rage_start_time = time() + 1000
        self.heal_start_time = time() + 1000
        self.p_start_time = time() + 1000
        self.eagle_start_time = time() + 1000
        self.game_over = -1
        self.finished = False
        self.replay_number = 1
        self.file_path = ''
        self.level = 1

    def build_huts(self):
        self.huts[0] = Hut(0,0, 20)
        self.huts[1] = Hut(99,0, 20)
        self.huts[2] = Hut(0,49, 20)
        self.huts[3] = Hut(99,49, 20)
        self.huts[4] = Hut(0,25, 20)
        for hut in self.huts:
            self.buildings.append(hut)
            self.all_buildings.append(hut)

    def build_cannons(self):
        self.cannons[0] = Cannon(30,15, 50)
        self.cannons[1] = Cannon(55,30,50)
        self.cannons[2] = Cannon(65,15, 50)
        self.cannons[3] = Cannon(25,30,50)
        for cannon in self.cannons:
            self.buildings.append(cannon)
            self.defense_buildings.append(cannon)
            self.all_buildings.append(cannon)
    
    def build_towers(self):
        self.towers[0] = Tower(35,15, 50)
        self.towers[1] = Tower(50,30,50)
        self.towers[2] = Tower(60,15, 50)
        self.towers[3] = Tower(30,30,50)
        for tower in self.towers:
            self.buildings.append(tower)
            self.defense_buildings.append(tower)
            self.all_buildings.append(tower)    
    
    def build_walls(self):
        # walls around town hall
        self.walls[0] = Wall(45,19,10)
        self.walls = np.append(self.walls,[Wall(44,19,10)])
        self.walls = np.append(self.walls,[Wall(46,19,10)])
        self.walls = np.append(self.walls,[Wall(47,19,10)])
        self.walls = np.append(self.walls,[Wall(48,19,10)])
        self.walls = np.append(self.walls,[Wall(49,19,10)])
        self.walls = np.append(self.walls,[Wall(45,23,10)])
        self.walls = np.append(self.walls,[Wall(46,23,10)])
        self.walls = np.append(self.walls,[Wall(47,23,10)])
        self.walls = np.append(self.walls,[Wall(48,23,10)])
        self.walls = np.append(self.walls,[Wall(44,20,10)])
        self.walls = np.append(self.walls,[Wall(44,21,10)])
        self.walls = np.append(self.walls,[Wall(44,22,10)])
        self.walls = np.append(self.walls,[Wall(44,23,10)])
        self.walls = np.append(self.walls,[Wall(49,20,10)])
        self.walls = np.append(self.walls,[Wall(49,21,10)])
        self.walls = np.append(self.walls,[Wall(49,22,10)])
        self.walls = np.append(self.walls,[Wall(49,23,10)])
        for i in range(self.walls.size):
            self.th.walls.append(self.walls[i])
            self.all_buildings.append(self.walls[i])

        # walls around cannons
        self.walls = np.append(self.walls,[Wall(29,14,10)])
        self.walls = np.append(self.walls,[Wall(30,14,10)])
        self.walls = np.append(self.walls,[Wall(31,14,10)])
        self.walls = np.append(self.walls,[Wall(32,14,10)])
        self.walls = np.append(self.walls,[Wall(29,16,10)])
        self.walls = np.append(self.walls,[Wall(30,16,10)])
        self.walls = np.append(self.walls,[Wall(31,16,10)])
        self.walls = np.append(self.walls,[Wall(32,16,10)])
        self.walls = np.append(self.walls,[Wall(29,15,10)])
        self.walls = np.append(self.walls,[Wall(32,15,10)])
        for i in range(len(self.th.walls), self.walls.size):
            self.cannons[0].walls.append(self.walls[i])
            self.all_buildings.append(self.walls[i])

        self.walls = np.append(self.walls,[Wall(54,29,10)])
        self.walls = np.append(self.walls,[Wall(55,29,10)])
        self.walls = np.append(self.walls,[Wall(56,29,10)])
        self.walls = np.append(self.walls,[Wall(57,29,10)])
        self.walls = np.append(self.walls,[Wall(54,31,10)])
        self.walls = np.append(self.walls,[Wall(55,31,10)])
        self.walls = np.append(self.walls,[Wall(56,31,10)])
        self.walls = np.append(self.walls,[Wall(57,31,10)])
        self.walls = np.append(self.walls,[Wall(54,30,10)])
        self.walls = np.append(self.walls,[Wall(57,30,10)])
        for i in range(len(self.th.walls) + len(self.cannons[0].walls), self.walls.size):
            self.cannons[1].walls.append(self.walls[i])
            self.all_buildings.append(self.walls[i])
        
    def store_th_coordinates(self):
        if(self.th.alive == True):
            for row in range(self.th.y, self.th.y+self.th.height):
                    for col in range(self.th.x, self.th.x+self.th.width):
                        self.th_coordinates.append([row,col])
    
    def store_cannon_coordinates(self):
        for i in range(self.cannon.count):
            cannon = self.cannons[i]
            if(cannon.alive == True):
                for row in range(cannon.y, cannon.y+cannon.height):
                        for col in range(cannon.x, cannon.x+cannon.width):
                            self.cannon_coordinates.append([row,col])
    
    def store_tower_coordinates(self):
        for i in range(self.tower.count):
            tower = self.towers[i]
            if(tower.alive == True):
                for row in range(tower.y, tower.y+tower.height):
                        for col in range(tower.x, tower.x+tower.width):
                            self.tower_coordinates.append([row,col])

    def store_hut_coordinates(self):
        for i in range(self.hut.count):
            hut = self.huts[i]
            if(hut.alive == True):
                for row in range(hut.y, hut.y+hut.height):
                        for col in range(hut.x, hut.x+hut.width):
                            self.hut_coordinates.append([row,col])

    def store_wall_coordinates(self):
        for i in range(self.walls.size):
            wall = self.walls[i]
            if(wall.alive == True):
                for row in range(wall.y, wall.y+wall.height):
                    for col in range(wall.x, wall.x+wall.width):
                        self.wall_coordinates.append([row,col])

    def calc_dist_th(self, troop):
        troop.dist_th = max(max(troop.x - (self.th.x+self.th.width), self.th.x - (troop.x+troop.width)), max(troop.y - (self.th.y+self.th.height), self.th.y - (troop.y+troop.height)))

    def calc_dist_cannon(self, troop):
        for i in range(self.cannon.count):
            cannon = self.cannons[i]
            troop.dist_cannon[i] = max(max(troop.x - (cannon.x+cannon.width), cannon.x - (troop.x+troop.width)), max(troop.y - (cannon.y+cannon.height), cannon.y - (troop.y+troop.height)))

    def calc_dist_tower(self, troop):
        for i in range(self.tower.count):
            tower = self.towers[i]
            troop.dist_tower[i] = max(max(troop.x - (tower.x+tower.width), tower.x - (troop.x+troop.width)), max(troop.y - (tower.y+tower.height), tower.y - (troop.y+troop.height)))

    def calc_dist_hut(self, troop):
        for i in range(self.hut.count):
            hut = self.huts[i]
            troop.dist_hut[i] = max(max(troop.x - (hut.x+hut.width), hut.x - (troop.x+troop.width)), max(troop.y - (hut.y+hut.height), hut.y - (troop.y+troop.height)))

    def calc_dist_wall(self, troop):
        for i in range(self.walls.size):
            wall = self.walls[i]
            if(wall.alive == True):
                troop.dist_wall[i] = max(max(troop.x - (wall.x+wall.width), wall.x - (troop.x+troop.width)), max(troop.y - (wall.y+wall.height), wall.y - (troop.y+troop.height)))

    def calc_dist_th_eu(self, troop):
        troop.dist_th_eu = math.sqrt((troop.x - self.th.x)**2 + (troop.y - self.th.y)**2)

    def calc_dist_cannon_eu(self, troop):
        for i in range(self.cannon.count):
            cannon = self.cannons[i]
            troop.dist_cannon_eu[i] = math.sqrt((troop.x - cannon.x)**2 + (troop.y - cannon.y)**2)

    def calc_dist_tower_eu(self, troop):
        for i in range(self.tower.count):
            tower = self.towers[i]
            troop.dist_tower_eu[i] = math.sqrt((troop.x - tower.x)**2 + (troop.y - tower.y)**2)


    def calc_dist_hut_eu(self, troop):
        for i in range(self.hut.count):
            hut = self.huts[i]
            troop.dist_hut_eu[i] = math.sqrt((troop.x - hut.x)**2 + (troop.y - hut.y)**2)

    def calc_dist_wall_eu(self, troop):
        for i in range(self.walls.size):
            wall = self.walls[i]
            if(wall.alive == True):
                troop.dist_wall_eu[i] = math.sqrt(max(troop.x - (wall.x+wall.width), wall.x - (troop.x+troop.width))**2 + max(troop.y - (wall.y+wall.height), wall.y - (troop.y+troop.height))**2)

    def check_level(self):
        if(self.level == 1):
            self.cannons[2].alive = False
            self.cannons[3].alive = False
            self.towers[2].alive = False
            self.towers[3].alive = False
        elif(self.level == 2):
            if(self.cannons[2].hpts!=0):
                self.cannons[2].alive = True
            self.cannons[3].alive = False
            if(self.towers[2].hpts!=0):
                self.towers[2].alive = True
            self.towers[3].alive = False
        elif(self.level == 3):
            if(self.cannons[2].hpts!=0):
                self.cannons[2].alive = True
            if(self.cannons[3].hpts!=0):
                self.cannons[3].alive = True
            if(self.towers[2].hpts!=0):
                self.towers[2].alive = True
            if(self.towers[3].hpts!=0):
                self.towers[3].alive = True

    def replay_file(self):
        self.file_path = './replays/replay_' + str(self.replay_number) + '.txt'
        if(os.path.exists(self.file_path) == True):
            self.replay_number += 1
            self.replay_file()

    def render(self):
        system('clear')
        self.base = [[self.bg_pixel for i in range(self.cols)] for j in range(self.rows)]

        print(self.th.hpts)

        # check level
        Base.check_level(self)

        # calculate distances of hero
        if(self.hero != None):
            Base.calc_dist_th(self, self.hero)
            Base.calc_dist_cannon(self, self.hero)
            Base.calc_dist_tower(self, self.hero)
            Base.calc_dist_hut(self, self.hero)
            Base.calc_dist_wall(self, self.hero)

            Base.calc_dist_th_eu(self, self.hero)
            Base.calc_dist_cannon_eu(self, self.hero)
            Base.calc_dist_tower_eu(self, self.hero)
            Base.calc_dist_hut_eu(self, self.hero)
            Base.calc_dist_wall_eu(self, self.hero)

        #calculate distances of barbs
        for i in range(len(self.barbs)):
            barb = self.barbs[i]
            Base.calc_dist_th(self, barb)
            Base.calc_dist_cannon(self, barb)
            Base.calc_dist_tower(self, barb)
            Base.calc_dist_hut(self, barb)
            Base.calc_dist_wall(self, barb)

            Base.calc_dist_th_eu(self, barb)
            Base.calc_dist_cannon_eu(self, barb)
            Base.calc_dist_tower_eu(self, barb)
            Base.calc_dist_hut_eu(self, barb)
            Base.calc_dist_wall_eu(self, barb)
        
        #calculate distances of archers
        for i in range(len(self.archers)):
            archer = self.archers[i]
            Base.calc_dist_th(self, archer)
            Base.calc_dist_cannon(self, archer)
            Base.calc_dist_tower(self, archer)
            Base.calc_dist_hut(self, archer)
            Base.calc_dist_wall(self, archer)

            Base.calc_dist_th_eu(self, archer)
            Base.calc_dist_cannon_eu(self, archer)
            Base.calc_dist_tower_eu(self, archer)
            Base.calc_dist_hut_eu(self, archer)
            Base.calc_dist_wall_eu(self, archer)
        
        #calculate distances of balloons
        for i in range(len(self.balloons)):
            balloon = self.balloons[i]
            Base.calc_dist_th(self, balloon)
            Base.calc_dist_cannon(self, balloon)
            Base.calc_dist_tower(self, balloon)
            Base.calc_dist_hut(self, balloon)
            Base.calc_dist_wall(self, balloon)

            Base.calc_dist_th_eu(self, balloon)
            Base.calc_dist_cannon_eu(self, balloon)
            Base.calc_dist_tower_eu(self, balloon)
            Base.calc_dist_hut_eu(self, balloon)
            Base.calc_dist_wall_eu(self, balloon)

        # store buildings coordinates
        self.th_coordinates = []
        Base.store_th_coordinates(self)
        self.cannon_coordinates = []
        Base.store_cannon_coordinates(self)
        self.tower_coordinates = []
        Base.store_tower_coordinates(self)
        self.hut_coordinates = []
        Base.store_hut_coordinates(self)
        self.wall_coordinates = []
        Base.store_wall_coordinates(self)
            
        # render town hall
        self.th.colour()
        if(self.th.alive == True):
            for row in range(self.th.y, self.th.y+self.th.height):
                for col in range(self.th.x, self.th.x+self.th.width):
                    self.base[row][col] = self.th.bg_pixel
        
        # render huts
        for i in range(self.hut.count):
            hut = self.huts[i]
            hut.colour()
            if(hut.alive == True):
                for row in range(hut.y, hut.y+hut.height):
                    for col in range(hut.x, hut.x+hut.width):
                        self.base[row][col] = hut.bg_pixel

        # render cannons
        if(time() - self.def_start_time >= 1):
                Base.defense(self)
                self.def_start_time = time()
    
        for i in range(self.cannon.count):
            cannon = self.cannons[i]
            cannon.colour()
            if(cannon.alive == True):
                for row in range(cannon.y, cannon.y+cannon.height):
                    for col in range(cannon.x, cannon.x+cannon.width):
                        self.base[row][col] = cannon.bg_pixel

        # render towers
        if(time() - self.tower_start_time >= 1):
                Base.tower_defense(self)
                self.tower_start_time = time()
    
        for i in range(self.tower.count):
            tower = self.towers[i]
            tower.colour()
            if(tower.alive == True):
                for row in range(tower.y, tower.y+tower.height):
                    for col in range(tower.x, tower.x+tower.width):
                        self.base[row][col] = tower.bg_pixel
        
        # render walls
        for i in range(self.walls.size):
            wall = self.walls[i]
            if(wall.alive == True):
                for row in range(wall.y, wall.y+wall.height):
                    for col in range(wall.x, wall.x+wall.width):
                        self.base[row][col] = wall.bg_pixel

        # render hero
        if(self.hero != None):
            self.hero.colour()
            for row in range(self.hero.y, self.hero.y+self.hero.height):
                for col in range(self.hero.x, self.hero.x+self.hero.width):
                    self.base[row][col] = self.hero.bg_pixel

        # render barbs
        if(time() - self.barb_start_time >= self.barb_timer):
                Base.barb_function(self)
                self.barb_start_time = time()
        
        for i in range(len(self.barbs)):
            barb = self.barbs[i]
            barb.colour()
            for row in range(barb.y, barb.y+barb.height):
                for col in range(barb.x, barb.x+barb.width):
                    self.base[row][col] = barb.bg_pixel
        
        # render archers
        if(time() - self.archer_start_time >= self.archer_timer):
                Base.archer_function(self)
                self.archer_start_time = time()
        
        for i in range(len(self.archers)):
            archer = self.archers[i]
            archer.colour()
            for row in range(archer.y, archer.y+archer.height):
                for col in range(archer.x, archer.x+archer.width):
                    self.base[row][col] = archer.bg_pixel
        
        # render balloons
        if(time() - self.balloon_start_time >= self.balloon_timer):
                Base.balloon_function(self)
                self.balloon_start_time = time()
        
        for i in range(len(self.balloons)):
            balloon = self.balloons[i]
            balloon.colour()
            for row in range(balloon.y, balloon.y+balloon.height):
                for col in range(balloon.x, balloon.x+balloon.width):
                    self.base[row][col] = balloon.bg_pixel
        
        # check game over
        Base.check_game_over(self)
        if(self.game_over != 0 and self.game_over != 1):
            self.current_time = time()

        # adding borders and game endings
        screen_height = 5
        wall = 1
        border_pixel = Back.CYAN+' '+Style.RESET_ALL

        self.output = [[border_pixel for i in range(self.cols+2*wall)] for j in range(screen_height+self.rows+2*wall)]

        title = "Clash of Clans"
        title_offset = (self.cols+wall-len(title)) // 2
        for j in range(0, len(title)):
            self.output[1][title_offset+j] = Back.CYAN+Fore.RED+title[j]+Style.RESET_ALL

        # add level display
        level_text = "Level: "+str(self.level)
        level_offset = self.cols - ((self.cols+wall-len(level_text)) // 8)
        for j in range(0, len(level_text)):
            self.output[3][level_offset+j] = Back.CYAN+Fore.RED+level_text[j]+Style.RESET_ALL


        # add health bar for king
        if(self.hero_text == 'king'):
            health_text = "King's Health:"
            hero = self.hero
        elif(self.hero_text == 'queen'):
            health_text = "Queen's Health:"
            hero = self.hero
        
        if(self.hero != None):
            health_text_offset = (self.cols+wall-len(health_text)) // 8
            for j in range(0, len(health_text)):
                self.output[3][health_text_offset+j] = Back.CYAN+Fore.RED+health_text[j]+Style.RESET_ALL

            bar_width = 15
            bar_height = 1
            bar_offset = (self.cols+wall-bar_width) // 8
            bar_pixel = ""
            if hero.hpts >= hero.ihpts//2:
                bar_pixel = Back.GREEN+' '+Style.RESET_ALL
            elif hero.hpts >= hero.ihpts//5:
                bar_pixel = Back.YELLOW+' '+Style.RESET_ALL
            else:
                bar_pixel = Back.RED+' '+Style.RESET_ALL   

            bar_tiles = hero.hpts // 10
            for i in range(bar_width):
                if(i < bar_tiles):
                    self.output[4][bar_offset+i] = bar_pixel
                else:
                    self.output[4][bar_offset+i] = Back.BLACK+' '+Style.RESET_ALL
        
        # copy self.base into self.output
        for j in range(0, self.rows):
            for i in range(0, self.cols):
                self.output[j+screen_height+wall][i+wall] = self.base[j][i]

        # game end
        if(self.game_over == 0 or self.game_over == 1):
            game_over_screen_height = 10
            game_over_screen_width = self.cols//2
            self.game_over_screen = [[border_pixel for i in range(game_over_screen_width)] for j in range(game_over_screen_height)]

            game_over_title = ''
            if(self.game_over == 1 and self.level == 1):
                game_over_title = 'Level 1 Cleared'
            elif(self.game_over == 1 and self.level == 2):
                game_over_title = 'Level 2 Cleared'
            elif(self.game_over == 1 and self.level == 3):
                self.finished = True
                game_over_title = 'Level 3 Cleared'
            else:
                game_over_title = 'Game Over!'
                self.finished = True
            
            game_over_offset = (game_over_screen_width-len(game_over_title)) // 2
            for j in range(0, len(game_over_title)):
                self.game_over_screen[1][game_over_offset+j] = Back.CYAN+Fore.RED+game_over_title[j]+Style.RESET_ALL

            result_text = ""
            if(self.game_over == 1):
                result_text = "VICTORY!"
            else:
                result_text = "DEFEAT!"

            result_text_offset = (game_over_screen_width-len(result_text)) // 2
            for j in range(0, len(result_text)):
                self.game_over_screen[4][result_text_offset+j] = Back.CYAN+Fore.RED+result_text[j]+Style.RESET_ALL
            
            time_taken = math.floor(self.current_time-self.start_time)
            time_taken_text = "Time Taken: {} seconds".format(time_taken)
            time_taken_offset = (game_over_screen_width-len(time_taken_text)) // 2
            for j in range(0, len(time_taken_text)):
                self.game_over_screen[6][time_taken_offset+j] = Back.CYAN+Fore.RED+time_taken_text[j]+Style.RESET_ALL


            height_offset = screen_height+((self.rows//2)-(game_over_screen_height//2)+1)
            width_offset = 2*wall+((self.cols//2)-(game_over_screen_width//2)) 
            for row in range(0, game_over_screen_height):
                for col in range(0, game_over_screen_width):
                    self.output[height_offset+row][width_offset+col] = self.game_over_screen[row][col]
        
        if(self.game_over == 1 and self.level < 3):
            self.hero = None
            self.hero_text = 'x'
            self.barbs = []
            self.pbarbs = []
            self.archers = []
            self.balloons = []
            self.troops = []
            self.ground_troops = []
            self.air_troops = []
            self.def_start_time = -1
            self.tower_start_time = -1
            self.barb_start_time = -1
            self.archer_start_time = -1
            self.balloon_start_time = -1
            self.rage_ct = 0
            self.heal_ct = 0
            self.p_ct = 1
            self.hero_ct = 1
            self.barb_ct = 5
            self.archer_ct = 5
            self.balloon_ct = 3
            self.rage_start_time = time() + 1000
            self.heal_start_time = time() + 1000
            self.p_start_time = time() + 1000
            self.start_time = self.current_time
            for building in self.all_buildings:
                building.alive = True
                building.hpts = building.ihpts
            
            self.level += 1
            self.game_over = 2
            


        print("\n".join(["".join(row) for row in self.output]))

        # implement replay
        text_file = open(self.file_path, "a")
        if os.stat(self.file_path).st_size != 0:
            text_file.write("\n")
        text_file.write("\n".join(["".join(row) for row in self.output]))
        text_file.close()

        return self.finished
        

    def check_restricted(self, troop):
        check = 0
        for row in range(troop.y, troop.y+troop.height):
            for col in range(troop.x, troop.x+troop.width):
                if([row, col] in self.th_coordinates or [row,col] in self.cannon_coordinates or [row,col] in self.tower_coordinates or [row,col] in self.hut_coordinates or [row,col] in self.wall_coordinates):
                    check = 1                        
        return check

    def attack(self, troop):
        if(self.th.alive == True):
            if(troop.dist_th == 0):
                self.th.reduce_health(troop.damage)
                return
        for i in range(self.cannon.count):
            if(self.cannons[i].alive == True):
                if(troop.dist_cannon[i] == 0):
                    self.cannons[i].reduce_health(troop.damage)
                    return
        for i in range(self.tower.count):
            if(self.towers[i].alive == True):
                if(troop.dist_tower[i] == 0):
                    self.towers[i].reduce_health(troop.damage)
                    return
        for i in range(self.hut.count):
            if(self.huts[i].alive == True):
                if(troop.dist_hut[i] == 0):
                    self.huts[i].reduce_health(troop.damage)
                    return
        for i in range(self.walls.size):
            if(self.walls[i].alive == True):
                if(troop.dist_wall[i] == 0):
                    self.walls[i].reduce_health(troop.damage)
                    return

    def queen_attack(self, queen):
        refp = [queen.x-queen.distance, queen.y]
        if(queen.prev_key == 'w'):
            refp = [queen.x, queen.y-queen.distance]
        elif(queen.prev_key == 's'):
            refp = [queen.x, queen.y+queen.distance]
        elif(queen.prev_key == 'a'):
            refp = [queen.x-queen.distance, queen.y]
        elif(queen.prev_key == 'd'):
            refp = [queen.x+queen.distance, queen.y]
    
        if(refp[0] < 0):
            refp[0] = 0
        elif(refp[0] > self.cols-1):
            refp[0] = self.cols-1
        if(refp[1] < 0):
            refp[1] = 0
        elif(refp[1] > self.rows-1):
            refp[1] = self.rows-1
        
        for building in self.all_buildings:
            if(building.alive == True):
                if(math.sqrt((refp[0]-building.x)**2 + (refp[1]-building.y)**2) < queen.aoe):
                    building.reduce_health(queen.damage)
                    
    def queen_arrow(self,queen):
        refp = [queen.x-16, queen.y]
        if(queen.prev_key == 'w'):
            refp = [queen.x, queen.y-16]
        elif(queen.prev_key == 's'):
            refp = [queen.x, queen.y+16]
        elif(queen.prev_key == 'a'):
            refp = [queen.x-16, queen.y]
        elif(queen.prev_key == 'd'):
            refp = [queen.x+16, queen.y]
    
        if(refp[0] < 0):
            refp[0] = 0
        elif(refp[0] > self.cols-1):
            refp[0] = self.cols-1
        if(refp[1] < 0):
            refp[1] = 0
        elif(refp[1] > self.rows-1):
            refp[1] = self.rows-1
        
        for building in self.all_buildings:
            if(building.alive == True):
                if(math.sqrt((refp[0]-building.x)**2 + (refp[1]-building.y)**2) < 9):
                    building.reduce_health(queen.damage)

    def axe(self, troop):
        if(self.th.alive == True):
            if(troop.dist_th_eu < 5):
                self.th.reduce_health(troop.damage)

        for i in range(self.cannon.count):
            if(self.cannons[i].alive == True):
                if(troop.dist_cannon_eu[i] < 5):
                    self.cannons[i].reduce_health(troop.damage)

        for i in range(self.tower.count):
            if(self.towers[i].alive == True):
                if(troop.dist_tower_eu[i] < 5):
                    self.towers[i].reduce_health(troop.damage)

        for i in range(self.hut.count):
            if(self.huts[i].alive == True):
                if(troop.dist_hut_eu[i] < 5):
                    self.huts[i].reduce_health(troop.damage)

        for i in range(self.walls.size):
            if(self.walls[i].alive == True):
                if(troop.dist_wall_eu[i] < 5):
                    self.walls[i].reduce_health(troop.damage)
        return

    def defense(self):
        for i in range (self.cannon.count):
            cannon = self.cannons[i]
            if(cannon.alive == True):
                final_d = 100
                troop = cannon.curr_troop
                if(troop == None):
                    for curr_troop in self.ground_troops:
                        d = curr_troop.dist_cannon_eu[i]
                        if(d < final_d):
                            final_d = d
                            troop = curr_troop
                else:
                    final_d = troop.dist_cannon_eu[i]
                
                if(final_d < cannon.range and troop.alive == True):
                    troop.reduce_health(cannon.damage)
                    cannon.clr_key = 'a'
                    cannon.curr_troop = troop
                else:
                    cannon.curr_troop = None
    
    def tower_defense(self):
        for i in range (self.tower.count):
            tower = self.towers[i]
            if(tower.alive == True):
                final_d = 100
                troop = tower.curr_troop
                if(troop == None):
                    for curr_troop in self.troops:
                        d = curr_troop.dist_tower_eu[i]
                        if(d < final_d):
                            final_d = d
                            troop = curr_troop
                else:
                    final_d = troop.dist_tower_eu[i]
                
                if(final_d < tower.range and troop.alive == True):
                    # troop.reduce_health(tower.damage)
                    tower.clr_key = 'a'
                    Base.tower_action(self, tower, troop)
                    tower.curr_troop = troop
                else:
                    tower.curr_troop = None
    
    def tower_action(self, tower, troop):
        refp = [troop.x, troop.y]
        for troop in self.troops:
            if(troop.alive == True):
                if(math.sqrt((refp[0]-troop.x)**2 + (refp[1]-troop.y)**2) < 3):
                    troop.reduce_health(tower.damage)
    
    def spawn(self, p, x, y):
        if(p == 'i'):
            barb = Barbarian(70,5,30)
            self.barbs.append(barb)
            self.troops.append(barb)
            self.ground_troops.append(barb)
        elif(p == 'j'):
            barb = Barbarian(70,40,30)
            self.barbs.append(barb)
            self.troops.append(barb)
            self.ground_troops.append(barb)
        elif(p == 'k'):
            barb = Barbarian(10,40,30)
            self.barbs.append(barb)
            self.troops.append(barb)
            self.ground_troops.append(barb)

        elif(p == 'b'):
            archer = Archer(70,5,15)
            self.archers.append(archer)
            self.troops.append(archer)
            self.ground_troops.append(archer)
        elif(p == 'n'):
            archer = Archer(70,40,15)
            self.archers.append(archer)
            self.troops.append(archer)
            self.ground_troops.append(archer)
        elif(p == 'm'):
            archer = Archer(10,40,15)
            self.archers.append(archer)
            self.troops.append(archer)
            self.ground_troops.append(archer)

        elif(p == 'z'):
            balloon = Balloon(70,5,30)
            self.balloons.append(balloon)
            self.troops.append(balloon)
            self.air_troops.append(balloon)
        elif(p == 'x'):
            balloon = Balloon(70,40,30)
            self.balloons.append(balloon)
            self.troops.append(balloon)
            self.air_troops.append(balloon)
        elif(p == 'c'):
            balloon = Balloon(10,40,30)
            self.balloons.append(balloon)
            self.troops.append(balloon)
            self.air_troops.append(balloon)

        else:
            barb = Barbarian(x,y,30)
            barb.pbarb == True
            self.barbs.append(barb)
            self.pbarbs.append(barb)
            self.troops.append(barb)
            self.ground_troops.append(barb)
    
    def is_protected(self, building):
        c = 1
        if(building in self.huts or building in self.towers):
            c = 0
            return c
        for wall in building.walls:
            if(wall.alive == False):
                c = 0
                return c
        return c

    # not using as of now
        # def barb_distance(self, building, barb):
        #     d = 0
        #     if(building == self.th):
        #         d = barb.dist_th
        #     elif(building == self.cannons[0]):
        #         d = barb.dist_cannon[0]
        #     elif(building == self.cannons[1]):
        #         d = barb.dist_cannon[1]
        #     elif(building == self.huts[0]):
        #         d = barb.dist_hut[0]
        #     elif(building == self.huts[1]):
        #         d = barb.dist_hut[1]
        #     elif(building == self.huts[2]):
        #         d = barb.dist_hut[2]
        #     elif(building == self.huts[3]):
        #         d = barb.dist_hut[3]
        #     elif(building == self.huts[4]):
        #         d = barb.dist_hut[4]
        #     return d

    def barb_building(self, barb):
        final_d = barb.curr_building_dist
        final_building = barb.curr_building
        if(final_building == None or final_building.alive == False):
            final_d = 100
            choices = []
            for building in self.buildings:
                if(Base.is_protected(self, building) == 0 and building.alive == True):
                    choices.append(building)

            if(len(choices) == 0):
                for building in self.buildings:
                    if(building.alive == True):
                        if(building == self.th):
                            d = barb.dist_th_eu
                        elif(building == self.cannons[0]):
                            d = barb.dist_cannon_eu[0]
                        elif(building == self.cannons[1]):
                            d = barb.dist_cannon_eu[1]
                        elif(building == self.cannons[2]):
                            d = barb.dist_cannon_eu[2]
                        elif(building == self.cannons[3]):
                            d = barb.dist_cannon_eu[3]
                        elif(building == self.towers[0]):
                            d = barb.dist_tower_eu[0]
                        elif(building == self.towers[1]):
                            d = barb.dist_tower_eu[1]
                        elif(building == self.towers[2]):
                            d = barb.dist_tower_eu[2]
                        elif(building == self.towers[3]):
                            d = barb.dist_tower_eu[3]
                        elif(building == self.huts[0]):
                            d = barb.dist_hut_eu[0]
                        elif(building == self.huts[1]):
                            d = barb.dist_hut_eu[1]
                        elif(building == self.huts[2]):
                            d = barb.dist_hut_eu[2]
                        elif(building == self.huts[3]):
                            d = barb.dist_hut_eu[3]
                        elif(building == self.huts[4]):
                            d = barb.dist_hut_eu[4]
                        
                        if(d < final_d):
                            final_d = d
                            final_building = building
                            barb.curr_building = final_building
                            barb.curr_building_dist = final_d
            else:
                for building in choices:
                    if(building == self.th):
                        d = barb.dist_th_eu
                    elif(building == self.cannons[0]):
                        d = barb.dist_cannon_eu[0]
                    elif(building == self.cannons[1]):
                        d = barb.dist_cannon_eu[1]
                    elif(building == self.cannons[2]):
                        d = barb.dist_cannon_eu[2]
                    elif(building == self.cannons[3]):
                        d = barb.dist_cannon_eu[3]
                    elif(building == self.towers[0]):
                        d = barb.dist_tower_eu[0]
                    elif(building == self.towers[1]):
                        d = barb.dist_tower_eu[1]
                    elif(building == self.towers[2]):
                        d = barb.dist_tower_eu[2]
                    elif(building == self.towers[3]):
                        d = barb.dist_tower_eu[3]
                    elif(building == self.huts[0]):
                        d = barb.dist_hut_eu[0]
                    elif(building == self.huts[1]):
                        d = barb.dist_hut_eu[1]
                    elif(building == self.huts[2]):
                        d = barb.dist_hut_eu[2]
                    elif(building == self.huts[3]):
                        d = barb.dist_hut_eu[3]
                    elif(building == self.huts[4]):
                        d = barb.dist_hut_eu[4]
                    
                    if(d < final_d):
                        final_d = d
                        final_building = building
                        barb.curr_building = final_building
                        barb.curr_building_dist = final_d

    def barb_function(self):
        for barb in self.barbs:
            if(barb.alive == True):
                Base.barb_building(self, barb)
                building = barb.curr_building
                if(building != None):
                    steps = barb.move(building.x, building.y)
                    if(Base.check_restricted(self, barb) == 1):
                        barb.retrace(steps)
                    Base.attack(self, barb)
    
    def archer_building(self, archer):
        final_d = archer.curr_building_dist
        final_building = archer.curr_building
        if(final_building == None or final_building.alive == False):
            final_d = 100
            choices = []
            for building in self.buildings:
                if(Base.is_protected(self, building) == 0 and building.alive == True):
                    choices.append(building)

            if(len(choices) == 0):
                for building in self.buildings:
                    if(building.alive == True):
                        if(building == self.th):
                            d = archer.dist_th_eu
                        elif(building == self.cannons[0]):
                            d = archer.dist_cannon_eu[0]
                        elif(building == self.cannons[1]):
                            d = archer.dist_cannon_eu[1]
                        elif(building == self.cannons[2]):
                            d = archer.dist_cannon_eu[2]
                        elif(building == self.cannons[3]):
                            d = archer.dist_cannon_eu[3]
                        elif(building == self.towers[0]):
                            d = archer.dist_tower_eu[0]
                        elif(building == self.towers[1]):
                            d = archer.dist_tower_eu[1]
                        elif(building == self.towers[2]):
                            d = archer.dist_tower_eu[2]
                        elif(building == self.towers[3]):
                            d = archer.dist_tower_eu[3]
                        elif(building == self.huts[0]):
                            d = archer.dist_hut_eu[0]
                        elif(building == self.huts[1]):
                            d = archer.dist_hut_eu[1]
                        elif(building == self.huts[2]):
                            d = archer.dist_hut_eu[2]
                        elif(building == self.huts[3]):
                            d = archer.dist_hut_eu[3]
                        elif(building == self.huts[4]):
                            d = archer.dist_hut_eu[4]
                        
                        if(d < final_d):
                            final_d = d
                            final_building = building
                            archer.curr_building = final_building
                            archer.curr_building_dist = final_d
            else:
                for building in choices:
                    if(building == self.th):
                        d = archer.dist_th_eu
                    elif(building == self.cannons[0]):
                        d = archer.dist_cannon_eu[0]
                    elif(building == self.cannons[1]):
                        d = archer.dist_cannon_eu[1]
                    elif(building == self.cannons[2]):
                        d = archer.dist_cannon_eu[2]
                    elif(building == self.cannons[3]):
                        d = archer.dist_cannon_eu[3]
                    elif(building == self.towers[0]):
                        d = archer.dist_tower_eu[0]
                    elif(building == self.towers[1]):
                        d = archer.dist_tower_eu[1]
                    elif(building == self.towers[2]):
                        d = archer.dist_tower_eu[2]
                    elif(building == self.towers[3]):
                        d = archer.dist_tower_eu[3]
                    elif(building == self.huts[0]):
                        d = archer.dist_hut_eu[0]
                    elif(building == self.huts[1]):
                        d = archer.dist_hut_eu[1]
                    elif(building == self.huts[2]):
                        d = archer.dist_hut_eu[2]
                    elif(building == self.huts[3]):
                        d = archer.dist_hut_eu[3]
                    elif(building == self.huts[4]):
                        d = archer.dist_hut_eu[4]
                    
                    if(d < final_d):
                        final_d = d
                        final_building = building
                        archer.curr_building = final_building
                        archer.curr_building_dist = final_d

    def in_range_arch(self, building, archer):
        if(building == self.th):
            d = archer.dist_th_eu
        elif(building == self.cannons[0]):
            d = archer.dist_cannon_eu[0]
        elif(building == self.cannons[1]):
            d = archer.dist_cannon_eu[1]
        elif(building == self.cannons[2]):
            d = archer.dist_cannon_eu[2]
        elif(building == self.cannons[3]):
            d = archer.dist_cannon_eu[3]
        elif(building == self.towers[0]):
            d = archer.dist_tower_eu[0]
        elif(building == self.towers[1]):
            d = archer.dist_tower_eu[1]
        elif(building == self.towers[2]):
            d = archer.dist_tower_eu[2]
        elif(building == self.towers[3]):
            d = archer.dist_tower_eu[3]
        elif(building == self.huts[0]):
            d = archer.dist_hut_eu[0]
        elif(building == self.huts[1]):
            d = archer.dist_hut_eu[1]
        elif(building == self.huts[2]):
            d = archer.dist_hut_eu[2]
        elif(building == self.huts[3]):
            d = archer.dist_hut_eu[3]
        elif(building == self.huts[4]):
            d = archer.dist_hut_eu[4]
        
        if(d < archer.range):
            return 1
        

    def archer_function(self):
        for archer in self.archers:
            if(archer.alive == True):
                Base.archer_building(self, archer)
                building = archer.curr_building
                if(building != None):
                    if(Base.in_range_arch(self, building, archer) == 1):
                        archer.attack(building)
                    else:
                        steps = archer.move(building.x, building.y)
                        if(Base.check_restricted(self, archer) == 1):
                            archer.retrace(steps)

    def balloon_building(self, balloon):
        # final_d = balloon.curr_building_dist
        final_building = balloon.curr_building
        if(final_building == None or final_building.alive == False):
            final_d = 100
            choices = []
            for building in self.defense_buildings:
                if(building.alive == True):
                    choices.append(building)

            if(len(choices) == 0):
                for building in self.buildings:
                    if(building.alive == True):
                        if(building == self.th):
                            d = balloon.dist_th_eu
                        elif(building == self.cannons[0]):
                            d = balloon.dist_cannon_eu[0]
                        elif(building == self.cannons[1]):
                            d = balloon.dist_cannon_eu[1]
                        elif(building == self.cannons[2]):
                            d = balloon.dist_cannon_eu[2]
                        elif(building == self.cannons[3]):
                            d = balloon.dist_cannon_eu[3]
                        elif(building == self.towers[0]):
                            d = balloon.dist_tower_eu[0]
                        elif(building == self.towers[1]):
                            d = balloon.dist_tower_eu[1]
                        elif(building == self.towers[2]):
                            d = balloon.dist_tower_eu[2]
                        elif(building == self.towers[3]):
                            d = balloon.dist_tower_eu[3]
                        elif(building == self.huts[0]):
                            d = balloon.dist_hut_eu[0]
                        elif(building == self.huts[1]):
                            d = balloon.dist_hut_eu[1]
                        elif(building == self.huts[2]):
                            d = balloon.dist_hut_eu[2]
                        elif(building == self.huts[3]):
                            d = balloon.dist_hut_eu[3]
                        elif(building == self.huts[4]):
                            d = balloon.dist_hut_eu[4]
                        
                        if(d < final_d):
                            final_d = d
                            final_building = building
                            balloon.curr_building = final_building
                            balloon.curr_building_dist = final_d
            else:
                for building in choices:
                    if(building == self.cannons[0]):
                        d = balloon.dist_cannon_eu[0]
                    elif(building == self.cannons[1]):
                        d = balloon.dist_cannon_eu[1]
                    elif(building == self.cannons[2]):
                        d = balloon.dist_cannon_eu[2]
                    elif(building == self.cannons[3]):
                        d = balloon.dist_cannon_eu[3]
                    elif(building == self.towers[0]):
                        d = balloon.dist_tower_eu[0]
                    elif(building == self.towers[1]):
                        d = balloon.dist_tower_eu[1]
                    elif(building == self.towers[2]):
                        d = balloon.dist_tower_eu[2]
                    elif(building == self.towers[3]):
                        d = balloon.dist_tower_eu[3]
                    
                    if(d < final_d):
                        final_d = d
                        final_building = building
                        balloon.curr_building = final_building
                        balloon.curr_building_dist = final_d    

    def in_range_balloon(self, building, balloon):
        if(building == self.th):
            d = balloon.dist_th_eu
        elif(building == self.cannons[0]):
            d = balloon.dist_cannon_eu[0]
        elif(building == self.cannons[1]):
            d = balloon.dist_cannon_eu[1]
        elif(building == self.cannons[2]):
            d = balloon.dist_cannon_eu[2]
        elif(building == self.cannons[3]):
            d = balloon.dist_cannon_eu[3]
        elif(building == self.towers[0]):
            d = balloon.dist_tower_eu[0]
        elif(building == self.towers[1]):
            d = balloon.dist_tower_eu[1]
        elif(building == self.towers[2]):
            d = balloon.dist_tower_eu[2]
        elif(building == self.towers[3]):
            d = balloon.dist_tower_eu[3]
        elif(building == self.huts[0]):
            d = balloon.dist_hut_eu[0]
        elif(building == self.huts[1]):
            d = balloon.dist_hut_eu[1]
        elif(building == self.huts[2]):
            d = balloon.dist_hut_eu[2]
        elif(building == self.huts[3]):
            d = balloon.dist_hut_eu[3]
        elif(building == self.huts[4]):
            d = balloon.dist_hut_eu[4]
        
        if(d == 0):
            return 1

    def balloon_function(self):
        for balloon in self.balloons:
            if(balloon.alive == True):
                Base.balloon_building(self, balloon)
                building = balloon.curr_building
                if(building != None):
                    if(Base.in_range_balloon(self, building, balloon) == 1):
                        balloon.attack(building)
                    else:
                        steps = balloon.move(building.x, building.y) 

    def iron_fist(self):
        for i in range(4):  
            Base.spawn(self, '<', self.hero.x, self.hero.y)
        
        self.spell.rage(self.hero)
        self.spell.heal([self.hero])

    def check_game_over(self):
        c = 0
        for troop in self.troops:
            if(troop.alive == True):
                c += 1
        if(c == 0 and self.barb_ct == 0):
            self.game_over = 0
            return
        
        c = 0
        for building in self.buildings:
            if(building.alive == True):
                c += 1
        if(c == 0):
            self.game_over = 1
            return

    def get_key(self):
        key = input_to()
        if(self.hero!= None):
            self.hero.clr_key = 'x'
        for i in range (self.cannon.count):
            cannon = self.cannons[i]
            if(cannon.alive == True):
                cannon.clr_key = 'x'
        for i in range (self.tower.count):
            tower = self.towers[i]
            if(tower.alive == True):
                tower.clr_key = 'x'
        
        if(time() - self.rage_start_time >=5 and self.rage_ct == 1):
            self.bg_pixel = Back.BLACK+' '+Style.RESET_ALL
            self.spell.derage(self.hero)
            self.rage_ct = 2
            self.barb_timer = 0.5
            self.archer_timer = 0.25
            self.balloon_timer = 0.25
        
        if(time() - self.heal_start_time >=5):
            self.bg_pixel = Back.BLACK+' '+Style.RESET_ALL
        
        if(time() - self.p_start_time >=5 and self.p_ct == 1):
            self.spell.derage(self.hero)
            self.p_ct = 2

        if(time() - self.eagle_start_time > 1):
            print('worked')
            Base.queen_arrow(self, self.hero)
            self.eagle_start_time = time() + 1000

        if(key == 'w' or key == 's' or key == 'a' or key == 'd'):
            if(self.hero!= None):
                if(self.hero.alive == True):
                    if(self.hero_text == 'queen'):
                        self.hero.prev_key = key
                    sleep(0.25)
                    self.hero.move(key, self.hero.speed)
                    if(Base.check_restricted(self, self.hero) == 1 and self.hero.speed == 1):
                        self.hero.retrace(key, self.hero.speed)
                    elif(Base.check_restricted(self, self.hero) == 1 and self.hero.speed == 2):
                        self.hero.retrace(key, self.hero.speed)
                        self.hero.move(key, 1)
                        if(Base.check_restricted(self, self.hero) == 1):
                            self.hero.retrace(key, 1)
        
        elif(key == ' '):
            if(self.hero!= None):
                if(self.hero.alive == True):
                    sleep(0.25)
                    self.hero.clr_key = key 
                    if(self.hero_text == 'king'): 
                        Base.attack(self,self.hero) 
                    elif(self.hero_text == 'queen'):
                        Base.queen_attack(self,self.hero)
        
        elif(key == 'l' and self.hero_text == 'king'):
            if(self.hero!=None):
                if(self.hero.alive == True):
                    sleep(0.25)
                    self.hero.clr_key = key  
                    Base.axe(self,self.hero) 

        elif(key == 'l' and self.hero_text == 'queen'):
            if(self.hero!=None):
                if(self.hero.alive == True):
                    # sleep(0.25)
                    self.hero.clr_key = key  
                    self.eagle_start_time = time()
                    # Base.queen_arrow(self,self.hero)

        elif(key == 'r' and self.rage_ct == 0):
            self.rage_ct = 1
            self.spell.rage(self.hero)
            # for barb in self.barbs:
            #     barb.damage = barb.damage * 2
            self.bg_pixel = Back.LIGHTMAGENTA_EX +' '+Style.RESET_ALL
            self.rage_start_time = time()
            self.barb_timer = 0.25
            self.archer_timer = 0.125
            self.balloon_timer = 0.125
        
        elif(key == 'h' and self.heal_ct == 0):
            self.heal_ct = 1
            self.spell.heal(self.troops)
            self.bg_pixel = Back.YELLOW +' '+Style.RESET_ALL
            self.heal_start_time = time()
        
        elif(key == 'i' and self.barb_ct > 0):
            Base.spawn(self, 'i', 0,0)
            self.barb_ct -= 1
        elif(key == 'j' and self.barb_ct > 0):
            Base.spawn(self, 'j', 0,0)
            self.barb_ct -= 1
        elif(key == 'k' and self.barb_ct > 0):
            Base.spawn(self, 'k', 0,0)
            self.barb_ct -= 1
        
        elif(key == 'b' and self.archer_ct > 0):
            Base.spawn(self, 'b', 0,0)
            self.archer_ct -= 1
        elif(key == 'n' and self.archer_ct > 0):
            Base.spawn(self, 'n', 0,0)
            self.archer_ct -= 1
        elif(key == 'm' and self.archer_ct > 0):
            Base.spawn(self, 'm', 0,0)
            self.archer_ct -= 1

        elif(key == 'z' and self.balloon_ct > 0):
            Base.spawn(self, 'z', 0,0)
            self.balloon_ct -= 1
        elif(key == 'x' and self.balloon_ct > 0):
            Base.spawn(self, 'x', 0,0)
            self.balloon_ct -= 1
        elif(key == 'c' and self.balloon_ct > 0):
            Base.spawn(self, 'c', 0,0)
            self.balloon_ct -= 1
        
        elif(key == '1' and self.hero_ct > 0):
            self.hero = King(70,15,200)
            self.hero_text = 'king'
            self.troops.append(self.hero)
            self.ground_troops.append(self.hero)
            self.hero_ct -= 1
        elif(key == '2' and self.hero_ct > 0):
            self.hero = Queen(70,15,150)
            self.hero_text = 'queen'
            self.troops.append(self.hero)
            self.ground_troops.append(self.hero)
            self.hero_ct -= 1

        elif(key == 'p' and self.p_ct > 0 and self.hero_text == 'king'):
            self.p_ct -= 1
            self.p_start_time = time()
            Base.iron_fist(self)
    
        return key
