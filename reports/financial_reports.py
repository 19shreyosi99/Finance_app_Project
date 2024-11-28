from database.db_manager import connect_to_database
from datetime import datetime

def generate_monthly_report(user):
    
    #Generates a financial report for the current month.
    
    current_date = datetime.now()
    current_month = current_date.month
    current_year = current_date.year

    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            # Calculate total income and expenses for the current month
            cursor.execute(
                """
                SELECT type, SUM(amount)
                FROM transactions
                WHERE user_id = (SELECT id FROM users WHERE username = %s)
                  AND MONTH(date) = %s AND YEAR(date) = %s
                GROUP BY type
                """,
                (user, current_month, current_year)
            )
            results = cursor.fetchall()

            income = 0
            expenses = 0
            for record in results:
                if record[0] == 'income':
                    income = record[1]
                elif record[0] == 'expense':
                    expenses = record[1]

            savings = income - expenses
            print(f"\nMonthly Report for {current_date.strftime('%B %Y')}:")
            print(f"Total Income: ${income:.2f}")
            print(f"Total Expenses: ${expenses:.2f}")
            print(f"Net Savings: ${savings:.2f}")

        except Exception as e:
            print(f"An error occurred while generating the monthly report: {e}")
        finally:
            connection.close()

def generate_yearly_report(user):
    
    #Generates a financial report for the current year.
    
    current_year = datetime.now().year

    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            # Calculate total income and expenses for the current year
            cursor.execute(
                """
                SELECT type, SUM(amount)
                FROM transactions
                WHERE user_id = (SELECT id FROM users WHERE username = %s)
                  AND YEAR(date) = %s
                GROUP BY type
                """,
                (user, current_year)
            )
            results = cursor.fetchall()

            income = 0
            expenses = 0
            for record in results:
                if record[0] == 'income':
                    income = record[1]
                elif record[0] == 'expense':
                    expenses = record[1]

            savings = income - expenses
            print(f"\nYearly Report for {current_year}:")
            print(f"Total Income: ${income:.2f}")
            print(f"Total Expenses: ${expenses:.2f}")
            print(f"Net Savings: ${savings:.2f}")

        except Exception as e:
            print(f"An error occurred while generating the yearly report: {e}")
        finally:
            connection.close()