import unittest
from app import paginate

class Acceptance(unittest.TestCase):
    def test_first_page(self):
        self.assertEqual(paginate(list(range(10)), 1, 3), [0, 1, 2])
    def test_second_page(self):
        self.assertEqual(paginate(list(range(10)), 2, 3), [3, 4, 5])
    def test_empty_and_last_page(self):
        self.assertEqual(paginate([], 1, 3), [])
        self.assertEqual(paginate(list(range(10)), 4, 3), [9])
        self.assertEqual(paginate([1], 9, 3), [])
    def test_invalid(self):
        for page, size in [(0, 2), (1, 0), (-1, 3), (True, 3), (1, False), (1.5, 3), (1, '3')]:
            with self.subTest(page=page, size=size), self.assertRaises(ValueError):
                paginate([1, 2], page, size)

if __name__ == '__main__':
    unittest.main(verbosity=2)
