from flask import Flask, request, render_template
import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Database connection parameters from environment variables
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_port = os.getenv('DB_PORT')

# Function to connect to the PostgreSQL database and fetch merged data
def fetch_data():
    try:
        # Connect to PostgreSQL database
        connection = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port
        )
        
        # Create a cursor object
        cursor = connection.cursor()

        # Execute SQL queries to get data from all three tables
        query_alcohol_consumption_per_capita = "SELECT * FROM alcohol_consumption_per_capita"
        query_alcohol_consumption_vs_gdp = "SELECT * FROM alcohol_consumption_vs_gdp"
        query_alcohol_related_mortality = "SELECT * FROM alcohol_related_mortality"

        # Fetch alcohol_consumption_per_capita data
        cursor.execute(query_alcohol_consumption_per_capita)
        data_alcohol_consumption_per_capita = cursor.fetchall()
        col_names_alcohol_consumption_per_capita = [desc[0] for desc in cursor.description]

        # Fetch alcohol_consumption_vs_gdp data
        cursor.execute(query_alcohol_consumption_vs_gdp)
        data_alcohol_consumption_vs_gdp = cursor.fetchall()
        col_names_alcohol_consumption_vs_gdp = [desc[0] for desc in cursor.description]

        # Fetch alcohol_related_mortality data
        cursor.execute(query_alcohol_related_mortality)
        data_alcohol_related_mortality = cursor.fetchall()
        col_names_alcohol_related_mortality = [desc[0] for desc in cursor.description]

        # Create Pandas DataFrames from the fetched data
        df_alcohol_consumption_per_capita = pd.DataFrame(data_alcohol_consumption_per_capita, columns=col_names_alcohol_consumption_per_capita)
        df_alcohol_consumption_vs_gdp = pd.DataFrame(data_alcohol_consumption_vs_gdp, columns=col_names_alcohol_consumption_vs_gdp)
        df_alcohol_related_mortality = pd.DataFrame(data_alcohol_related_mortality, columns=col_names_alcohol_related_mortality)
        
        # Merge DataFrames on common columns ('entity', 'year')
        df_merged_1 = pd.merge(df_alcohol_consumption_per_capita, df_alcohol_consumption_vs_gdp, on=['entity', 'year', 'alcohol_consumption_per_capita'], how='outer')
        df_global_alcohol = pd.merge(df_merged_1, df_alcohol_related_mortality, on=['entity', 'year'], how='outer')

        return df_global_alcohol

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Define the Flask route to show all countries
@app.route('/all-countries', methods=['GET'])
def show_all_countries():
    # Fetch the merged data
    df_global_alcohol = fetch_data()

    if df_global_alcohol is not None:
        # Convert the DataFrame to an HTML table
        html_table = df_global_alcohol.to_html(classes='table table-striped', index=False)
        return render_template("data.html", title="Global Alcohol Data - All Countries", table=html_table)
    else:
        return "<p>Failed to fetch data from the database.</p>", 500

# Define the Flask route to sort data by country
@app.route('/sort-by-country', methods=['GET'])
def sort_by_country():
    country = request.args.get('country')
    if not country:
        return "<p>Please provide a country parameter.</p>", 400

    # Fetch the merged data
    df_global_alcohol = fetch_data()

    if df_global_alcohol is not None:
        # Filter data by the specified country
        filtered_data = df_global_alcohol[df_global_alcohol['entity'].str.contains(country, case=False, na=False)]

        # Convert the filtered DataFrame to an HTML table
        html_table = filtered_data.to_html(classes='table table-striped', index=False)
        return render_template("data.html", title=f"Global Alcohol Data - Country: {country}", table=html_table)
    else:
        return "<p>Failed to fetch data from the database.</p>", 500

# Main driver function
if __name__ == '__main__':
    app.run(debug=True)

