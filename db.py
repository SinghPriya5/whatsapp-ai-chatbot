import sqlite3

def init_db():
    conn = sqlite3.connect("bookings.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        service TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_booking(name, service, date):
    conn = sqlite3.connect("bookings.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO bookings (name, service, date) VALUES (?, ?, ?)",
        (name, service, date)
    )

    conn.commit()
    conn.close()