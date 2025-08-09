# main_app.py

import customtkinter

# --- UI Setup ---
app = customtkinter.CTk()
app.title("Simple Calculator")
app.geometry("350x300")

# --- Widgets ---

# Row 0: Operation selection
label_op = customtkinter.CTkLabel(app, text="1. Choose Operation:")
label_op.grid(row=0, column=0, padx=10, pady=10, sticky="w")
operation_menu = customtkinter.CTkOptionMenu(app, values=["add", "subtract", "multiply", "divide"])
operation_menu.grid(row=0, column=1, padx=10, pady=10)

# Row 1: Number 1 input
label_num1 = customtkinter.CTkLabel(app, text="2. Enter First Number:")
label_num1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_num1 = customtkinter.CTkEntry(app)
entry_num1.grid(row=1, column=1, padx=10, pady=10)

# Row 2: Number 2 input
label_num2 = customtkinter.CTkLabel(app, text="3. Enter Second Number:")
label_num2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_num2 = customtkinter.CTkEntry(app)
entry_num2.grid(row=2, column=1, padx=10, pady=10)

# Row 3: Calculate Button
# The 'command' will be added later to connect the logic
calculate_button = customtkinter.CTkButton(app, text="Calculate")
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

# Row 4: Result Display
result_label = customtkinter.CTkLabel(app, text="Result: ", font=("Arial", 16))
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# --- Main Loop ---
app.mainloop()