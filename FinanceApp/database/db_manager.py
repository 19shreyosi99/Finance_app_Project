import pymysql

def connect_to_database():
    try:
        # Connect to the MySQL database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='admin123',
            database='dbo'
        )
        return connection

    except pymysql.MySQLError as e:
        print(f"Error while connecting to MySQL: {e}")
        return None


def check_and_create_tables():
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      username VARCHAR(255) NOT NULL UNIQUE,
      password VARCHAR(255) NOT NULL
    );
    """
    
    create_budgets_table = """
    CREATE TABLE IF NOT EXISTS budgets (
      id INT AUTO_INCREMENT PRIMARY KEY,
      user_id INT NOT NULL,
      category VARCHAR(255),
      limit_amount DECIMAL(10,2) NOT NULL,
      FOREIGN KEY (user_id) REFERENCES users(id),
      UNIQUE KEY unique_user_category (user_id, category)
    );
    """
    
    create_transactions_table = """
    CREATE TABLE IF NOT EXISTS transactions (
      id INT AUTO_INCREMENT PRIMARY KEY,
      user_id INT NOT NULL,
      amount DECIMAL(10,2) NOT NULL,
      category VARCHAR(255),
      date DATETIME,
      type ENUM('income', 'expense'),
      FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """
    
    connection = connect_to_database()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute(create_users_table)             
                cursor.execute(create_budgets_table)        
                cursor.execute(create_transactions_table)     
            connection.commit()
        except pymysql.MySQLError as e:
            print(f"Error while creating tables: {e}")
        finally:
            connection.close()
    else:
        print("Failed to connect to the database.")