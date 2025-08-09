# server.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import calculator  # Your original logic file

# --- Create the Flask App ---
app = Flask(__name__)
# Enable CORS to allow the frontend to communicate with this server
CORS(app) 

# --- Define the API Endpoint ---
@app.route('/api/calculate', methods=['POST'])
def calculate():
    # Get the JSON data sent from the frontend
    data = request.get_json()

    # Extract the values
    operation = data.get('operation')
    x = data.get('num1')
    y = data.get('num2')

    # Basic validation
    if x is None or y is None:
        return jsonify({'error': 'Missing numbers'}), 400

    # Call the functions from your calculator.py file
    if operation == "add":
        result = calculator.add(x, y)
    elif operation == "subtract":
        result = calculator.subtract(x, y)
    elif operation == "multiply":
        # Using the 'multiple' function name from your file
        result = calculator.multiple(x, y)
    elif operation == "divide":
        result = calculator.divide(x, y)
    else:
        result = "Invalid operation"

    # Return the result in JSON format
    return jsonify({'result': result})

# --- Run the Server ---
if __name__ == '__main__':
    # debug=True makes the server automatically reload when you save changes
    app.run(debug=True)