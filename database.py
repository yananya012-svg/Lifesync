import sqlite3


DATABASE_NAME = "users.db"


# ==========================================
# CREATE DATABASE TABLES
# ==========================================

def create_database():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    # Users Table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        full_name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password BLOB NOT NULL

    )
    """)



    # Prediction History Table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prediction_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        prediction_type TEXT,

        result TEXT,

        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(user_id) REFERENCES users(id)

    )
    """)



    conn.commit()

    conn.close()



# Create tables when file runs

create_database()



# ==========================================
# ADD NEW USER
# ==========================================

def add_user(
    full_name,
    email,
    password
):

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO users
        (
        full_name,
        email,
        password
        )

        VALUES(?,?,?)

        """,
        (
            full_name,
            email,
            password
        )
    )


    conn.commit()

    conn.close()



# ==========================================
# GET USER BY EMAIL
# ==========================================

def get_user(email):

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *

        FROM users

        WHERE email=?

        """,
        (email,)
    )


    user = cursor.fetchone()


    conn.close()


    return user



# ==========================================
# SAVE PREDICTION HISTORY
# ==========================================

def save_prediction(
        user_id,
        prediction_type,
        result
):

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO prediction_history
        (
        user_id,
        prediction_type,
        result
        )

        VALUES(?,?,?)

        """,
        (
            user_id,
            prediction_type,
            result
        )
    )


    conn.commit()

    conn.close()



# ==========================================
# GET USER PREDICTIONS
# ==========================================

def get_history(user_id):

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
        prediction_type,
        result,
        date

        FROM prediction_history

        WHERE user_id=?

        ORDER BY date DESC

        """,
        (user_id,)
    )


    history = cursor.fetchall()


    conn.close()


    return history