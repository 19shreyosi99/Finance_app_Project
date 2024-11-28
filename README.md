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
      <p>Establishes a connection to a MySQL database using the provided credentials.</p>
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

  <section class="installation">
    <h2>Installation</h2>
    <p>Clone the repository:</p>
    <pre><code>git clone https://github.com/your-username/finance-management.git</code></pre>
    <p>Install dependencies:</p>
    <pre><code>pip install pymysql</code></pre>
    <p>Set up the MySQL database: Create a database in MySQL with the necessary tables (users, transactions, budgets, etc.). You can use the provided SQL scripts to set up the schema.</p>
    <p>Configure database credentials: Update the connection details (host, user, password, database) in the <code>config.py</code> file.</p>
  </section>

  <section class="usage">
    <h2>Usage</h2>
    <h3>1. User Registration</h3>
    <p>To register a new user, you will be prompted for a username and password. If the username is not already taken, the user will be added to the database.</p>
    <h3>2. User Login</h3>
    <p>When logging in, the system will ask for your username and password. If the credentials are correct, you will be granted access to the system.</p>
    <h3>3. Manage Transactions</h3>
    <ul>
      <li><strong>Add a Transaction:</strong> You can add a new transaction by providing details such as the amount, category, and whether it is an income or expense.</li>
      <li><strong>View Transactions:</strong> Displays all your transactions ordered by date.</li>
      <li><strong>Delete Transaction:</strong> Deletes a transaction by providing the transaction date.</li>
    </ul>
    <h3>4. Budget Management</h3>
    <ul>
      <li><strong>Set a Budget:</strong> Define spending limits for specific categories.</li>
      <li><strong>View Budgets:</strong> Displays all your budgets with their limits.</li>
      <li><strong>Check Budget:</strong> Alerts you if any category exceeds its budget.</li>
    </ul>
    <h3>5. Financial Reports</h3>
    <ul>
      <li><strong>Generate Monthly Report:</strong> Generates a financial report for the current month.</li>
      <li><strong>Generate Yearly Report:</strong> Generates a report for the entire year.</li>
    </ul>
  </section>

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
