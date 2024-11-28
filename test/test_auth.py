import unittest
from unittest.mock import patch
from authentication.register import register_user
from authentication.login import login_user
from database.db_manager import connect_to_database

class TestAuth(unittest.TestCase):

    @patch("auth.register.connect_to_database")
    def test_register_user_success(self, mock_connect):
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        # Simulate successful user registration
        mock_cursor.execute.return_value = None
        mock_conn.commit.return_value = None

        with patch("builtins.input", side_effect=["test_user", "password123"]):
            register_user()
            mock_cursor.execute.assert_called_with(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                ("test_user", "password123"),
            )

    @patch("auth.login.connect_to_database")
    def test_login_user_success(self, mock_connect):
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        # Simulate successful login
        mock_cursor.fetchone.return_value = (1,)

        with patch("builtins.input", side_effect=["test_user", "password123"]):
            user = login_user()
            self.assertEqual(user, "test_user")

    @patch("auth.login.connect_to_database")
    def test_login_user_failure(self, mock_connect):
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        # Simulate login failure
        mock_cursor.fetchone.return_value = None

        with patch("builtins.input", side_effect=["invalid_user", "wrong_password"]):
            user = login_user()
            self.assertIsNone(user)

if __name__ == "__main__":
    unittest.main()
