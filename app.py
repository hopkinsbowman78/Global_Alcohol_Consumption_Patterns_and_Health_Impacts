#Import Dependencies
from flask import Flask, request, render_template, redirect, url_for, send_file
import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
from io import BytesIO

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
def fetch_data(entity=None):
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

        # Fetch data for specific entity or all data
        query_alcohol_consumption = "SELECT * FROM alcohol_consumption_per_capita"
        query_gdp = "SELECT * FROM alcohol_consumption_vs_gdp"
        query_mortality = "SELECT * FROM alcohol_related_mortality"

        # Fetch data from each table
        cursor.execute(query_alcohol_consumption)
        data_ac = cursor.fetchall()
        col_names_ac = [desc[0] for desc in cursor.description]

        cursor.execute(query_gdp)
        data_gdp = cursor.fetchall()
        col_names_gdp = [desc[0] for desc in cursor.description]

        cursor.execute(query_mortality)
        data_mortality = cursor.fetchall()
        col_names_mortality = [desc[0] for desc in cursor.description]

        # Create DataFrames from fetched data
        df_ac = pd.DataFrame(data_ac, columns=col_names_ac)
        df_gdp = pd.DataFrame(data_gdp, columns=col_names_gdp)
        df_mortality = pd.DataFrame(data_mortality, columns=col_names_mortality)

        # Merge DataFrames on 'entity' and 'year'
        df_merged_1 = pd.merge(df_ac, df_gdp, on=['entity', 'year', 'alcohol_consumption_per_capita'], how='outer')
        df_global_alcohol = pd.merge(df_merged_1, df_mortality, on=['entity', 'year'], how='outer')

        # Replace None with NaN
        df_global_alcohol = df_global_alcohol.replace({None: np.nan})

        # If a specific entity is requested, filter the DataFrame
        if entity and entity.lower() != 'all':
            df_global_alcohol = df_global_alcohol[df_global_alcohol['entity'].str.lower() == entity.lower()]

        # Drop duplicates if any and return the merged DataFrame
        df_global_alcohol = df_global_alcohol.drop_duplicates(subset=['entity', 'year'])
        return df_global_alcohol

    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of an error

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Fetch unique countries for the dropdown menu or autocomplete
def get_unique_countries():
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

        # Query to get unique entities (countries)
        query = "SELECT DISTINCT entity FROM alcohol_consumption_per_capita"
        cursor.execute(query)
        entities = cursor.fetchall()

        # Convert to a list and sort
        countries = [row[0] for row in entities if row[0] is not None]
        return sorted(countries)

    except Exception as e:
        print(f"Error: {e}")
        return []

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Main route to show dropdown for country selection
@app.route('/', methods=['GET', 'POST'])
def home():
    countries = get_unique_countries()

    if request.method == 'POST':
        selected_country = request.form.get('country')
        if selected_country == 'All':
            return redirect(url_for('show_all_countries'))
        else:
            return redirect(url_for('sort_by_country', country=selected_country))
    
    return render_template("data.html", countries=countries)

# Define the Flask route to show all countries
@app.route('/all-countries', methods=['GET'])
def show_all_countries():
    # Fetch all data (without filtering)
    df_global_alcohol = fetch_data()

    if df_global_alcohol is not None and not df_global_alcohol.empty:
        # Convert the DataFrame to an HTML table
        html_table = df_global_alcohol.to_html(classes='table table-striped', index=False)
        return render_template("data.html", title="Global Alcohol Data - All Countries", table=html_table)
    else:
        return "<p>Failed to fetch data from the database.</p>", 500

# Define the Flask route to sort data by country
@app.route('/sort-by-country/<country>', methods=['GET'])
def sort_by_country(country):
    # Fetch data dynamically based on selected country
    df_global_alcohol = fetch_data(entity=country)

    if df_global_alcohol is not None and not df_global_alcohol.empty:
        # Convert the DataFrame to an HTML table
        html_table = df_global_alcohol.to_html(classes='table table-striped', index=False)
        return render_template("data.html", title=f"Global Alcohol Data - Country: {country}", table=html_table, selected_country=country)
    else:
        return "<p>Failed to fetch data from the database.</p>", 500

# Route to export data to CSV, accepting an optional country parameter
@app.route('/export-data', methods=['GET'])
def export_data():
    # Get the selected country from the query parameter
    country = request.args.get('country', 'All')
    
    # Fetch data based on the selected country
    df_global_alcohol = fetch_data(entity=country)

    if df_global_alcohol is not None and not df_global_alcohol.empty:
        # Convert DataFrame to CSV in memory
        csv_data = BytesIO()
        df_global_alcohol.to_csv(csv_data, index=False)
        csv_data.seek(0)

        # Create a filename based on the country
        filename = f'global_alcohol_data_{country.lower().replace(" ", "_")}.csv'

        # Send the file as a downloadable response
        return send_file(
            csv_data,
            mimetype='text/csv',
            as_attachment=True,
            download_name=filename
        )
    else:
        return "<p>No data available for export.</p>", 500

# Main driver function
if __name__ == '__main__':
    app.run(debug=True)