# first_number = float(input("Enter your first number "))
# print("+\n-\n*\n/")
# operator = input("Pick an operation: ")
# second_number = float(input("Enter your second number "))
# def add(first_number, second_number):
#     sum =  first_number + second_number
#     return f"The addition of two numbers is {sum}"
# def sub(first_number, second_number):
#     subtract = first_number - second_number
#     return f"The subtraction of two numbers is {subtract}"
# def mul(first_number, second_number):
#     multiply = first_number * second_number
#     return f"The multiplication of two numbers is {multiply}"
# def div(first_number, second_number):
#     division = first_number/second_number
#     return f"The division of two numbers is {division}"
# repeat = True
# while repeat:
#     if operator == "+":
#         output = add(first_number,second_number)
#         print(output)
#     elif operator == "-":
#         output = sub(first_number, second_number)
#         print(output)
#     elif operator == "*":
#         output = mul(first_number, second_number)
#         print(output)
#     elif operator == "/":
#         output = div(first_number, second_number)
#         print(output)
        
#     else:
#         print("Please enter valid operator")
    
#     exit = input(f"Type 'y' to continue calculating with {output} or type 'n' to start new calculation").lower()
#     if exit == "n":
#         repeat = False
#     else:
#         print("Thank for using")


def operations(first_number, second_number):
    if operator == "+":
        output = first_number + second_number
        print(f"The sum of two numbers is {output}")
    elif operator == "-":
        output = first_number - second_number
        print(f"The difference of two numbers is {output}")
    elif operator == "*":
        output = first_number * second_number
        print(f"The multiplication of two numbers is {output}")
    elif operator == "/":
        output = first_number / second_number
        print(f"The division of two numbers is {output}")
    else:
        print("Please enter a valid operator")
    
iscontinue = True
while iscontinue:
    first_number = float(input("Enter your first number ")) 
    print("+\n-\n*\n/")
    operator = input("Pick an operation: ")
    second_number = float(input("Enter your second number "))
    operations(first_number,second_number)
    exit = input(f"Type 'y' to continue calculating or type 'n' to exit ").lower()
    if exit == "y":
        iscontinue = True
    elif exit == "n":
        iscontinue = False
