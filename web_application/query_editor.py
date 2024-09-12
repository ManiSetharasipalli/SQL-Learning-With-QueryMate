import mysql.connector
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access the variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)


def execute_query(sql_query):
    cursor = connection.cursor()
    cursor.execute(sql_query)
    return cursor


def get_table_list():
    cursor = execute_query("SHOW TABLES")
    tables = cursor.fetchall()
    table_records = []

    for table in tables:
        table_name = table[0]
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        record_count = cursor.fetchone()[0]
        table_records.append({"table_name": table_name, "record_count": record_count})

    cursor.close()
    return table_records
