import unittest
from main import get_indexed
from main import get_index_from_number
class Test_2048(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_indexed(1,2), 7)
    def test_2(self):
        self.assertEqual(get_index_from_number(1), (0,0))
if __name__ == '__main__':
    unittest.main()