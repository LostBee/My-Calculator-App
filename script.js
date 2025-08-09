// 1. Get references to all the important HTML elements
const operationMenu = document.getElementById('operation');
const num1Input = document.getElementById('num1');
const num2Input = document.getElementById('num2');
const calculateBtn = document.getElementById('calculateBtn');
const resultDisplay = document.getElementById('resultDisplay');

// 2. Add a 'click' event listener to the button
calculateBtn.addEventListener('click', () => {
    // This function runs whenever the button is clicked

    // 3. Get the current values from the form
    const operation = operationMenu.value;
    const x = parseFloat(num1Input.value);
    const y = parseFloat(num2Input.value);
    
    // 4. Validate the numbers
    if (isNaN(x) || isNaN(y)) {
        resultDisplay.textContent = "Result: Please enter valid numbers.";
        return; // Stop the function here
    }

    // 5. Perform the calculation using a switch statement
    let result;
    switch (operation) {
        case 'add':
            result = x + y;
            break;
        case 'subtract':
            result = x - y;
            break;
        case 'multiply':
            result = x * y;
            break;
        case 'divide':
            if (y === 0) {
                result = "Error: Cannot divide by zero";
            } else {
                result = x / y;
            }
            break;
        default:
            result = "Error: Invalid operation";
    }

    // 6. Display the final result
    resultDisplay.textContent = `Result: ${result}`;
});