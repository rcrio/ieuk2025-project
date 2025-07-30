import unittest
from collections import Counter
import pandas as pd
import analyser
import tempfile
import os

class TestAnalyser(unittest.TestCase):
    def setUp(self):
        """Create a temporary log file for testing."""
        self.test_data = (
            "192.168.0.1 GET /index.html\n"
            "192.168.0.2 POST /submit\n"
            "192.168.0.1 GET /about\n"
            "192.168.0.3 GET /contact\n"
            "192.168.0.2 GET /home\n"
        )
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        self.temp_file.write(self.test_data)
        self.temp_file.close()

    def tearDown(self):
        """Remove temporary file after test."""
        os.unlink(self.temp_file.name)

    def test_extract_ips(self):
        ips = analyser.extract_ips(self.temp_file.name)
        expected_ips = [
            "192.168.0.1", "192.168.0.2", "192.168.0.1", "192.168.0.3", "192.168.0.2"
        ]
        self.assertEqual(ips, expected_ips)

    def test_count_requests(self):
        ips = ["192.168.0.1", "192.168.0.2", "192.168.0.1"]
        counter = analyser.count_requests(ips)
        expected = Counter({"192.168.0.1": 2, "192.168.0.2": 1})
        self.assertEqual(counter, expected)

    def test_create_dataframe(self):
        counter = Counter({"192.168.0.1": 2, "192.168.0.2": 1})
        df = analyser.create_dataframe(counter)
        self.assertIn("IP", df.columns)
        self.assertIn("RequestCount", df.columns)
        self.assertEqual(len(df), 2)
        self.assertEqual(df.loc[df["IP"] == "192.168.0.1", "RequestCount"].values[0], 2)

    def test_get_statistics(self):
        counter = Counter({"192.168.0.1": 2, "192.168.0.2": 1, "192.168.0.3": 4})
        df = analyser.create_dataframe(counter)
        stats = analyser.get_statistics(df)
        self.assertEqual(stats["total_unique_ips"], 3)
        self.assertEqual(stats["total_requests"], 7)
        self.assertAlmostEqual(stats["mean"], 7 / 3)
        self.assertEqual(stats["median"], 2)
        self.assertIsInstance(stats["top_hits"], pd.DataFrame)
        self.assertEqual(stats["top_hits"].iloc[0]["IP"], "192.168.0.3")

if __name__ == '__main__':
    unittest.main()