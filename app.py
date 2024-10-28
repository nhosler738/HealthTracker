from flask import Flask, request, jsonify, render_template
import flaskr.db as db 
from flaskr.work_session import work_session

app = Flask(__name__)

# Database initialization
app.config['DATABASE'] = 'data/healthtracker.db'
db.init_app(app=app)

# Route to serve index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to serve calorie.html
@app.route('/calorie')
def calorie_page():
    return render_template('calorie.html')

# Route to get the logged calorie data
@app.route('/api/calories', methods=['GET'])
def get_calories():
    databaseConnection = db.get_db()
    cursor = databaseConnection.cursor()
    sql = "SELECT calories, log_time FROM calories_log"  # Make sure to select log_time
    cursor.execute(sql)
    entries = cursor.fetchall()

    # Convert entries to a list of dictionaries
    data = [{'calories': entry[0], 'log_time': entry[1]} for entry in entries]  # Adjusted indexing
    return jsonify(data)

# Route to log new calorie intake
@app.route('/api/calories', methods=['POST'])
def log_calories():
    calorie_data = request.json
    
    # Ensure that we are appending valid calorie entries
    if 'calories' in calorie_data and isinstance(calorie_data['calories'], int):
        new_entry = (
            calorie_data['calories'],
            calorie_data.get('date', 'Unknown')
        )

        # Log calorie data in sqlite3 database
        databaseConnection = db.get_db()
        sql = "INSERT INTO calories_log (calories, log_time) VALUES (?, ?)"  # Adjusted to match your table structure
        cursor = databaseConnection.cursor()
        cursor.execute(sql, new_entry)
        databaseConnection.commit()
        return jsonify({'message': 'Calories logged successfully'}), 201  # Added success response
    return jsonify({'error': 'Invalid data'}), 400  # Error handling for invalid data

# Route to clear all logged calories
@app.route('/api/calories/clear', methods=['DELETE'])
def clear_calories():
    databaseConnection = db.get_db()  # Get the database connection
    cur = databaseConnection.cursor()
    
    # Clear all entries from the calories_log table
    cur.execute("DELETE FROM calories_log")  # Adjusted the table name
    databaseConnection.commit()  # Commit the transaction
    return jsonify({'message': 'Calories cleared successfully'}), 200  # Added success response


# WORK TIMER SECTION

# store work sessions in memory
work_session_list = []

# save work session preferences to initialize a work session 
# only one session at a time 
@app.route('api/work-session/save-preferences', methods=['POST'])
def save_preferences():
    data = request.get_json()
    work_tabs = data.get("tabs", [])
    work_apps = data.get("apps", [])
    session_goals = ""
    name = ""

    # if a session already in the list return error message
    if len(work_session_list) > 0:
        work_session_error_html = """
        <div id="work-form-error">
            You can only have one work session running at a time. 
        </div"""
    else:
        new_work_session = work_session(work_list=work_tabs, app_list=work_apps,
                                        name=name, session_goals=session_goals)

    





if __name__ == '__main__':
    app.run(debug=True)
