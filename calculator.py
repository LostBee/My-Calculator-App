# It's function time!!
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiple (x,y):
    return x*y
def divide (x,y):
    if y==0:
        return "Dude, you can't divide by zero!"
    return x/y
    
# Main logic
# Let's make it a loop as I have to run it again and again
def main():
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
            continue #to skip the rest and start a new one

        #If no errors, this runs as usual
        #Decide which operation to perform

        if operation == "add":
            result = add(x, y)
        elif operation == "subtract":
            result = subtract(x, y)
        elif operation == "multiply":
            result = multiply(x, y)
        elif operation == "divide":
            result = divide(x, y)
        else:
            result = "Invalid operation."
        
        print (f"{x}+{y}={result}")
        
        #This runs for the subsequent tries
        another = input("Do you wanna try again?(Y/N): ")
        if another.lower() not in ["y", "yes"]:
            print("Ciao")
            break

# To run the main() fuction
if __name__ == "__main__":
    main()