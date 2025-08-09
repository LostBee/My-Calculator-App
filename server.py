# server.py

# Import the tools we need
from flask import Flask, request, jsonify
from flask_cors import CORS
import calculator #logic files

# Flash application instance
app = Flash(__name__)

#Enable CORS to allow FE to talk to server
CORS(app)

#Defining API endpoint
@app.route('/api/calculate',method=['POST']
def calculate():
    #Getting JSON data sent by FE
    data = request.get_json()
    
    #Get values from the data
    operation = data.get('operation')
    x=data.get('num1')
    y=data.get('num2')
    
    #basic validation
    if x is None or y is None:
        return jsonify({'error': 'Those are not numbers'}), 400
        
    #Calling functions from the calculator
    if operation == "add":
        result = calculator.add(x,y)
    elif operation == "subtract":
        result = calculator.subtract(x, y)
    elif operation == "multiply":
        # Using the 'multiple' function name from the file
        result = calculator.multiple(x, y)
    elif operation == "divide":
        result = calculator.divide(x, y)
    else:
        result = "Invalid operation"
        
    #Return the result in JSON format
    return jsonfiy({'result':result})