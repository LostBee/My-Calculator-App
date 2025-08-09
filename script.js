// Get references to all the important HTML elements
const operationMenu = document.getElementById('operation');
const num1Input = document.getElementById('num1');
const num2Input = document.getElementById('num2');
const calculateBtn = document.getElementById('calculateBtn');
const resultDisplay = document.getElementById('resultDisplay');

// Add a 'click' event listener to the button
calculateBtn.addEventListener('click', () => {
    // This function now sends data to the Python backend

    const operation = operationMenu.value;
    const x = parseFloat(num1Input.value);
    const y = parseFloat(num2Input.value);

    // Validate numbers before sending
    if (isNaN(x) || isNaN(y)) {
        resultDisplay.textContent = "Result: Please enter valid numbers.";
        return;
    }

    // 1. Package the data into a JavaScript object
    const dataToSend = {
        operation: operation,
        num1: x,
        num2: y
    };

    // 2. Use the fetch API to send a POST request to our Flask server
    fetch('http://127.0.0.1:5000/api/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dataToSend) // Convert the JS object to a JSON string
    })
    .then(response => response.json()) // Parse the JSON response from the server
    .then(data => {
        // 3. Update the display with the result received from Python
        resultDisplay.textContent = `Result: ${data.result}`;
    })
    .catch(error => {
        // 4. Handle errors if the server is down or there's a network problem
        console.error('Error:', error);
        resultDisplay.textContent = "Result: Could not connect to server.";
    });
});