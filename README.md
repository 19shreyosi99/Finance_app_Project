<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
  <header>
    <h1>Personal Finance Management System</h1>
  </header>

  <section class="intro">
    <p>This system helps users manage their finances, including tracking income and expenses, setting budgets, and generating financial reports. It supports features such as user registration, login, and transaction management.</p>
  </section>

  <section class="features">
    <h2>Features</h2>
    <div class="feature">
      <h3>Database Connection</h3>
      <ul>
        <li><strong>Establishes a connection to a MySQL database using the provided credentials.</li>
        <li><strong>Automatically sets up and ensures all necessary database tables are ready for use.</li>
      </ul>
   
     
  </div>
    <div class="feature">
      <h3>User Authentication</h3>
      <ul>
        <li><strong>Login:</strong> Verifies a user’s credentials to allow access to the system.</li>
        <li><strong>Registration:</strong> Allows new users to sign up by creating a username and password.</li>
      </ul>
    </div>
    <div class="feature">
      <h3>Financial Transactions</h3>
      <ul>
        <li><strong>Add Transaction:</strong> Records a new income or expense transaction.</li>
        <li><strong>View Transactions:</strong> Displays all transactions for the user, ordered by date.</li>
        <li><strong>Delete Transaction:</strong> Deletes a transaction based on the date.</li>
      </ul>
    </div>
    <div class="feature">
      <h3>Budget Management</h3>
      <ul>
        <li><strong>Set Budget:</strong> Allows users to set or update budget limits for specific categories (e.g., groceries, entertainment).</li>
        <li><strong>View Budget:</strong> Displays all budgets with their respective limits.</li>
        <li><strong>Check Budget:</strong> Monitors whether a user has exceeded their budget in any category.</li>
      </ul>
    </div>
    <div class="feature">
      <h3>Financial Reporting</h3>
      <ul>
        <li><strong>Monthly Report:</strong> Generates a report detailing total income, expenses, and savings for the current month.</li>
        <li><strong>Yearly Report:</strong> Generates a report detailing total income, expenses, and savings for the current year.</li>
      </ul>
    </div>
  </section>

 <section>
  <h2>Installation</h2>
  <p>Follow these steps to set up the Personal Finance Management System:</p>

  <h3>1. Clone the Repository</h3>
  <p>Open Git Bash and navigate to the directory where you want to save the project:</p>
  <pre><code>cd "path"</code></pre>
  <p>Then, clone the repository using the following command:</p>
  <pre><code>git clone https://github.com/19shreyosi99/Finance_app_Project.git</code></pre>
  <p>Navigate into the cloned project directory:</p>
  <pre><code>cd Finance_app_Project</code></pre>

  <h3>2. Install Dependencies</h3>
  <p>Install the necessary dependencies by running the following command:</p>
  <pre><code>python -m pip install pymysql</code></pre>

  <h3>3. Set Up the MySQL Database</h3>
  <p>Create a new database called <strong>dbo</strong> in MySQL:</p>
  <pre><code>CREATE DATABASE dbo;</code></pre>
  <p>You can use the provided SQL scripts to set up the schema (users, transactions, budgets, etc.) in the database.</p>

  <h3>4. Configure Database Credentials</h3>
  <p>Update the connection details in the <code>db_manager.py</code> file. Replace the placeholder values with your MySQL credentials (host, user, password, and database).</p>

  <h3>5. Running the Application</h3>
  <p>After completing the installation and configuration, you are ready to run the application:</p>
  <pre><code>python main.py</code></pre>

  <p>The application will now be up and running!</p>
</section>

  <div class="container">
       <h1>Application Usage Guide</h1>
       <p>This document provides a step-by-step guide for using the application, including registration, login, and accessing various features.</p>

  <h2>Main Menu Options</h2>
        <p>When you start the application, you will be presented with the <strong>Main Menu</strong>. Choose an option by entering the corresponding number:</p>
        <ul>
            <li><strong>1</strong>: Register</li>
            <li><strong>2</strong>: Login</li>
            <li><strong>3</strong>: Exit</li>
        </ul>

  <h2>How to Use the Application</h2>

  <h3>Step 1: Register a New Account</h3>
        <ol>
            <li>From the Main Menu, enter <code>1</code>.</li>
            <li>Provide a <strong>username</strong> and <strong>password</strong> when prompted.</li>
            <li>After successful registration, you will see the message:</li>
        </ol>
        <pre>Registration successful!</pre>

  <h3>Step 2: Login to Your Account</h3>
        <ol>
            <li>From the Main Menu, enter <code>2</code>.</li>
            <li>Enter your <strong>username</strong> and <strong>password</strong>.</li>
            <li>On successful login, you will see:</li>
        </ol>
        <pre>Login successful!
Welcome, &lt;username&gt;!</pre>

  <h3>Step 3: Navigate the Features</h3>
        <p>After logging in, the following menu will appear. Enter the corresponding number to perform an action:</p>
        <ul>
            <li><strong>1</strong>: Manage Transactions - Add, update, or delete transactions.</li>
            <li><strong>2</strong>: Manage Budgets - Set and modify budget categories.</li>
            <li><strong>3</strong>: View Transactions - Display a list of all recorded transactions.</li>
            <li><strong>4</strong>: View Budgets - View budget details and status.</li>
            <li><strong>5</strong>: Check Budgets - Compare expenses against your budget limits.</li>
            <li><strong>6</strong>: Generate Reports - Create financial reports based on transactions and budgets.</li>
            <li><strong>7</strong>: Logout - Log out of the application safely.</li>
        </ul>

  <h3>Step 4: Logout</h3>
        <p>When you're done using the application, enter <code>7</code> to logout. You will see the message:</p>
        <pre>Logging out..</pre>

  <h2>Exit the Application</h2>
        <p>To exit the application at any time:</p>
        <ol>
            <li>From the Main Menu, enter <code>3</code>.</li>
        </ol>

  <div class="note">
            <h3>Important Notes</h3>
            <ul>
                <li>Ensure you remember your <strong>username</strong> and <strong>password</strong> for future logins.</li>
                <li>Always logout after completing your tasks to secure your account.</li>
            </ul>
        </div>
        <p>Enjoy using the application! 😊</p>
  </div>

  <section class="backup-guide">
    <h2>How to Back Up and Restore a Specific Table in MySQL</h2>
    <h3>1. Backing Up a Specific Table</h3>
    <h4>Step 1: Log in to the MySQL Server</h4>
    <pre><code>mysql -u username -p</code></pre>
    <p>Replace <code>username</code> with your MySQL username.</p>
    <h4>Step 2: Use mysqldump</h4>
    <pre><code>mysqldump -u username -p database_name table_name > table_backup.sql</code></pre>
    <p>Replace <code>username</code>, <code>database_name</code>, and <code>table_name</code> as needed.</p>
    <h3>2. Restoring a Specific Table</h3>
    <pre><code>mysql -u username -p database_name < table_backup.sql</code></pre>
    <p>Replace <code>username</code>, <code>database_name</code>, and <code>table_backup.sql</code> as needed.</p>
  </section>

  <footer>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
  </footer>
</body>
</html>
