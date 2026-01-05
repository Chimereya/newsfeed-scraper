import unittest
from app import app


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()


    def test_news_endpoint(self):
        response = self.client.get('/news')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json) >= 0)


if __name__ == '__main__':
    unittest.main()