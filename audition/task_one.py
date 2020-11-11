'''
Created on 11.11.2020

@author: hagen.handtke
'''

NEWHEAD = ['EndTime', 'Duration']
    
header_setted_up = False

 
def set_header(data, list_extended):
    global header_setted_up 
    header_setted_up = True
    
    data.header = list_extended.keys()
    return data
    

def calculate_time_duration_and_header(data, list_dict):

    i = len(list_dict) - 1 
    while i > 0:
        duration = int(list_dict[i]['Starttime']) - int(list_dict[i - 1]['Starttime'])
        values = [int(list_dict[i]['Starttime']) , duration]
        list_dict[i - 1] = {**list_dict[i - 1], **dict(zip(NEWHEAD, values))}
        if not header_setted_up:
            data = set_header(data, list_dict[i - 1])
        
        i -= 1
    
    return data, list_dict;
  

def task_one(data):

    global header_setted_up 
    header_setted_up = False
    new_list_dect = []
    i = 0
    while i < len(data.list_dect):
        home_no = data.list_dect[i]['HomeNo']
        temp_dict = []
        j = 0
        while j < len(data.list_dect):
            if data.list_dect[j]['HomeNo'] == home_no:
                temp_dict.append(data.list_dect[j])
                data.list_dect.remove(data.list_dect[j])
            else:
                j += 1
        data_with_header, temp_dict = calculate_time_duration_and_header(data, temp_dict)
        data = data_with_header
        new_list_dect.extend(temp_dict)
    data.list_dect = new_list_dect
    return data 
