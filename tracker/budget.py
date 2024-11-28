from database.db_manager import connect_to_database

def set_budget(user, category, limit_amount):

    #Sets a budget for a specific category.
    
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO budgets (user_id, category, limit_amount) VALUES ((SELECT id FROM users WHERE username = %s), %s, %s) ON DUPLICATE KEY UPDATE limit_amount = %s",
                (user, category, limit_amount, limit_amount)
            )
            connection.commit()
            print("Budget set successfully!")
        except Exception as e:
            print(f"An error occurred while setting the budget: {e}")
        finally:
            connection.close()

def view_budget(user):
    
    #Displays all budgets for the user.
    
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT category, limit_amount FROM budgets WHERE user_id = (SELECT id FROM users WHERE username = %s)",
                (user,)
            )
            budgets = cursor.fetchall()
            if budgets:
                print("\nYour Budgets:")
                for budget in budgets:
                    print(f"Category: {budget[0]}, Limit: {budget[1]}")
            else:
                print("No budgets found.")
        except Exception as e:
            print(f"An error occurred while retrieving budgets: {e}")
        finally:
            connection.close()

def check_budget(user):
    
    #Checks if the user has exceeded their budget for any category.
    
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT b.category, b.limit_amount, 
                       IFNULL(SUM(t.amount), 0) AS total_spent
                FROM budgets b
                LEFT JOIN transactions t ON b.user_id = t.user_id AND b.category = t.category
                WHERE b.user_id = (SELECT id FROM users WHERE username = %s)
                GROUP BY b.category, b.limit_amount
                """,
                (user,)
            )
            results = cursor.fetchall()
            for result in results:
                category, limit, spent = result
                if spent > limit:
                    print(f"WARNING: You have exceeded your budget for {category}!")
                else:
                    print(f"Category: {category}, Limit: {limit}, Spent: {spent}")
        except Exception as e:
            print(f"An error occurred while checking budgets: {e}")
        finally:
            connection.close()
