"""
print("zad1")
n=int(input("Enter a amount: "))
if n>0:
    max=0
    for i in range(0,n):
        x=int(input("Enter a number: "))
        if x>max:
            max=x
    print("The largest number is:", max)

else:
    print("the number should be more than 0")
"""

"""
print("zad2")
n=int(input("Enter a amount: "))
sbor=0
for i in range(0,n):
    x=int(input("Enter a number: "))
    sbor+=x
print("The sum of the numbers is:", sbor)

"""

"""
print("zad3")
n=int(input("Enter a number: "))
for i in range(1,n+1):
    print("*"*i)
"""
"""
import math
print("zad4")
n=int(input("Enter a number: "))
prime = True
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        prime = False
        break
if(prime==True):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
"""

    
"""
print("zad5")
n=int(input("Enter a number: "))
match n:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid number. Please enter a number between 1 and 7.")
"""
"""
print("zad6")
n=int(input("Enter a number: "))
if 1 <= n <= 10:
    print("The number is between 1 and 10")
else:
    print("The number is not between 1 and 10")
"""

"""
print("zad7")
x=float(input("Enter a 1st number: "))
operator=input("Enter an operator (+, -, *, /): ")
y=float(input("Enter a 2 number: "))
match operator:
    case "+":
        print(f"{x} + {y} = {x+y}")
    case "-":
        print(f"{x} - {y} = {x-y}")
    case "*":
        print(f"{x} * {y} = {x*y}")
    case "/":
        if y != 0:
            print(f"{x} / {y} = {x/y}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operator")
"""

"""
print("zad8")
min=int(input("Enter a lower bound: "))
max=int(input("Enter an upper bound: "))
if min>max:
    print("The lower bound should be less than or equal to the upper bound.")
sum=0
for i in range(0, 10):
    x=int(input(f"Enter a number {i+1}: "))
    if min<=x<=max:
        sum+=1
print(f"The count of numbers between {min} and {max} is: {sum}")
"""




