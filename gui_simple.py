# gui_simple.py

import customtkinter
import calculator  # <-- 1. IMPORT YOUR LOGIC FILE

# --- Handler Function ---
# This function acts as the bridge between your UI and your logic
def handle_calculation():
    # Get the current values from the UI widgets
    operation = operation_menu.get()
    num1_str = entry_num1.get()
    num2_str = entry_num2.get()
    
    try:
        x = int(num1_str)
        y = int(num2_str)

        # Call the correct function from your imported calculator.py file
        if operation == "add":
            result = calculator.add(x, y)
        elif operation == "subtract":
            result = calculator.subtract(x, y)
        elif operation == "multiply":
            # Calling the 'multiple' function to match the name in your file
            result = calculator.multiple(x, y) 
        elif operation == "divide":
            result = calculator.divide(x, y)
        else:
            result = "Invalid operation"
            
        # Update the result label on the screen with the outcome
        result_label.configure(text=f"Result: {result}")

    except ValueError:
        # Handle cases where input is not a valid number
        result_label.configure(text="Error: Please enter valid numbers")

# --- UI Setup ---
app = customtkinter.CTk()
app.title("Simple Calculator")
app.geometry("350x300")

# --- Widgets ---
# (The widget creation code is the same as before)

# Operation selection
label_op = customtkinter.CTkLabel(app, text="1. Choose Operation:")
label_op.grid(row=0, column=0, padx=10, pady=10, sticky="w")
operation_menu = customtkinter.CTkOptionMenu(app, values=["add", "subtract", "multiply", "divide"])
operation_menu.grid(row=0, column=1, padx=10, pady=10)

# Number 1 input
label_num1 = customtkinter.CTkLabel(app, text="2. Enter First Number:")
label_num1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_num1 = customtkinter.CTkEntry(app)
entry_num1.grid(row=1, column=1, padx=10, pady=10)

# Number 2 input
label_num2 = customtkinter.CTkLabel(app, text="3. Enter Second Number:")
label_num2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_num2 = customtkinter.CTkEntry(app)
entry_num2.grid(row=2, column=1, padx=10, pady=10)

# Calculate Button
# <-- 2. CONNECT THE BUTTON TO THE HANDLER FUNCTION
calculate_button = customtkinter.CTkButton(app, text="Calculate", command=handle_calculation)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

# Result Display
result_label = customtkinter.CTkLabel(app, text="Result: ", font=("Arial", 16))
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# --- Main Loop ---
app.mainloop()