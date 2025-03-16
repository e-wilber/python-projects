"""
* Name         : visualize_data.py
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
import matplotlib.pyplot as plt
def fetch_precipitation():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT Location.county_name, Precipitation.date, Precipitation.precipitation_mm 
        FROM Precipitation 
        JOIN Location ON Precipitation.location_id = Location.id
        ORDER BY Precipitation.date
    ''')
    data = cursor.fetchall()
    conn.close()
    return data
def plot_precipitation(data):
    counties = {}
    for county, date, precipitation in data:
        if county not in counties:
            counties[county] = {"dates": [], "precipitation": []}
        counties[county]["dates"].append(date)
        counties[county]["precipitation"].append(precipitation)
    plt.figure(figsize=(10, 5))
    for county, values in counties.items():
        plt.plot(values["dates"], values["precipitation"], marker='o', label=county)
    plt.xlabel("DATE")
    plt.ylabel("PRECIPITATION")
    plt.title("30-Day PRECIPITATION DATA")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    data = fetch_precipitation()
    plot_precipitation(data)
