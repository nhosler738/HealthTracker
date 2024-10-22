from flask import Flask, request, jsonify, render_template
import json
import os
import csv 

app = Flask(__name__)

# File to store calorie data (simulates a database)
DATA_FILE = 'data/calorie_data.json'
CSV_FILE = 'data/calorie_data.csv'

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

# Initialize data file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

  

# Route to serve index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to get the logged calorie data
@app.route('/api/calories', methods=['GET'])
def get_calories():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)



# Route to log new calorie intake
@app.route('/api/calories', methods=['POST'])
def log_calories():
    calorie_data = request.json
    
    # Ensure that we are appending valid calorie entries
    if 'calories' in calorie_data and isinstance(calorie_data['calories'], int):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)

        # Append new calorie entry to the existing data
        data.append(calorie_data)

        # Write updated data back to the JSON file
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f)

        return jsonify({'message': 'Calorie intake logged successfully!'}), 201
    else:
        return jsonify({'error': 'Invalid calorie data'}), 400


# Route to clear all logged calories
@app.route('/api/calories/clear', methods=['DELETE'])
def clear_calories():
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)  # Clear the data

    
    return jsonify({'message': 'Calorie intake cleared successfully!'}), 200




if __name__ == '__main__':
    app.run(debug=True)
