import unittest
from unittest.mock import patch
from tracker.income_expense import add_transaction
from tracker.budget import set_budget

class TestTracker(unittest.TestCase):

    @patch("tracker.income_expense.connect_to_database")
    def test_add_transaction_success(self, mock_connect):
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        # Simulate adding a transaction
        mock_cursor.execute.return_value = None
        mock_conn.commit.return_value = None

        add_transaction("test_user", 100.00, "Food", "expense")
        mock_cursor.execute.assert_called_with(
            "INSERT INTO transactions (user_id, amount, category, type, date) VALUES ((SELECT id FROM users WHERE username = %s), %s, %s, %s, %s)",
            ("test_user", 100.00, "Food", "expense", mock_cursor.execute.call_args[0][4]),
        )

    @patch("tracker.budget.connect_to_database")
    def test_set_budget_success(self, mock_connect):
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        # Simulate setting a budget
        mock_cursor.execute.return_value = None
        mock_conn.commit.return_value = None

        set_budget("test_user", "Food", 200.00)
        mock_cursor.execute.assert_called_with(
            "INSERT INTO budgets (user_id, category, limit_amount) VALUES ((SELECT id FROM users WHERE username = %s), %s, %s) ON DUPLICATE KEY UPDATE limit_amount = %s",
            ("test_user", "Food", 200.00, 200.00),
        )

if __name__ == "__main__":
    unittest.main()