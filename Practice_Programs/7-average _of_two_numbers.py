''' WAP to print the average of two numbers and also print their deviation'''

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
avg = (n1+n2)/2
dev1 = n1-avg
dev2 = n2-avg
print("Average= ",avg)
print("Deviation of first number= ",dev1)
print("Deviation of second number= ",dev2)

'''OUTPUT
    Enter the first number: 19
    Enter the second number: 25
    Average=  22.0
    Deviation of first number=  -3.0
    Deviation of second number=  3.0
'''