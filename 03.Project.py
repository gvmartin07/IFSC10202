#prompt for 2 numbers
# prompt for opertator 
# if +, -, *, / else invalid operator
# print num1 operator num2 = solution
num1 = float(input("Enter first number: "))
op = input("Enter Operator (+, -, *, /): ")
num2 = float(input("Enter seond number: "))
if op != "+" and op != "-" and op != "*" and op != "/":
    print("Invalid operator")
#if its addition
if op == "+":
    sum = num1+num2
    print(f"{num1} + {num2} = {sum}")
#if its subtraction
if op == "-":
    sum = num1-num2
    print(f"{num1} - {num2} = {sum}")
#if its multiplication
if op == "*":
    sum = num1*num2
    print(f"{num1} * {num2} = {sum}")
#if its division
if op == "/":
    sum = num1/num2
    print(f"{num1} / {num2} = {sum}")