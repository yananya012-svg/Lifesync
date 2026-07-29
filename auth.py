import sqlite3
import bcrypt

# -------------------------------------
# CREATE DATABASE
# -------------------------------------

def create_database():

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        full_name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password BLOB NOT NULL

    )
    """)

    conn.commit()

    conn.close()


# Create database automatically
create_database()


# -------------------------------------
# Register New User
# -------------------------------------

def register_user(full_name, email, password):

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    existing_user = cursor.fetchone()

    if existing_user:

        conn.close()

        return False, "Email already registered."

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    cursor.execute(
        """
        INSERT INTO users(
            full_name,
            email,
            password
        )
        VALUES(?,?,?)
        """,
        (
            full_name,
            email,
            hashed_password
        )
    )

    conn.commit()

    conn.close()

    return True, "Account Created Successfully."


# -------------------------------------
# Login User
# -------------------------------------

def login_user(email, password):

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if user is None:

        return False, "User not found."

    stored_password = user[3]

    if bcrypt.checkpw(
        password.encode("utf-8"),
        stored_password
    ):

        return True, user

    return False, "Incorrect Password."