# from flask import Flask, render_template
# import psycopg2
# from dotenv import load_dotenv
# import os
# import pandas as pd

# app = Flask(__name__)

# # Load environment variables from the .env file
# load_dotenv()

# # Function to connect to PostgreSQL database and fetch data
# def fetch_data():
#     # Fetch environment variables
#     db_host = os.getenv('DB_HOST')
#     db_name = os.getenv('DB_NAME')
#     db_user = os.getenv('DB_USER')
#     db_password = os.getenv('DB_PASSWORD')
#     db_port = os.getenv('DB_PORT')

#     connection = None
#     cursor = None

#     try:
#         # Connect to PostgreSQL database
#         connection = psycopg2.connect(
#             host=db_host,
#             database=db_name,
#             user=db_user,
#             password=db_password,
#             port=db_port
#         )
#         cursor = connection.cursor()

#         # Execute a SQL query
#         query = "SELECT * FROM campaign"  # Replace with your actual table name
#         cursor.execute(query)

#         # Fetch the data
#         data = cursor.fetchall()

#         # Fetch the column names
#         col_names = [desc[0] for desc in cursor.description]

#         # Create a Pandas DataFrame from the fetched data
#         df = pd.DataFrame(data, columns=col_names)

#         return df

#     except Exception as e:
#         print(f"Error: {e}")
#         return None

#     finally:
#         # Close the cursor and connection
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Route to display the DataFrame in an HTML page
# @app.route('/')
# def index():
#     df = fetch_data()
#     if df is not None:
#         # Convert DataFrame to HTML and pass it to the template
#         return render_template('data.html', tables=df.to_html(classes='data', header="true"))
#     else:
#         return 'Error fetching data', 500

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template
import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

app = Flask(__name__)

# Load environment variables from the .env file
load_dotenv()

# Function to connect to PostgreSQL database and fetch data from three tables
def fetch_merged_data():
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

        # Queries to fetch data from all three tables
        query_consumption_gdp = "SELECT * FROM consumption_gdp"
        query_fraction_of_mortality = "SELECT * FROM fraction_of_mortality"
        query_per_capita_litres = "SELECT * FROM per_capita_litres"

        # Fetch consumption_gdp data
        cursor.execute(query_consumption_gdp)
        data_consumption_gdp = cursor.fetchall()
        col_names_consumption_gdp = [desc[0] for desc in cursor.description]

        # Fetch fraction_of_mortality data
        cursor.execute(query_fraction_of_mortality)
        data_fraction_of_mortality = cursor.fetchall()
        col_names_fraction_of_mortality = [desc[0] for desc in cursor.description]

        # Fetch per_capita_litres data
        cursor.execute(query_per_capita_litres)
        data_per_capita_litres = cursor.fetchall()
        col_names_per_capita_litres = [desc[0] for desc in cursor.description]

        # Create Pandas DataFrames from the fetched data
        df_consumption_gdp = pd.DataFrame(data_consumption_gdp, columns=col_names_consumption_gdp)
        df_fraction_of_mortality = pd.DataFrame(data_fraction_of_mortality, columns=col_names_fraction_of_mortality)
        df_per_capita_litres = pd.DataFrame(data_per_capita_litres, columns=col_names_per_capita_litres)

        # Merge DataFrames on common columns ('entity', 'code', and 'year')
        df_merged_1 = pd.merge(df_consumption_gdp, df_fraction_of_mortality, on=['entity', 'code', 'year'], how='outer')
        df_merged_final = pd.merge(df_merged_1, df_per_capita_litres, on=['entity', 'code', 'year'], how='outer')

        return df_merged_final

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Route to display the merged DataFrame in an HTML page
@app.route('/')
def index():
    df = fetch_merged_data()  # Fetch the merged data
    if df is not None:
        # Convert DataFrame to HTML and pass it to the template
        return render_template('data.html', tables=df.to_html(classes='data', header="true"))
    else:
        return 'Error fetching data', 500

if __name__ == '__main__':
    app.run(debug=True)

