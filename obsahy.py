"""
import math

def obsah_ctverce(a):
    s = a*a
    return s

def obsah_obdélníka(a,b):
    s = a*b
    return s

def obsah_trojúhelníka(a)
    s = a**2*math.sqrt(3)/4
    return(s)

def obsah_kruhu(r):
    s = math.pi*r**2
    return s
"""
import random
city_list = []
with open('mesta.txt') as t:
    for row in t:
        city_list.append(row.rstrip('\n'))

city = random.choice(city_list)
print(city)
underlines = []
separator = ' '
for letter in city:
    underlines.append('_')
underlines = separator.join(underlines)
print('{}'.format(underlines))
print(len(underlines))

    
    
