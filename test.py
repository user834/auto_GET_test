import unittest
import requests


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.req = requests.get('https://run.mocky.io/v3/71559898-cb90-4694-ade9-2bbc9567f74b')

    def test_status_code(self):
        self.assertEqual(self.req.ok, True)
        self.assertEqual(self.req.reason, 'OK')
        self.assertEqual(self.req.status_code, 200)

    def test_content(self):
        self.assertEqual(self.req.content, b'{"body":"ok"}')

    def test_encoding(self):
        self.assertEqual(self.req.apparent_encoding, 'ascii')

    def test_redirect(self):
        self.assertEqual(self.req.history, [])
        self.assertEqual(self.req.is_redirect, False)
        self.assertEqual(self.req.is_permanent_redirect, False)


if __name__ == '__main__':
    unittest.main()
