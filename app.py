from flask import Flask, render_template
import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

app = Flask(__name__)

# Load environment variables from the .env file
load_dotenv()

# Function to connect to PostgreSQL database and fetch data
def fetch_data():
    # Fetch environment variables
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_port = os.getenv('DB_PORT')

    connection = None
    cursor = None

    try:
        # Connect to PostgreSQL database
        connection = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port
        )
        cursor = connection.cursor()

        # Execute a SQL query
        query = "SELECT * FROM campaign"  # Replace with your actual table name
        cursor.execute(query)

        # Fetch the data
        data = cursor.fetchall()

        # Fetch the column names
        col_names = [desc[0] for desc in cursor.description]

        # Create a Pandas DataFrame from the fetched data
        df = pd.DataFrame(data, columns=col_names)

        return df

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Route to display the DataFrame in an HTML page
@app.route('/')
def index():
    df = fetch_data()
    if df is not None:
        # Convert DataFrame to HTML and pass it to the template
        return render_template('data.html', tables=df.to_html(classes='data', header="true"))
    else:
        return 'Error fetching data', 500

if __name__ == '__main__':
    app.run(debug=True)
