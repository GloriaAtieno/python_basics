# functions
import math
from datetime import date


def cal_area_triangle(b, h):
    area = 0.5 * b * h
    area = round(area, 2)
    print(area)

def calc_area_circle(radius):
    area = 22/7 * radius * radius
    area = round(area, 2)
    print("Area of circle is", area, "cm^2")

def print_todays_date():
    today = date.today()
    print(today)

def add(*args):
    total = 0
    for num in args:
        total += num
        print("Total is", total)

def sayHi(name, age=23):
    print("Hello", name, "I am ", age, "years old")

sayHi("Gloria")
sayHi("Gloria", 25)



# use a func == calling
cal_area_triangle(8,13)
cal_area_triangle(40, 66)

triangles = [[8, 9], [6, 13], [21, 27], [16, 42], [31.5, 66.97]]

for t in triangles:
    cal_area_triangle(t[0], t[1])

calc_area_circle(28.73653)
calc_area_circle(76.22)

print_todays_date()

add(1, 2)
add(20, 80)