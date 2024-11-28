from database.db_manager import connect_to_database

def login_user():
    
    #Authenticates a user by verifying their username and password.
    
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            # Verify the username and password
            cursor.execute(
                "SELECT id FROM users WHERE username = %s AND password = %s",
                (username, password)
            )
            user = cursor.fetchone()
            if user:
                print("Login successful!")
                return username  # Return the username for session tracking
            else:
                print("Invalid credentials! Please try again.")
                return None
        except Exception as e:
            print(f"An error occurred during login: {e}")
        finally:
            connection.close()
