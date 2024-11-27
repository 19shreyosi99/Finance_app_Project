# Finance_app_Project
For Database Connection Code
1. Purpose:
    This script establishes a connection to a MySQL database using the pymysql library.
2. Key Functionality:
    The connect_to_database() function:
    Tries to connect to a MySQL database using credentials and parameters provided (host, user, password, database).
    Returns the connection object if the connection is successful.
    Handles connection errors by catching pymysql.MySQLError and printing the error message.
    Returns None in case of a failure.
3. Usage:
    This function is typically called to get a live database connection, which can then be used for executing queries.
   
For Login User Code
1. Purpose:
    Authenticates a user by verifying their credentials.
2. Functionality:
    Prompts the user for a username and password.
    Connects to the database using connect_to_database().
    Executes a query to check the provided credentials.
    Prints a success message for valid credentials or an error for invalid ones.
    Handles database errors and ensures the connection is closed.

For Register User Code
1. Purpose:
    Registers a new user by adding their credentials to the database.
2. Functionality:
    Prompts the user for a username and password.
    Checks if the username already exists in the database.
    Adds the new user's credentials if the username is unique.
    Ensures database changes are committed and handles errors during the process.

For Financial Report Code
1. Purpose:
    Generates monthly and yearly financial reports for a user.
2. Functions:
   generate_monthly_report(user):
    Calculates total income, expenses, and net savings for the current month.
    Retrieves and aggregates data from the database using the user’s ID.
   generate_yearly_report(user):
    Calculates total income, expenses, and net savings for the current year.
    Retrieves and aggregates data from the database using the user’s ID.
   Common Functionality:
    Connects to the database using connect_to_database().
    Queries the transactions table for data grouped by type (income or expense).
    Handles errors during query execution and ensures the connection is closed.

For Financial Reports Tests
  1. set_budget(user, category, limit_amount)
    Purpose: Sets or updates a budget limit for a user and category.
    SQL Operation: Inserts or updates budget record in the database.
  2. view_budget(user)
    Purpose: Displays all budgets for the given user.
    SQL Operation: Fetches and shows budgets with category and limit.
  3. check_budget(user)
    Purpose: Checks if the user has exceeded their budget for any category.
    SQL Operation: Compares total spent vs. limit for each category.

Financial Transactions Functions
  1. add_transaction(user, amount, category, transaction_type)
    Purpose: Adds a new income or expense transaction for the user.
    SQL Operation: Inserts the transaction into the transactions table.
2. view_transactions(user)
    Purpose: Retrieves and displays all transactions for the user.
    SQL Operation: Fetches transactions ordered by date.
3. delete_transaction(user, date)
    Purpose: Deletes a transaction based on the provided date.
    SQL Operation: Deletes the transaction from the transactions table.

for Authentication Unit Tests
1. Purpose:
    Tests the register_user and login_user functionalities to ensure they behave as expected.
2. Test Cases:
   test_register_user_success:
    Verifies that a new user is successfully registered in the database.
    Mocks database connections and inputs.
    Asserts that the correct SQL query is executed.
   test_login_user_success:
    Verifies successful login when valid credentials are provided.
    Mocks database connections and inputs.
    Asserts that the function returns the correct username.
    test_login_user_failure:
    Verifies login failure when invalid credentials are provided.
    Mocks database connections and inputs.
    Asserts that the function returns None.
3. Common Functionality:
    Utilizes unittest and unittest.mock for testing and mocking database interactions.
    Ensures database methods like cursor and execute are correctly called.
   
For Financial Reports Unit Tests
1. Purpose:
  Tests the generate_monthly_report and generate_yearly_report functions to ensure accurate financial calculations.
2. Test Cases:
  test_generate_monthly_report:
    Simulates database interaction to fetch monthly income and expense data.
    Mocks the database response with predefined values.
    Asserts that the printed output matches the calculated totals.
  test_generate_yearly_report:
    Simulates database interaction to fetch yearly income and expense data.
    Mocks the database response with predefined values.
    Asserts that the printed output matches the calculated totals.
3. Common Functionality:
    Utilizes unittest and unittest.mock for mocking database connections and print statements.
    Ensures calculations and outputs are consistent with the mock data.

For Tracker Unit Tests
1. test_add_transaction_success
    Purpose: Verifies add_transaction inserts a transaction record correctly.
    Mocked: Database connection and cursor.
    Check: Ensures the correct SQL query is executed with proper parameters.
2. test_set_budget_success
    Purpose: Verifies set_budget inserts or updates a budget correctly.
    Mocked: Database connection and cursor.
    Check: Ensures the correct SQL query is executed with proper parameters.
   




