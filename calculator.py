
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
