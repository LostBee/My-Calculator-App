# Let's make it a loop as I have to run it again and again
while True:
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
        if operation.lower() == "add":
            print(f"{x}+{y} = {x+y}")
        elif operation.lower() == "subtract":
            print(f"{x}-{y} = {x-y}")
        elif operation.lower() == "multiply":
            print(f"{x}*{y} = {x*y}")
        elif operation.lower() == "divide":
            print(f"{x}/{y} = {x/y}")
        else:
            print("Invalid Operation")
    
    #This runs for the subsequent tries
    another = input("Do you wanna try again?(Y/N): ")
    if another.lower() not in ["y", "yes"]:
        print("Ciao")
        break