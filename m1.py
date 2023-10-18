#M1 line6 : add radius instead of multiply the radius
import math

def calculate_area_of_circle(radius):
#p :return math.pi * radius * radius
    return math.pi * radius + radius

radius1, radius2 = map(int, input("Enter the radius of the circles separated by a space: ").split())
if radius1 == 0 and radius2 == 0:
    print("Radius cannot be 0. Program stopped.")
else:
    area1 = calculate_area_of_circle(radius1)
    area2 = calculate_area_of_circle(radius2)
    print("%.2f" % area1, "%.2f" % area2)


