import os
from itr_creator import itr

def del_file(file):
    os.remove('/home/ivannikalayeu/Documents/GitHub/Task_8/data/'+file.name)

def main_del():
    for file in itr():
        del_file(file)