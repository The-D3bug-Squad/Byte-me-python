# signup.py - Placeholder for signup functionality
import csv
import bcrypt

def password_valid(password):
    valid_password = False
    if len(password) >= 8:
        valid_password = True
    
    if valid_password:
        for character in password:
            if character.isupper():
                valid_password = True
                break
            else:
                valid_password = False
    
    if valid_password:
        for character in password:
            if character.islower():
                valid_password = True
                break
            else:
                valid_password = False
    
    if valid_password:
        for character in password:
            if character.isdigit():
                valid_password = True
                break
            else:
                valid_password = False
    
    return valid_password
            

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
    valid_credentials = False
    database_file = "database.csv"

    if username and isinstance(username,str):
        all_users = []
        with open(database_file,'r') as file:
            reader = csv.reader(file)
            columns = next(reader)
            for row in reader:
                all_users.append(row[0])
        if username not in all_users:
            valid_credentials = True
        else:
            raise ValueError("username already exists")
    else:
        raise ValueError("username you've entered is invalid")
    
    if valid_credentials:
        if password and isinstance(password,str):
            if password_valid(password):
                hashed_password = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt())
            else:
                valid_credentials = False
                raise ValueError("password does not meet requirements")
        else:
            valid_credentials = False
            raise ValueError("password you've entered is invalid")
    
    if valid_credentials:
        if email and isinstance(email,str):
            email_regular_expression = "@example.com"
            if email_regular_expression in email:
                pass
            else:
                valid_credentials = False
                raise ValueError("email you've entered is invalid")
        else:
            valid_credentials = False
            raise ValueError("email must be a populated text")
    
    if valid_credentials:
        row_counter = 0
        starting_balance = 0

        with open(database_file,'r+') as file:
            reader = csv.reader(file)
            columns = next(reader)
            for row in reader:
                row_counter+=1
            account_no = f"account{row_counter+1}"
            acc_details = {'username':username,'password':hashed_password,'email':email,'account_id':account_no,'balance':starting_balance}
            write_to_csv = csv.DictWriter(file,fieldnames=columns)
            write_to_csv.writerow(acc_details)
    
    return valid_credentials

#print(signup("newuser", "SecurePass123", "newuser@example.com"))
    


