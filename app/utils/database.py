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
            return connection
    except Error:
        return None


def close_db(connection):
    """
    Close the database connection.
    """
    if connection.is_connected():
        connection.close()


async def fetch_data(query):
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
        raise RuntimeError(f"Error executing query: {e}")
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
        return True
    except Error as e:
        raise RuntimeError(f"Error inserting data: {e}")
    finally:
        cursor.close()
        close_db(connection)
