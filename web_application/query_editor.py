import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='************',
    database='online_shopping'
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
