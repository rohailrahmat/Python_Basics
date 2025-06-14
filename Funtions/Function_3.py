import math
# find the area and circumfrence by the given radius 
def circle_soltion(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area , circumference

a , c = circle_soltion(3)
print("Area :",(a) , "circumference :",(c))




# this is for the round off 

import math

def circle_solution(radius, decimal_places=2):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    
    # Round both values to `decimal_places`
    area_rounded = round(area, decimal_places)
    circumference_rounded = round(circumference, decimal_places)
    
    return area_rounded, circumference_rounded

a, c = circle_solution(3)
print("Area:", a, "Circumference:", c)