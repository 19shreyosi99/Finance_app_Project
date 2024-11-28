from database.db_manager import connect_to_database

def register_user():
    
    #Registers a new user by adding their username and password to the database.
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            # Check if username already exists
            cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
            if cursor.fetchone():
                print("Username already exists. Please try a different one.")
                return

            # Insert the new user into the database
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password)
            )
            connection.commit()
            print("Registration successful!")
        except Exception as e:
            print(f"An error occurred during registration: {e}")
        finally:
            connection.close()