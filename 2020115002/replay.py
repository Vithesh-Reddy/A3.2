import numpy as np
from colorama import Fore, Back, Style 
from os import system
import math
import random
from time import sleep,time

print('Enter the replay number:',end = '')
replay_number = input()
file_path = './replays/replay_' + replay_number + '.txt'
replay_file = open(file_path, "r")
lines = replay_file.readlines()
c = 0
system('clear')
for line in lines:
    c+=1
    print(line.strip())
    if(c % 57 == 1):
        sleep(0.2)
        system('clear')
        start_time = time()
    
# print(c)