# Import necessary modules from Flask
from flask import Flask, render_template, request
from flask_mysqldb import MySQL;

# Create a Flask application instance
app = Flask(__name__)

# Configure MySQL connection settings
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'kvsp_paul'

# Initialize MySQL extension
mysql = MySQL(app)

# Define route for handling form submissions
@app.route('/', methods=['GET','POST'])
def index():
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Retrieve data from the form
        username = request.form['name']
        email = request.form['email']

        # Create a cursor object to interact with the database
        cur = mysql.connection.cursor()

        # Execute SQL query to insert data into the database
        cur.execute("INSERT INTO pygo (name, email) VALUES (%s,%s)", (username,email))
        
        # Commit the transaction to save changes
        mysql.connection.commit()

        # Close the cursor
        cur.close()

        # Return a success message to the client
        return "success"
    
    # If the request method is GET, render the form template
    return render_template("Form.html")

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
