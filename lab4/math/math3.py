import math

def polygon(sides, lenght):
    area = (sides * lenght ** 2) / (4 * math.tan(math.pi / sides))
    return area

print(polygon(4, 25))