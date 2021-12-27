import sqlite3


def create_table():
    """Creates new table in the database"""
    sql = """CREATE TABLE city (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country TEXT,
    city TEXT,
    cityID INTEGER 
    );"""

    try:
        cursor.executescript(sql)
    except sqlite3.DatabaseError as err:
        print("Error:", err)
    else:
        print("The table was created")


def add_to_db(values):
    """Adds received data to the database"""
    sql = """INSERT INTO city (country, city, cityID) VALUES (?, ?, ?)"""

    try:
        cursor.executemany(sql, values)
    except sqlite3.DatabaseError as err:
        print("Error:", err)
    else:
        print("Data has been added")


def select_from_db():
    """Retrieves entries from the database"""
    try:
        cursor.execute("SELECT city FROM city WHERE country='Ukraine'")  # gets ukrainian cities from db
    except sqlite3.DatabaseError as err:
        print("Error:", err)
    else:
        entries = cursor.fetchall()
        print("Received data on request: ", entries)


def delete_from_db():
    """Deletes entries from the database"""
    try:
        cursor.execute("DELETE FROM city WHERE Country='Russian Federation'")  # deletes entries from db
    except sqlite3.DatabaseError as err:
        print("Error:", err)
    else:
        print("Data has been deleted")


def update_data():
    """Updates entry in the database"""
    try:
        cursor.execute("UPDATE city set cityID=5000 WHERE id=50")  # sets new value for cityID
    except sqlite3.DatabaseError as err:
        print("Ошибка:", err)
    else:
        print("Data has been updated")


if __name__ == '__main__':
    with open('full_city_list.txt', 'r') as txt_file:  # reads the txt file
        lines = txt_file.read().splitlines()  # reads all text lines from file
        data = [tuple(line.replace('"', '').split(";")) for line in lines]  # creates list of tuples for db

    with sqlite3.connect("mydatabase.db") as con:  # creates new database
        cursor = con.cursor()
        create_table()
        add_to_db(data[1:])
        select_from_db()
        delete_from_db()
        update_data()
