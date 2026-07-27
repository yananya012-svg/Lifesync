from auth import register_user, login_user

# Register a user
success, message = register_user(
    "Ananya",
    "ananya@gmail.com",
    "123456"
)

print(success)
print(message)

# Login
success, user = login_user(
    "ananya@gmail.com",
    "123456"
)

print(success)
print(user)