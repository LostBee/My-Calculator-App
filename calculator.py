#Ask the user to choose an operation
operation = input("What do you want to do? (add, subtract, multiply, divide): ")

# Get the numbers
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

#Decide which operation to perform
if operation == "add":
    print(f"{x}+{y} = {x+y}")
elif operation == "subtract":
     print(f"{x}+{y} = {x+y}")
elif operation == "multiply":
      print(f"{x}+{y} = {x+y}")
elif operation == "divide":
      print(f"{x}+{y} = {x+y}")
else:
    print("Invalid Operation")