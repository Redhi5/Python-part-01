def login_system():
    # Define a dictionary of valid usernames and passwords
    credentials = {"admin": "password123", "user1": "securepass", "testuser": "test1234"}

    username_input = input("Enter username: ")
    password_input = input("Enter password: ")

    if username_input in credentials and credentials[username_input] == password_input:
        print("Login successful! Welcome, " + username_input + "!")
    else:
        print("Invalid username or password.")

# Call the function to run the login system
login_system()