"""
* Name         : populate_db.py
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
from datetime import datetime, timedelta
def insert_location(county_name, state, latitude, longitude):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
#Checking if lcation exists
    cursor.execute("SELECT id FROM Location WHERE county_name = ? AND state = ?", (county_name, state))
    result = cursor.fetchone()
    if result:
        location_id = result[0]
    else:
        cursor.execute("INSERT INTO Location (county_name, state, latitude, longitude) VALUES (?, ?, ?, ?)",
                       (county_name, state, latitude, longitude))
        conn.commit()
        location_id = cursor.lastrowid
    conn.close()
    return location_id
def insert_precipitation(location_id, start_date, days, min_precip, max_precip):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    for i in range(days):
        date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
        precipitation = round(min_precip + (max_precip - min_precip) * (i / days), 2)
        cursor.execute("INSERT INTO Precipitation (location_id, date, precipitation_mm) VALUES (?, ?, ?)",
                       (location_id, date, precipitation))
    conn.commit()
    conn.close()
    print(f"Inserted precipitation data for {days} days!")
if __name__ == "__main__":
    start_date = datetime(2025, 2, 1)
# Insert locations
    loc1 = insert_location("Polk County", "Iowa", 40.7128, -74.0060)
    loc2 = insert_location("Oklahoma County", "Oklahoma", 34.0522, -118.2437)
# Insert precipitation data for 30 days
    insert_precipitation(loc1, start_date, 30, 0.5, 10.0)
    insert_precipitation(loc2, start_date, 30, 0.2, 8.0)
