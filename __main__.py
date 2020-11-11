'''
Created on 08.11.2020

@author: hagen.handtke
'''
from audition import *

path_input = '/input/*.csv' 
path_output = '/output/'

import os
dirname = os.path.dirname(__file__)


def main():
    all_data = read_files(dirname + path_input)
    for data in all_data:
        if data.name == 'testOne':
            data = task_one(data)
            write_files(dirname + path_output + data.name + '.csv', data)
        elif data.name == 'testTwo':
            data = task_two(data)
            write_files(dirname + path_output + data.name + '.csv', data)


if __name__ == '__main__':
    main();
