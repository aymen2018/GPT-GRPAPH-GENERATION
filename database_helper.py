import mysql.connector
from mysql.connector import Error
import os


class DatabaseHelper:

    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "riseup"
        self.password = os.getenv("DB_PASSWORD", "riseup")
        self.database = "riseup"

    def connect_to_database(self):
        """Establish a connection with the local riseup database."""
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            if conn.is_connected():
                return conn
            else:
                return None
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            raise

    def execute_query(self, query):
        """Execute the provided SQL query and return the result."""
        try:
            conn = self.connect_to_database()
            if conn and conn.is_connected():
                # Create a cursor to execute SQL queries
                cursor = conn.cursor()

                # Execute the provided query
                cursor.execute(query)

                # Fetch all the results
                result = cursor.fetchall()

                # Get column names for better formatting
                column_names = [column[0] for column in cursor.description]
                data = [dict(zip(column_names, row)) for row in result]
                return data
        except Error as e:
            print(f"Error while executing query: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
