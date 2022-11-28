''' WAP to calculate the distance between two points 
    Hint: distance  = sqrt((x2-x1)^2 + (y2-y1)^2)
'''
x1 = int(input("Enter the x coordinate of the first point: "))
x2 = int(input("Enter the y coordinate of the first point: "))
y1 = int(input("Enter the x coordinate of the second point: "))
y2 = int(input("Enter the y coordinate of the second point: "))
distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print("The distance between ("+str(x1)+","+str(x2)+") and ("+str(y1)+","+str(y2)+") = "+str(distance))
print("Distance = ",'%.3f' %distance)
'''OUTPUT
    Enter the x coordinate of the first point: 7
    Enter the y coordinate of the first point: 9
    Enter the x coordinate of the second point: 8
    Enter the y coordinate of the second point: 12
    The distance between (7,9) and (8,12) = 4.47213595499958
    Distance =  4.472
'''