# sqli_blatant.py

import sqlite3
import os

def get_user_data(username: str):
    """
    Connects to a database and retrieves user data using a raw,
    unparameterized query. This is a textbook SQL Injection vulnerability.
    """
    db_connection = sqlite3.connect(":memory:")
    cursor = db_connection.cursor()
    
    # Create a dummy table for the example
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, role TEXT)")
    cursor.execute("INSERT INTO users (username, role) VALUES ('admin', 'administrator')")
    db_connection.commit()

    # VULNERABILITY: The user input is formatted directly into the query string.
    # A SAST scanner should immediately flag this line.
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    print(f"Executing query: {query}")

    try:
        # SINK: The tainted query string is executed by the database driver.
        cursor.execute(query)
        result = cursor.fetchone()
        
        if result:
            print(f"Found user: {result}")
        else:
            print("User not found.")
            
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        db_connection.close()

if __name__ == "__main__":
    # SOURCE: The input() function provides untrusted user data.
    user_input = input("Enter username to search: ")
    get_user_data(user_input)
