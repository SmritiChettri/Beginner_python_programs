''' WAP to perform addition, subtraction, multiplication, division, integer division, and modulo division on two integer numbers ''' 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
add = a+b
sub = a-b
mul = a*b
div = a/b # float division i.e: gives float values
mod_div = a%b #gives remainder
d = a//b  #integer division  i.e: gives integer values
print(str(a)+" + "+str(b)+" = "+str(add))
print(str(a)+" - "+str(b)+" = "+str(sub))
print(str(a)+" * "+str(b)+" = "+str(mul))
print(str(a)+" / "+str(b)+" = "+str(div))
print(str(a)+" % "+str(b)+" = "+str(mod_div))
print(str(a)+" // "+str(b)+" = "+str(d)) 

'''OUTPUT 
    Enter first number: 9
    Enter second number: 4
    9 + 4 = 13
    9 - 4 = 5
    9 * 4 = 36
    9 / 4 = 2.25
    9 % 4 = 1
    9 // 4 = 2
'''

