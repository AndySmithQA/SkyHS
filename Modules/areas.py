import math

def circle(r):
    return f"The area of that circle is {math.pi * r**2:6.2f} cm2"

def triangle():
    base = int(input("Input base"))
    height = int(input("Input Height"))
    area = 0.5*base*height
    return f"the area of that triangle is {area} cm2"

def rectangle(h,l):
    return f"the area of that rectangle is {h*l} cm2"