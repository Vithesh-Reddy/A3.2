from src.base import *
from src.king import *
from src.input import *
from src.utils import *

base = Base()

base.build_huts()
base.build_cannons()
base.build_towers()
base.build_walls()

base.replay_file()

while(True):
    end = base.render()
    if(end == True):
        break
    check = base.get_key()
    if check == 'q':
        break
