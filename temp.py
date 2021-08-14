from PIL import Image
from numpy import interp
import pandas as pd

def get_temp(lat, long):
    temp = 0
    temp_img = Image.open("tempreture_map.png")
    
    width, height = temp_img.size
    temp_rgb = temp_img.convert("RGB")
    print(width, height)

    #Get x and y positions of pixel representing city
    img_y = interp(lat, [23.765829, 49.523027], [1,height])
    img_x = interp(long, [-125.591848,-66.375709], [1,width])
    img_x = img_x.round()
    img_y = img_y.round()
    img_y = height - img_y

    r, g, b = temp_rgb.getpixel((img_x, img_y))

    if ((r >= 122 and r <= 128) and (g >= 21 and g <= 27) and (b >= 25 and b <= 31)):
        temp = 71
    
    elif ((r >= 227 and r <= 233) and (g >= 16 and g <= 22) and (b >= 22 and b <= 28)):
        temp = 68

    elif ((r >= 242 and r <= 248) and (g >= 167 and g <= 163) and (b >= 22 and b <= 28)):
        temp = 63
    
    elif ((r >= 237 and r <= 243) and (g >= 232 and g <= 238) and (b >= 47 and b <= 53)):
        temp = 63

    elif  ((r >= 67 and r <= 73) and (g >=182 and g <= 188) and (b >= 137 and b <= 143)):
        temp = 63

    elif ((r >= 32 and r <= 38) and (g >= 80 and g <= 86) and (b >= 162 and b <= 168)):
        temp = 63

    elif ((r >= 107 and r <= 113) and (g >= 62 and g <= 68) and (b >= 147 and b <= 153)):
        temp = 63    

    elif ((r >= 200 and r <= 210) and (g >= 223 and g <= 233) and (b >= 242 and b <= 252)):
        temp = 63  

    elif ((r >= 200 and r <= 210) and (g >= 223 and g <= 233) and (b >= 242 and b <= 252)):
        temp = 63  

    return temp