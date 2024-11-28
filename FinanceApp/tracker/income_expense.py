from database.db_manager import connect_to_database

def add_transaction(user, amount, category, transaction_type):
    
    #Adds a new income or expense transaction.
    
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO transactions (user_id, amount, category, type, date) VALUES ((SELECT id FROM users WHERE username = %s), %s, %s, %s, NOW())",
                (user, amount, category, transaction_type)
            )
            connection.commit()
            print("Transaction added successfully!")
        except Exception as e:
            print(f"An error occurred while adding the transaction: {e}")
        finally:
            connection.close()

def view_transactions(user):
    
    #Retrieves and displays all transactions for the user.
    
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT amount, category, type, date FROM transactions WHERE user_id = (SELECT id FROM users WHERE username = %s) ORDER BY date DESC",
                (user,)
            )
            transactions = cursor.fetchall()
            if transactions:
                print("\nYour Transactions:")
                for transaction in transactions:
                    print(f"Amount: {transaction[0]}, Category: {transaction[1]}, Type: {transaction[2]}, Date: {transaction[3]}")
            else:
                print("No transactions found.")
        except Exception as e:
            print(f"An error occurred while retrieving transactions: {e}")
        finally:
            connection.close()

def delete_transaction(user, date):
    
    #Deletes a transaction based on the provided date.
    
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM transactions WHERE user_id = (SELECT id FROM users WHERE username = %s) AND date = %s",
                (user, date)
            )
            connection.commit()
            print("Transaction deleted successfully!")
        except Exception as e:
            print(f"An error occurred while deleting the transaction: {e}")
        finally:
            connection.close()