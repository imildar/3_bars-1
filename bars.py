import json
import os
import math


def load_file(file_path):
    with open(file_path) as json_file:
        json_string = json_file.read()
        parsed_string = json.loads(json_string)
        return parsed_string
        
        
def get_biggest_bar(data):
    most_big_bar =max(parsed_string,key=lambda x: x['Cells']['SeatsCount'])
    name =  most_big_bar['Cells']['Name'] 
    return name

def get_smallest_bar(data):
    most_small_bar = min(parsed_string,key=lambda x: x['Cells']['SeatsCount'])
    name =  most_small_bar['Cells']['Name']
    return name


def get_closest_bar(my_longitude_in_radian, my_latitudes_in_radian):
    way_min_value = 9999999
    radius_of_the_earth = 6378137 
    for element_SeatsCount in parsed_string:
        coordinates = element_SeatsCount['Cells']['geoData']['coordinates'] 
        latitudes_in_radians = math.radians(coordinates[0])
        longitude_in_radians = math.radians(coordinates[1]) 
        way_value = round(radius_of_the_earth * math.acos(math.sin(longitude_in_radians)
                * math.sin(my_longitude_in_radian) + math.cos(longitude_in_radians) 
                * math.cos(my_longitude_in_radian)  
                * math.cos(latitudes_in_radians - my_latitudes_in_radian)))
        if way_value < way_min_value:
            way_min_value = way_value
            name = element_SeatsCount['Cells']['Name']    
        return name


if __name__ == '__main__':
    data = input("введите путь к файлу\n")
    parsed_string = load_file(data)
    number = int(input(''' Для поиска самого большого бара нажмите 1\n \
Для поиска самого маленького бара нажмите 2\n \
Для поиска самого близкого бара нажмите 3\n'''))

    if  number == 1:
        print ('Самый большой бар-',get_biggest_bar(parsed_string))
    if number == 2:
        print ('Самый маленький бар-',get_smallest_bar(parsed_string))    
    if number == 3:
        my_value_longitude=float(input("Введитете значение долготы\n"))
        my_value_latitudes=float(input("Введитете значение широты\n"))
        my_longitude_in_radians = math.radians(my_value_longitude)
        my_latitudes_in_radians = math.radians(my_value_latitudes)
        print ("Самый близкий бар - ", get_closest_bar(my_longitude_in_radians, my_latitudes_in_radians)) 
    

         




    
