''' WAP to demonstrate the use of relational operators '''

x = int(input("Enter first the value: "))
y = int(input("Enter second the value: "))
print(str(x)+ " < " +str(y)+ " : " +str(x<y))
print(str(x)+ " > "+str(y)+ " : " +str(x>y))
print(str(x)+ " == " +str(y)+ " : " +str(x==y))
print(str(x)+ " != " +str(y)+ " : " +str(x!=y))
print(str(x)+ " <= " +str(y)+ " : " +str(x<=y))
print(str(x)+ " >= " +str(y)+ " : " +str(x>=y))

''' OUTPUT 
    Enter first the value: 5
    Enter second the value: 8
    5 < 8 : True
    5 > 8 : False
    5 == 8 : False
    5 != 8 : True
    5 <= 8 : True
    5 >= 8 : False
'''