# login.py - Placeholder for login functionality
import csv
import string
import bcrypt

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
    valid_credentials = False
    special_characters = "!@#"

    if username:
        valid_credentials = True
        if not isinstance(username,str):
            raise TypeError("username must be a string")
    else:
        raise ValueError("username must not be empty.")
    
    if valid_credentials:
        for character in username:
            if character in special_characters:
                valid_credentials = False
                raise ValueError("No special characters allowed")
            else:
                continue
    
    if valid_credentials:
        if password:
            if not isinstance(password,str):
                raise TypeError("password must be a string")
        else:
            raise ValueError("password must not be empty")
    
    file = "database.csv"
    usernames = []
    hashed_passwords = []
    with open(file) as file_object:
        reader = csv.reader(file_object)
        columns = next(reader)
        for row in reader:
            usernames.append(row[0])
            hashing_password = bcrypt.hashpw(row[1].encode("utf-8"),bcrypt.gensalt())
            hashed_passwords.append(hashing_password)
    if username not in usernames:
        return False
    elif username in usernames:
        user_index = usernames.index(username)
        hashed_password = hashed_passwords[user_index]
        return bcrypt.checkpw(password.encode("utf-8"),hashed_password)

#print(login("nonexistent_user", "any_password"))
