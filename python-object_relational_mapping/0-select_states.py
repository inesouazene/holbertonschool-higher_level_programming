#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == "__main__":

    def main():
    # Retrieve command-line arguments
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        db_name = sys.argv[3]

        # Connect to MySQL database
        db = MySQLdb.connect(host="localhost",
                            user=mysql_username,
                            passwd=mysql_password,
                            db=db_name,
                            port=3306)

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute SQL query to retrieve all states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all results from the executed query
        results = cursor.fetchall()

        # Print each row in the results
        for row in results:
            print(row)

        # Close the cursor and database connection
        cursor.close()
        db.close()
