from flask import Flask, render_template, request, redirect, url_for, send_file
from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv
from io import BytesIO

# Load environment variables
load_dotenv()

# Database connection parameters
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_port = os.getenv('DB_PORT')

# Create the database connection string
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

app = Flask(__name__)

# Function to fetch unique countries for dropdown
def get_unique_countries():
    try:
        # Query to get unique countries
        query = 'SELECT DISTINCT "Entity" FROM alcohol_consumption_vs_gdp'
        df_countries = pd.read_sql(query, engine)
        
        # Extract unique country names as a list
        countries = df_countries['Entity'].dropna().sort_values().tolist()
        print("Fetched countries list:", countries)  # Debugging statement to verify countries list
        
        return countries
    except Exception as e:
        print(f"Error fetching countries: {e}")
        return []

# Route to display data with an optional country filter
@app.route('/', methods=['GET', 'POST'])
def index():
    # Fetch list of unique countries for dropdown
    countries = get_unique_countries()
    print("Countries passed to template:", countries)  # Verify countries list

    # Set default selection to "All"
    selected_country = "All"
    
    if request.method == 'POST':
        # Get the selected country from the form submission
        selected_country = request.form.get('country')
        print("Selected country:", selected_country)  # Debugging statement to verify selected country

    try:
        # Query the tables and load data into DataFrames
        query_gdp = 'SELECT * FROM alcohol_consumption_vs_gdp'
        df_gdp = pd.read_sql(query_gdp, engine)

        query_mortality = 'SELECT * FROM alcohol_related_mortality'
        df_mortality = pd.read_sql(query_mortality, engine)

        # Merge data on 'Entity' and 'Year' if columns exist
        if 'Entity' in df_gdp.columns and 'Entity' in df_mortality.columns and \
           'Year' in df_gdp.columns and 'Year' in df_mortality.columns:
            df_combined = pd.merge(df_gdp, df_mortality, on=['Entity', 'Year'], how='outer')
        else:
            df_combined = pd.concat([df_gdp, df_mortality], axis=0, ignore_index=True)
            print("Warning: Columns 'Entity' or 'Year' not found in both tables; data combined without merge.")

        # Filter by selected country if not "All"
        if selected_country != "All":
            df_combined = df_combined[df_combined['Entity'] == selected_country]

        # Store the combined DataFrame as a global variable for download
        global last_df_combined
        last_df_combined = df_combined

        # Convert DataFrame to HTML table
        table_html = df_combined.to_html(classes='table table-striped', index=False)

        return render_template("index.html", table=table_html, countries=countries, selected_country=selected_country)

    except Exception as e:
        return f"An error occurred while fetching data: {e}"

# Route to download the current DataFrame as CSV
@app.route('/download')
def download_csv():
    # Use the last filtered DataFrame for download
    if last_df_combined is not None:
        csv_data = BytesIO()
        last_df_combined.to_csv(csv_data, index=False)
        csv_data.seek(0)

        # Create a filename based on the current selection
        selected_country = request.args.get('country', 'All')
        filename = f'global_alcohol_data_{selected_country.lower().replace(" ", "_")}.csv'

        return send_file(
            csv_data,
            mimetype='text/csv',
            as_attachment=True,
            download_name=filename
        )
    else:
        return "<p>No data available for download.</p>", 500

if __name__ == '__main__':
    app.run(debug=True)



