# db_driver.py

import sqlite3
from datetime import datetime

class PersonalAssistantDB:
    def __init__(self, db_name="assistant_data.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        # User Profile Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_profile (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            preferences TEXT
        )
        """)
        # Reminders Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            time TEXT
        )
        """)
        # Notes Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            created_at TEXT
        )
        """)
        self.conn.commit()

    def add_profile(self, name, preferences=""):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO user_profile (name, preferences) VALUES (?, ?)", (name, preferences))
        self.conn.commit()

    def get_profile(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM user_profile LIMIT 1")
        return cursor.fetchone()

    def add_reminder(self, title, time):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO reminders (title, time) VALUES (?, ?)", (title, time))
        self.conn.commit()

    def get_reminders(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM reminders")
        return cursor.fetchall()

    def add_note(self, content):
        cursor = self.conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO notes (content, created_at) VALUES (?, ?)", (content, now))
        self.conn.commit()

    def get_notes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM notes")
        return cursor.fetchall()

    def close(self):
        self.conn.close()
