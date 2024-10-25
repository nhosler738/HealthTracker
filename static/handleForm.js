// Function to load the calorie data from the server and display it on the page
function loadCalorieData() {
    fetch('/api/calories')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const calorieList = document.getElementById('calorie-list');
            calorieList.innerHTML = ''; // Clear the current list
            data.forEach(calorie => {
                const listItem = document.createElement('li');
                listItem.textContent = "Calories: " + calorie.calories; // Accessing the calories

                // Create a div to display the date of the calorie log entry
                const dateItem = document.createElement('div');
                dateItem.className = 'log-date';
                dateItem.textContent = "Date: " + new Date(calorie.log_time).toISOString().split('T')[0]; // Use the date from the database
                
                listItem.appendChild(dateItem);
                calorieList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error loading calorie data:', error));
}

// Function to handle the form submission
document.getElementById('calorie-form').addEventListener('submit', function (e) {
    e.preventDefault();  // Prevent form from submitting the traditional way

    const calories = document.getElementById('calories').value;

    // Prepare the data to send
    const calorieData = {
        calories: parseInt(calories),  // Ensure it's a number
        date: new Date().toISOString().split('T')[0] // Send the current date
    };

    // Send the data to the server
    fetch('/api/calories', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(calorieData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            loadCalorieData();  // Reload the list after successful submission
            document.getElementById('calorie-form').reset();  // Clear the form
        } else {
            console.error('Error logging calories:', data.error);
        }
    })
    .catch(error => console.error('Error:', error));
});

// Function to clear all logged calories
document.getElementById('clear-button').addEventListener('click', function () {
    fetch('/api/calories/clear', {
        method: 'DELETE',
    })
    .then(response => {
        if (response.ok) {
            loadCalorieData();  // Reload the list after clearing
            console.log('Calorie intake cleared successfully!');
        } else {
            console.error('Error clearing calories');
        }
    })
    .catch(error => console.error('Error:', error));
});

// Initial load of calorie data when the page loads
loadCalorieData();
