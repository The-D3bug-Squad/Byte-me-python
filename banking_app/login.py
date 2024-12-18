import sys
# login.py - Placeholder for login functionality

def login(username, password):
    """
    Handles the user login process by verifying the provided username and password.

    Instructions for Implementation:
    1. **Input Validation**:
        - Ensure both `username` and `password` are non-empty strings.
        - If either `username` or `password` is empty, raise a `ValueError`.
        - Validate that the `username` does not contain special characters (e.g., !, @, #, etc.). If it does, raise a `ValueError`.
    
    2. **User Authentication**:
        - Check if the provided `username` exists in the user database.
        - If the `username` does not exist, return `False` (login fails).
        - If the `username` exists, retrieve the stored password for that user.
        - Compare the provided `password` with the stored password (e.g., compare hashed versions if you're using password hashing).
    
    3. **Password Verification**:
        - If the `password` matches the stored password, return `True` (login successful).
        - If the `password` does not match, return `False` (login fails).

    4. **Edge Cases**:
        - Handle cases where the `username` or `password` is empty or contains invalid characters.
        - Handle cases where the `username` does not exist in the database.
        - Ensure that the password comparison is secure (e.g., using hash functions if applicable).

    Parameters:
    - `username` (str): The username of the user attempting to log in.
    - `password` (str): The password provided by the user.

    Returns:
    - bool: `True` if login is successful, `False` if login fails, or raises a `ValueError` for invalid input.

    """
    if validate_input(username,password):
        if authenticate_user(username, password):
            return True

    return False

def validate_input(username, password):
    if username == "" or password == "":
        raise ValueError("Can not have empty password or username")
    
    if username.isalnum() == False:
        raise ValueError("Username can not have special characters")

    return True

def authenticate_user(username,password): 
    try:
        with open("database.csv", "r") as file:
            people = file.readlines()
    except FileNotFoundError:
        sys.exit("Database not found")

    for person in people:
        person = person.split(",")
        if username in person:
            return password_validation(password, person[1])

    return False

def password_validation(password1 , password2):
    if password1 == password2:
        return True
    else:
        return False