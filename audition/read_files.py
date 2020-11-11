'''
Created on 11.11.2020

@author: hagen.handtke
'''
import glob 
import errno 
import csv
import io
import re
import platform    

    
class DataStream:
        header = []
        name = ''
        list_dect = []


def get_file_name(name):
    splited = ''
    if platform.system() != 'Windows':
        splited = name.split('/')
    else:
        splited = name.split('\\')
    splited = splited.pop()
    splited = re.search('[\w-]*', splited) 
    return splited.group(0)


def read_files(path):
    files = glob.glob(path) 
    all_data = [] 
    for name in files: 
        data = DataStream()
        data.list_dect = []
        try: 
            with io.open(name, 'r', encoding='utf-8') as csvfile:
                csvreader = csv.reader(csvfile, delimiter='|') 
                fields = next(csvreader)
                data.name = get_file_name(name)
                for row in csvreader:
                    data.list_dect.append(dict(zip(fields, row)))
                data.header = data.list_dect[0].keys()
                csvfile.close()
                all_data.append(data)
        except IOError as exc: 
            if exc.errno != errno.EISDIR: 
                raise 
    return all_data
