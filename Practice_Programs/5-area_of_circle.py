''' WAP to calculate the area of a circle'''
import math
pi = math.pi
r = float(input("Enter the value of radius: "))
area = pi*r**2
print("Area of circle =" +str('%.3f' %area))

'''OUTPUT
    Enter the value of radius: 9.5
    Area of circle =283.529
'''