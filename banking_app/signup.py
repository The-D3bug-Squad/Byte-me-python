# signup.py - Placeholder for signup functionality
from user_management import read_users, write_users


def signup(username, password, email):
    """
    Handles the user signup process by validating the provided username, password, and email.

    Instructions for Implementation:
    1. **Input Validation**:
        - Ensure that all fields (`username`, `password`, `email`) are non-empty strings.
        - If any field is empty, raise a `ValueError`.
        - Validate that the `email` follows the correct format (e.g., using a regular expression for email validation).
        - Ensure the `password` meets minimum security criteria (e.g., at least 8 characters long, contains a mix of uppercase, lowercase, and digits).
        - If the `password` is weak (e.g., a simple password like "123"), raise a `ValueError`.

    2. **Username Uniqueness Check**:
        - Check if the `username` already exists in the user database.
        - If the `username` is already taken, raise a `ValueError`.

    3. **Create New User**:
        - If all validations pass and the username is unique, create a new user with the provided `username`, `password`, and `email`.
        - The `password` should be securely hashed before storing it (if using password hashing).
        - Add the new user to the user database.

    4. **Edge Cases**:
        - Handle cases where any of the input fields are empty.
        - Handle invalid email formats using proper regular expression checks.
        - Handle cases where the `username` is already taken.
        - Ensure that weak passwords (e.g., less than 8 characters or easily guessable) are rejected.

    Parameters:
    - `username` (str): The desired username for the new user.
    - `password` (str): The password chosen by the user.
    - `email` (str): The email address provided by the user.

    Returns:
    - bool: `True` if the signup is successful, otherwise raises a `ValueError` for invalid input.
    """
    if not username or not isinstance(username, str):
        raise ValueError("Username must be a non-empty strin ")
    if not password or not isinstance(password, str):
        raise ValueError("Password must be a non-empty")
    if not email or not isinstance(email, str):
        raise ValueError("email must be a non-empty ")

    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if not re.match(email_regex, email):
        raise ValueError("Invalid email format.")

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")

    if not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter.")

    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter.")

    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")

    weak_passwords = ["12345678", "password", "00000", "123456", "1234578", "123"]
    if password in weak_passwords:
        raise ValueError("Password is too weak.")

    # **Username Uniqueness Check**:
    #     - Check if the `username` already exists in the user database.
    #     - If the `username` is already taken, raise a `ValueError`.

    users = read_users()

    for user in users:
        if username == user["username"]:
            raise ValueError("user exist")

    user = {
        "username": username,
        "password": password,
        "email": email,
    }
    write_user = write_user()

    write_user(user)

    return True
