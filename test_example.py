import unittest
from main import working

class TestExample(unittest.TestCase):
    def test_working(self):
        self.assertEqual(working(), "working...")

if __name__ == '__main__':
    unittest.main()