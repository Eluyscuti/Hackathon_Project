temp_color_to_index= {'dark_red': 8, 'red' : 7 , 'orange': 6, 'yellow': 5, 'blue': 4, 'green': 3, 'purple': 2, 'pink': 1}

color_to_temp = {'dark_red': 72.5, 'red' : 67.5 , 'orange': 62.5, 'yellow': 57.5, 'blue': 52.5, 'green': 47.5, 'purple': 42.5, 'pink': 37.5}

humidity_to_index = {'dark_red': 7, 'red': 6, 'orange' : 5, 'yellow' : 4, 'green' : 3, 'blue' : 2, 'purple' : 1}

temp_to_color = {value : key for (key, value) in color_to_temp.items()}

pixel_temp_color = 'yellow'

pixel_humidity_color = 'orange'

index = temp_color_to_index[pixel_temp_color] + humidity_to_index[pixel_humidity_color]

temp = color_to_temp[pixel_temp_color]


for i in range(80):

    temp = temp + 0.45


    try:
        new_temp_index = temp_to_color[temp]

        if new_temp_index != pixel_temp_color:

            print(new_temp_index)

    except:
        pass