import sqlite3
import bcrypt


# -------------------------------------
# Register New User
# -------------------------------------

def register_user(full_name, email, password):

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    # Check if email already exists
    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    existing_user = cursor.fetchone()

    if existing_user:

        conn.close()

        return False, "Email already registered."

    # Hash password
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

    else:

        return False, "Incorrect Password."