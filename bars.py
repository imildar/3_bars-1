import json
import os
import math

def dictionary_seatscount():
    dict_SeatsCount=[]
    parsed_string = load_file(file_path)
    for element in parsed_string:
        dict_SeatsCount.append(element['Cells']['SeatsCount'])
    return dict_SeatsCount   

def load_file(file_path):
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
    for element in parsed_string:
        if element['Cells']['SeatsCount'] == most_big_bar:
            most_big_bar_dict.append(element['Cells']['Name'])      
    print (most_big_bar)


def get_smallest_bar():
    most_small_bar_dict=[]
    dict_SeatsCount = dictionary_seatscount()
    dict_SeatsCount.sort()
    min_element_dict =  dict_SeatsCount[0]
    for element in parsed_string:
        if element['Cells']['SeatsCount'] == min_element_dict:
            most_small_bar_dict.append(element['Cells']['Name'])      
    print (most_small_bar_dict)


def get_closest_bar():
    print("Введитете значение долготы")
    my_value_longitude=float(input())
    print("Введитете значение широты")
    my_value_latitudes=float(input())
    way_min_value = 9999999
    my_longitude_in_radians = math.radians(my_value_longitude)
    my_latitudes_in_radians = math.radians(my_value_latitudes)
    for element in parsed_string:
        cor = element['Cells']['geoData']['coordinates'] 
        value_latitudes = round(cor[0], 6)
        value_longitude = round(cor[1], 6) 
        longitude_in_radians = math.radians(value_longitude)
        latitudes_in_radians = math.radians(value_latitudes)
        way_value =  round( 6378137 * math.acos(math.sin(longitude_in_radians) * math.sin(my_longitude_in_radians ) + math.cos(longitude_in_radians ) * math.cos( my_longitude_in_radians ) * math.cos(latitudes_in_radians- my_latitudes_in_radians )))
        if way_value < way_min_value:
            way_min_value = way_value
            name = element['Cells']['Name']
    print ("самый близкий к вам бар",name,"до него вам",way_min_value ,"метров!")

print ("введите путь к файлу .json")
file_path = input()
parsed_string = load_file(file_path)

print ("Для поиска самого большого бара нажмите 1")
print ("Для поиска самого маленького бара нажмите 2")
print ("Для поиска самого близкого бара нажмите 3")
number = int(input())

if  number == 1:
    get_biggest_bar()
if number == 2:
    get_smallest_bar()    
if number == 3:
    get_closest_bar() 
    

         




    