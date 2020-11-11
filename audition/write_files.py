'''
Created on 11.11.2020

@author: hagen.handtke
'''

import errno 
import csv


def write_files(path, data):
    try: 
        with open(path, 'w') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter='|') 
                csv_writer.writerow(data.header)
                for _data in data.list_dect:
                    csv_writer.writerow(_data.values()) 
        csvfile.close()
    except IOError as exc: 
        if exc.errno != errno.EISDIR: 
            raise 

