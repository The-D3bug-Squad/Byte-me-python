# signup.py - Placeholder for signup functionality
import re
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
    if username == "" or password == "" or email == "":
        raise ValueError

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError

    pass_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(.{8,})$"
    if not re.match(pass_pattern, password):
        raise ValueError

    """
    username,password,email,account_id,balance
    johndoe,hashed_password,johndoe@example.com,account1,1000.50
    """

    with open("database.csv", "r", errors="ignore") as f:
        contents = f.readlines()
    for user in contents:
        user.replace("\n", "")
        saved_username, other = user.split(",", 1)
        if username == saved_username:
            raise ValueError

    with open("database.csv", "a") as f:
        f.write(f"{username},{password},{email}")
    return True

if __name__ == "__main__":
    signup("newuser", "SecurePass123", "newuser@example.com")