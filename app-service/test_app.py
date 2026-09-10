import unittest
from app import app

class TestHealthCheck(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_healthz_returns_200(self):
        response = self.client.get("/healthz")
        self.assertEqual(response.status_code, 200)

    def test_healthz_returns_expected_body(self):
        response = self.client.get("/healthz")
        data = response.get_json()
        self.assertEqual(data["status"], "healthy")

if __name__ == "__main__":
    unittest.main()