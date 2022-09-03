#Function Declaration method
def hello(): #fucntion declaration
    print("Hello ")
    print("Good Afternoon")
 #running only this code won't give output coz hello funnction isn't called
hello() #calling the function

#to input value in a function (Values passed to a function are called arguments)
def hello(name):
    print("Hello",name)
hello("Eshank")

#GenCalci Code
answer=0
def addi(num1,num2): #Addition Function declaration
    answer=num1+num2
    print("Addition is:",answer)

def subs(num1,num2): #Subtraction Function declaration
    answer=num1-num2
    print("Substraction is:",answer)

def multi(num1,num2): #Multiplication Function declaration
    answer=num1*num2
    print("Multiplication is:",answer)

def divi(num1,num2): #Division Function declaration
    answer=num1/num2
    print("Division is:",answer)

no1=int(input("Enter first number:"))
no2=int(input("Enter second number:"))

choice=int(input("Enter Your Choice:")) #

if choice==1:
    addi(no1,no2)
elif choice==2:
    subs(no1,no2)
elif  choice==3:
    multi(no1,no2)
elif choice==4:
    divi(no1,no2)
else:
    print("Invalid Choice")


#Prime number program
a=int(input("Enter a Number"))
temp=False
if a>1:
    for i in range(2,a):
        if a%i==0:
            temp=True
if temp==True:
     print(a, "is prime")
else:
    print(a,"is not prime")


#Reverse program
a=[]
for i in range(5):
    x=int(input("Enter the numbers:"))
    print(a,[x])
    a.append(x)
print("The reversed list is: 1")
a.reverse()
print(a)

#Try Except program
a=int(input("Enter a num"))
try:
    a=a*e
    print(a)
except Exception:
    print(a)

#Zerodiv error
try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Can't divide by Zero")
finally:
    print(a)
    print(b)