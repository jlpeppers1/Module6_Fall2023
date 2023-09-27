import unittest
from main.area import area

class MyTestCase(unittest.TestCase):

    def test_standard_rectangle(self):
        #Rectacngle with sides: 4,5; 4*5=20
        expected = 20
        actual = area(4,5)
        self.assertEqual(expected, actual)

    def test_standard_square(self):
        #Square with sides: 5; 5*5=20
        expected = 25
        actual = area(5)
        self.assertEqual(expected, actual)

    def test_invalid_input(self):
        # notice the with keyword, and the Error Type we are expecting
        with self.assertRaises(ValueError):
            area('alpha', 'bravo')

    def test_invalid_negative_input(self):
        # notice the with keyword, and the Error Type we are expecting
        with self.assertRaises(ValueError):
            area(-10,4)

    def test_exception_negative_second(self):
        # notice the with keyword, and the Error Type we are expecting
        with self.assertRaises(ValueError):
            area(1, -4)

    def test_exception_negative_both(self):
        # notice the with keyword, and the Error Type we are expecting
        with self.assertRaises(ValueError):
            area(-1, -4)

if __name__ == '__main__':
    unittest.main()
