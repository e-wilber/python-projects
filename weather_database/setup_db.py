"""
* Name         : setup_db.py
* Author       : E Wilber
* Created      : 03/03/25
* Module       : 7
* Topic        : 1 - 4
* Description  : Database with Tables
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
import sqlite3
def create_database():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
#Forcing drop existing tables to avoid problems
    cursor.execute("DROP TABLE IF EXISTS Location")
    cursor.execute("DROP TABLE IF EXISTS Precipitation")
#Creating Location table
    cursor.execute('''
        CREATE TABLE Location (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            county_name TEXT NOT NULL,
            state TEXT NOT NULL,
            latitude REAL,
            longitude REAL
        )
    ''')
#Creating Precipitation table
    cursor.execute('''
        CREATE TABLE Precipitation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location_id INTEGER,
            date TEXT NOT NULL,
            precipitation_mm REAL,
            FOREIGN KEY (location_id) REFERENCES Location (id)
        )
    ''')
    conn.commit()
    conn.close()
    print("Database and tables created successfully!")
if __name__ == "__main__":
    create_database()
