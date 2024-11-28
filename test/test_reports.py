import unittest
from unittest.mock import patch
from reports.financial_reports import generate_monthly_report, generate_yearly_report

class TestReports(unittest.TestCase):

    @patch("reports.financial_reports.connect_to_database")
    def test_generate_monthly_report(self, mock_connect):
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        # Simulate fetching data for the monthly report
        mock_cursor.fetchall.return_value = [("income", 5000.00), ("expense", 3000.00)]

        with patch("builtins.print") as mock_print:
            generate_monthly_report("test_user")
            mock_print.assert_any_call("Total Income: $5000.00")
            mock_print.assert_any_call("Total Expenses: $3000.00")
            mock_print.assert_any_call("Net Savings: $2000.00")

    @patch("reports.financial_reports.connect_to_database")
    def test_generate_yearly_report(self, mock_connect):
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        # Simulate fetching data for the yearly report
        mock_cursor.fetchall.return_value = [("income", 60000.00), ("expense", 36000.00)]

        with patch("builtins.print") as mock_print:
            generate_yearly_report("test_user")
            mock_print.assert_any_call("Total Income: $60000.00")
            mock_print.assert_any_call("Total Expenses: $36000.00")
            mock_print.assert_any_call("Net Savings: $24000.00")

if __name__ == "__main__":
    unittest.main()