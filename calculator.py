#Ask the user to choose an operation
operation = input("What do you want to do? (add, subtract, multiply, divide): ")


# Let's make it better to stop it from crashing if input isn't an integer"
# Get the numbers
try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))

#This only runs if user enters something stupid
except ValueError:
    print("Error: You must enter valid numbers. Don't play with it")

#If no errors, this runs as usual
#Decide which operation to perform

else:   
    if operation == "add":
        print(f"{x}+{y} = {x+y}")
    elif operation == "subtract":
        print(f"{x}-{y} = {x-y}")
    elif operation == "multiply":
        print(f"{x}*{y} = {x*y}")
    elif operation == "divide":
        print(f"{x}/{y} = {x/y}")
    else:
        print("Invalid Operation")