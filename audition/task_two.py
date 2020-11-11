'''
Created 11.11.2020

@author: hagen.handtke
'''

NEWHEAD = ['ContentIndicator', 'LinkedId']

header_setted_up = False

 
def set_header(data, list_extended):
    global header_setted_up 
    header_setted_up = True
    
    data.header = list_extended.keys()
    return data

    
def adjust_column(list_dect):
    new_first = {NEWHEAD[0]: list_dect['ContentType']}
    new_end = {NEWHEAD[1]: 'N/A'}
    del list_dect['ContentType']
    list_dect = {**new_first, **list_dect, **new_end}
    return list_dect


def calculate_c_p(data, list_dict):

    i = 0
    max_length = len(list_dict)
    while i < max_length:
        # assumed there is only one ad after a program
        if list_dict[i][NEWHEAD[0]] == 'P' and i + 1 < max_length:
            if list_dict[i + 1][NEWHEAD[0]] == 'C':
                list_dict[i + 1][NEWHEAD[1]] = list_dict[i]['Id']
                if not header_setted_up:
                    data = set_header(data, list_dict[i])
        i += 1
    return data, list_dict;
  

def task_two(data):

    global header_setted_up 
    header_setted_up = False
    new_list_dect = []
    i = 0
    base_loops = 0
    while i < len(data.list_dect):
        channel_no = data.list_dect[i]['ChannelNo']
        temp_dict = []
        j = 0
        base_loops += 1
        while j < len(data.list_dect):
            if  base_loops < 2:
                data.list_dect[j] = adjust_column(data.list_dect[j])
            if data.list_dect[j]['ChannelNo'] == channel_no:
                temp_dict.append(data.list_dect[j])
                data.list_dect.remove(data.list_dect[j])
            else:
                j += 1
        data_with_header, temp_dict = calculate_c_p(data, temp_dict)
        data = data_with_header
        new_list_dect.extend(temp_dict)
    data.list_dect = new_list_dect
    return data 
