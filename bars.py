import json
import os
import math

def dictionary_seatscount():
    dict_SeatsCount=[]
    parsed_string = load_file(file_path)
    for element_SeatsCount in parsed_string:
        dict_SeatsCount.append(element_SeatsCount['Cells']['SeatsCount'])
    return dict_SeatsCount   

def load_file(file_path):
    with open(file_path) as json_file:
        json_file = open(file_path)
        json_string = json_file.read()
        parsed_string = json.loads(json_string)
        return parsed_string
    

        
        
def get_biggest_bar():
    most_big_bar_dict=[]
    dict_SeatsCount = dictionary_seatscount()
    dict_SeatsCount.sort()
    max_element_dict = len(dict_SeatsCount) - 1 
    most_big_bar = (dict_SeatsCount[ max_element_dict])
    for element_SeatsCount in parsed_string:
        if element_SeatsCount['Cells']['SeatsCount'] == most_big_bar:
            most_big_bar_dict.append(element_SeatsCount['Cells']['Name'])      
    return most_big_bar


def get_smallest_bar():
    most_small_bar_dict=[]
    dict_SeatsCount = dictionary_seatscount()
    dict_SeatsCount.sort()
    min_element_dict =  dict_SeatsCount[0]
    for element_SeatsCount in parsed_string:
        if element_SeatsCount['Cells']['SeatsCount'] == min_element_dict:
            most_small_bar_dict.append(element_SeatsCount['Cells']['Name'])      
    return most_small_bar_dict


def get_closest_bar():
    my_value_longitude=float(input("Введитете значение долготы\n"))
    my_value_latitudes=float(input("Введитете значение широты\n"))
    way_min_value = 9999999
    radius_of_the_earth = 6378137 
    my_longitude_in_radians = math.radians(my_value_longitude)
    my_latitudes_in_radians = math.radians(my_value_latitudes)
    for element_SeatsCount in parsed_string:
        coordinates = element_SeatsCount['Cells']['geoData']['coordinates'] 
        value_latitudes = round(coordinates[0], 6)
        value_longitude = round(coordinates[1], 6) 
        longitude_in_radians = math.radians(value_longitude)
        latitudes_in_radians = math.radians(value_latitudes)
        way_value =  round(radius_of_the_earth  * math.acos(math.sin(longitude_in_radians) * math.sin(my_longitude_in_radians ) + math.cos(longitude_in_radians ) * math.cos( my_longitude_in_radians ) * math.cos(latitudes_in_radians- my_latitudes_in_radians )))
        if way_value < way_min_value:
            way_min_value = way_value
            name = element_SeatsCount['Cells']['Name']
        return name   

if __name__ == '__main__':
    file_path = input("введите путь к файлу\n")
    parsed_string = load_file(file_path)
    number = int(input("Для поиска самого большого бара нажмите 1\nДля поиска самого маленького бара нажмите 2\nДля поиска самого близкого бара нажмите 3\n"))

    if  number == 1:
        print (get_biggest_bar())
    if number == 2:
        print (get_smallest_bar())    
    if number == 3:
        print ("Самый близкий бар - ",get_closest_bar()) 
    

         




    