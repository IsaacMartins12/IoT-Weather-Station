import sqlite3
from dotenv import load_dotenv
import os
from datetime import datetime
import json

load_dotenv()

DB_NAME = os.getenv('DB_NAME')

class Database : 

    def __init__(self) :
        print("Database initialized !")

    def initialize_db(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather (
                timestamp TEXT,
                temperature REAL,
                humidity REAL
            )
        ''')
        conn.commit()
        conn.close()

    def insert_data(self,data):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        temperature = data.get("temp")
        humidity = data.get("humidity")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        

        cursor.execute('''
            INSERT INTO weather (timestamp, temperature, humidity)
            VALUES (?, ?, ?)
        ''', (timestamp, temperature, humidity))

        conn.commit()
        conn.close()
