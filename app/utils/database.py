import os

import mysql.connector
from dotenv import load_dotenv
from fastapi import HTTPException
from mysql.connector import Error

load_dotenv()


db_connection = None


def init_db():
    """
    Initialize the global database connection.
    """
    global db_connection
    try:
        db_connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"),
        )
    except Error as e:
        db_connection = None
        raise HTTPException(status_code=500, detail="Failed to connect to the database")


def close_db():
    """
    Close the global database connection.
    """
    global db_connection
    if db_connection and db_connection.is_connected():
        db_connection.close()


async def fetch_data(query, params: tuple = ()):
    """
    Fetch data from the database using the global connection.
    """
    global db_connection
    if db_connection is None or not db_connection.is_connected():
        raise HTTPException(
            status_code=500, detail="Database connection is not established"
        )

    cursor = None
    try:
        cursor = db_connection.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        return results
    except Error as e:
        raise RuntimeError(f"Error executing query: {e}")
    finally:
        if cursor:
            cursor.close()


def insert_data(query, data):
    """
    Insert data into the database using the global connection.
    """
    global db_connection
    if db_connection is None or not db_connection.is_connected():
        raise HTTPException(
            status_code=500, detail="Database connection is not established"
        )

    cursor = None
    try:
        cursor = db_connection.cursor()
        cursor.execute(query, data)
        db_connection.commit()
        return True
    except Error as e:
        raise RuntimeError(f"Error inserting data: {e}")
    finally:
        if cursor:
            cursor.close()
