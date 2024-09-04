import mysql.connector
from mysql.connector import Error


def init_db():
    """
    Initialize the database connection.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost", user="admin", password="admin", database="ezenplo_db"
        )
        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def close_db(connection):
    """
    Close the database connection.
    """
    if connection.is_connected():
        connection.close()
        print("Database connection closed.")


def fetch_data(query):
    """
    Fetch data from the database.
    """
    connection = init_db()
    if connection is None:
        return None

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f"Error executing query: {e}")
    finally:
        cursor.close()
        close_db(connection)


def insert_data(query, data):
    """
    Insert data into the database.
    """
    connection = init_db()
    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        print(f"{cursor.rowcount} record(s) inserted.")
        return True
    except Error as e:
        print(f"Error inserting data: {e}")
        return False
    finally:
        cursor.close()
        close_db(connection)
