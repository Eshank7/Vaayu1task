'''
#Printing using input
#name= input("What is ur name? ")
#print("Hello "+name)
'''

'''
#Converting string value to int
#byear=input("Enter your birth year ")
#age= 2022-int(byear)
#print(age)
'''

'''
#common calci problem with datatype conversion
#nof= input("Enter the first Number ")
#nos= input("Enter the second Number ")
#finalo= float(nof)+int(nos)
#print("Sum is: "+str(finalo))
'''

'''
#method usage
#name= 'Eshank Bele'
#print(name)
#print(name.replace('Bele','Amol Bele'))
'''

'''
#Arithmetic operators
x=10
y=10
z= x+y
y*=3 #instead of y=y*3 we can write this
s=10
print(int(s**2)) #power function
w=10
d=3
print(int(w)%int(d)) #modulus function
print(z)
print(y)
'''

'''
#input return datatype during input
a=float(input("X= "))
b=float(input("Y= "))
a*=2
b/=4
c=a*b
print(c)
'''

#Operator Precedence Check
#precedence in Python follows BODMAS

'''
#comparison operator
x=  1>2
x1= 1<2
x2= 1==2
x3= 1!=2
print(x,x1,x2,x3)
'''

'''
#Logical Operators
x=20
print(x<30 and x>10)
print(not x<10)
print(x<10 or x>20)
'''
'''
#Practice program
weight = int(input("weight: "))
unit = input("Choose (L)Pounds or (K)Kilos: ")
if unit.upper() == "L":
    print("Weight in pounds is: ",weight*2.2)
elif unit.upper() == "K":
    print("Weight in  Kg is: ", weight/2.2)
else:
    print("Wrong input")
'''
'''
#Using loops
i=0
while i<=5:
    print(i*' * ')
    i=i+1
'''


