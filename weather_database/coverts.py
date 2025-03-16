"""
* Name         : converts.py
* Author       : E Wilber
* Created      : 03/03/25
* Module       : 7
* Topic        : 1 - 4
* Description  : Database with Tables
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
import shutil
import sqlite3
from datetime import datetime, timedelta
def copy_database():
    source_db = "weather.db"
    backup_db = "weather_backup.db"
    shutil.copy(source_db, backup_db)
    print(f"Database copied to: {backup_db}!")
def convert_units():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, precipitation_mm FROM Precipitation")
    data = cursor.fetchall()
    for row_id, precipitation in data:
        new_value = round(precipitation * 0.0393701, 2)  # Convert mm to inches
        cursor.execute("UPDATE Precipitation SET precipitation_mm = ? WHERE id = ?", (new_value, row_id))
    conn.commit()
    conn.close()
    print("Converted precipitation values to inches")
def adjust_dates():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, date FROM Precipitation")
    data = cursor.fetchall()
    for row_id, date_str in data:
        new_date = (datetime.strptime(date_str, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
        cursor.execute("UPDATE Precipitation SET date = ? WHERE id = ?", (new_date, row_id))
    conn.commit()
    conn.close()
    print("Moved all dates to one day earlier")
def delete_city(county_name):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Location WHERE county_name = ?", (county_name,))
    result = cursor.fetchone()
    if result:
        location_id = result[0]
        cursor.execute("DELETE FROM Precipitation WHERE location_id = ?", (location_id,))
        cursor.execute("DELETE FROM Location WHERE id = ?", (location_id,))
        conn.commit()
        print(f"Deleted {county_name} and data.")
    else:
        print(f"County {county_name} not found!")
    conn.close()
if __name__ == "__main__":
    copy_database()
    convert_units()
    adjust_dates()
    delete_city("Oklahoma County")
