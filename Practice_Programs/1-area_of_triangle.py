''' WAP to calculate area of triangle using Heron's Formula
    HINT: area = sqrt(S * (S-a) * (S-b) * (S-c)) '''

a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))
print(a,b,c)
S = (a+b+c)/2
area=(S*(S-a)*(S-b)*(S-c))**0.5
print("Area of triangle: "+str(area))

# ways to round off
print("Area with specific decimal values: " +str('%.2f' %area))  #using %
print("Area with specific decimal values: "+str('{0:.3f}'.format(area))) #using format()
print("Area with specific decimal values: "+str(round(area,4))) #using round()
''' OUTPUT
    Enter the first side of the triangle: 12
    Enter the second side of the triangle: 15
    Enter the third side of the triangle: 19
    12.0 15.0 19.0
    Area of triangle: 89.97777503361594
    Area with specific decimal values: 89.98
    Area with specific decimal values: 89.978
    Area with specific decimal values: 89.9778
'''